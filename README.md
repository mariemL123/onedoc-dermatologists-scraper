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
