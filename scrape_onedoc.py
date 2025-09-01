import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://www.onedoc.ch"
START_URL = "https://www.onedoc.ch/de/hautarzt-dermatologe/stadte"

def get_html(url):
    time.sleep(1)  # anti-blocage
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    r.raise_for_status()
    return r.text

def parse_doctor_page(url):
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    data = {}

    name = soup.select_one("h1")
    data["Doctor Name"] = name.get_text(strip=True) if name else ""

    practice = soup.select_one("h2")
    data["Practice Name"] = practice.get_text(strip=True) if practice else ""

    address_block = soup.select_one("address")
    if address_block:
        addr_lines = address_block.get_text("\n", strip=True).split("\n")
        if len(addr_lines) >= 2:
            data["Street / Address"] = addr_lines[0]
            if " " in addr_lines[1]:
                postal, city = addr_lines[1].split(" ", 1)
                data["Postal Code"] = postal
                data["City"] = city
        else:
            data["Street / Address"] = addr_lines[0]

    phone = soup.select_one("a[href^='tel:']")
    data["Phone"] = phone.get_text(strip=True) if phone else ""

    website = soup.select_one("a[href^='http']")
    data["Website"] = website["href"] if website else ""

    email = soup.select_one("a[href^='mailto:']")
    data["Email"] = email["href"].replace("mailto:", "") if email else ""

    data["Profile Link"] = url

    return data

def main():
    doctors = []
    html = get_html(START_URL)
    soup = BeautifulSoup(html, "html.parser")

    city_links = [a["href"] for a in soup.select("a[href*='/de/hautarzt-dermatologe/']")]

    for city_link in city_links:
        city_url = BASE_URL + city_link
        city_html = get_html(city_url)
        city_soup = BeautifulSoup(city_html, "html.parser")

        profile_links = [a["href"] for a in city_soup.select("a[href*='/de/hautarzt-dermatologe/']")]

        for profile in profile_links:
            profile_url = BASE_URL + profile
            try:
                doctor_data = parse_doctor_page(profile_url)
                doctors.append(doctor_data)
                print("✅ Collected:", doctor_data.get("Doctor Name", ""))
            except Exception as e:
                print("⚠️ Error:", profile_url, e)

    df = pd.DataFrame(doctors)
    df.to_excel("dermatologists_onedoc.xlsx", index=False)
    print("🎉 File saved: dermatologists_onedoc.xlsx")

if __name__ == "__main__":
    main()
