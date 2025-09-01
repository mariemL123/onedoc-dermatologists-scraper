import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = "https://www.onedoc.ch"
START_URL = "https://www.onedoc.ch/de/hautarzt-dermatologe/stadte"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_html(url):
    r = requests.get(url, headers=HEADERS, timeout=15)
    r.raise_for_status()
    return r.text

def parse_doctor_page(url):
    try:
        html = get_html(url)
        soup = BeautifulSoup(html, "html.parser")
        data = {}

        # Nom du docteur
        name = soup.select_one("h1")
        data["Doctor Name"] = name.get_text(strip=True) if name else ""

        # Cabinet
        practice = soup.select_one("h2")
        data["Practice Name"] = practice.get_text(strip=True) if practice else ""

        # Adresse
        address_block = soup.select_one("address")
        data["Street / Address"] = ""
        data["Postal Code"] = ""
        data["City"] = ""
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

        # Téléphone
        phone = soup.select_one("a[href^='tel:']")
        data["Phone"] = phone.get_text(strip=True) if phone else ""

        # Site
        website = soup.select_one("a[href^='http']")
        data["Website"] = website["href"] if website else ""

        # Email
        email = soup.select_one("a[href^='mailto:']")
        data["Email"] = email["href"].replace("mailto:", "") if email else ""

        # Lien profil
        data["Profile Link"] = url

        return data

    except Exception as e:
        return {"Doctor Name": "", "Error": str(e), "Profile Link": url}

def save_progress(doctors, filename="dermatologists_onedoc.xlsx"):
    df = pd.DataFrame(doctors)
    df.to_excel(filename, index=False)
    print(f"💾 Sauvegarde intermédiaire : {len(doctors)} fiches → {filename}")

def main():
    doctors = []

    # Étape 1 : récupérer toutes les villes
    html = get_html(START_URL)
    soup = BeautifulSoup(html, "html.parser")
    city_links = [a["href"] for a in soup.select("a[href*='/de/hautarzt-dermatologe/']")]

    # Étape 2 : collecter tous les profils
    profile_links = []
    for city_link in city_links:
        city_url = BASE_URL + city_link
        city_html = get_html(city_url)
        city_soup = BeautifulSoup(city_html, "html.parser")
        links = [a["href"] for a in city_soup.select("a[href*='/de/hautarzt-dermatologe/']")]
        profile_links.extend([BASE_URL + l for l in links])

    print(f"🔍 {len(profile_links)} profils trouvés.")

    # Étape 3 : multi-thread scraping
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(parse_doctor_page, url): url for url in profile_links}
        for i, future in enumerate(as_completed(futures), 1):
            data = future.result()
            doctors.append(data)
            print(f"✅ {i}/{len(profile_links)} récupéré : {data.get('Doctor Name','')}")

            # Sauvegarde toutes les 100 fiches
            if i % 100 == 0:
                save_progress(doctors, "dermatologists_onedoc_partial.xlsx")

    # Étape 4 : sauvegarde finale
    save_progress(doctors, "dermatologists_onedoc.xlsx")
    print("🎉 Fichier final enregistré : dermatologists_onedoc.xlsx")

if __name__ == "__main__":
    main()
