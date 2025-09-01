# 🩺 Onedoc Dermatologists Scraper

## 📌 Project Overview
This project is a **web scraping tool** built with Python to extract and organize data of dermatologists and practices from the Swiss medical directory [Onedoc.ch](https://www.onedoc.ch/de/hautarzt-dermatologe/stadte).

The script collects relevant details and saves them into a **structured Excel file** for easy usage and further analysis.

---

## 🚀 Features
- Scrapes all dermatologists and practices listed on Onedoc.ch.
- Extracts:
  - 👨‍⚕️ Doctor’s name
  - 🏥 Practice name
  - 📍 Street & Address
  - 🏙️ Postal Code & City
  - 📞 Phone number (if available)
  - 🌐 Website / 📧 Email (if available)
- Saves data into a clean **Excel file (`.xlsx`)** with clear headers.
- Handles missing data gracefully.

---

## 🛠️ Technologies Used
- **Python 3**
- [Requests](https://docs.python-requests.org/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
- [Pandas](https://pandas.pydata.org/)
- [OpenPyXL](https://openpyxl.readthedocs.io/)

---

## 📂 Project Structure
📦 onedoc-dermatologists-scraper
┣ 📜 scraper.py # Main scraping script
┣ 📜 requirements.txt # Dependencies
┣ 📜 README.md # Project documentation
┗ 📂 output
┗ dermatologists_onedoc.xlsx # Final exported data

## ▶️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/mariemL123/onedoc-dermatologists-scraper.git
   cd onedoc-dermatologists-scraper

2.**Install dependencies**
  pip install -r requirements.txt

3.**Run the scraper**
  python scraper.py
  
4.**Check the output** 

  The results will be saved in output/dermatologists_onedoc.xlsx

  
| Doctor Name       | Practice Name      | Address            | Postal Code | City   | Phone            | Website/Email                                   |
| ----------------- | ------------------ | ------------------ | ----------- | ------ | ---------------- | ----------------------------------------------- |
| Dr. Max Muster    | Hautzentrum Zürich | Bahnhofstrasse 123 | 8001        | Zürich | +41 44 123 45 67 | [www.hautzentrum.ch](http://www.hautzentrum.ch) |
| Dr. Anna Beispiel | Praxis Derm Basel  | Spitalgasse 45     | 4051        | Basel  | N/A              | [info@dermbasel.ch](mailto:info@dermbasel.ch)   |

5.**📌 Use Cases**

  Building medical contact databases

  Market research for dermatologists in Switzerland

  Easy integration into CRM systems  
👩‍💻 Author : Mariem L.
