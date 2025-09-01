# OneDoc Dermatologists Scraper 🩺

Python web scraper to collect dermatologists' data from the [OneDoc directory](https://www.onedoc.ch/de/hautarzt-dermatologe/stadte).

## Features
- Scrapes all cities listed under dermatologists
- Extracts:
  - Doctor Name
  - Practice Name
  - Address
  - Postal Code & City
  - Phone
  - Website / Email
  - Profile Link
- Multi-threaded scraping (faster execution)
- Intermediate Excel backups every 100 records
- Final delivery in clean `.xlsx` format

## Tech Stack
- Python 3
- Requests
- BeautifulSoup4
- Pandas
- OpenPyXL
- ThreadPoolExecutor

## Output Example
| Doctor Name | Practice Name | Address | Postal Code | City | Phone | Website | Email | Profile Link |
|-------------|---------------|---------|-------------|------|-------|---------|-------|--------------|
| Dr. John Doe | Hautzentrum Zürich | Bahnhofstrasse 12 | 8001 | Zürich | +41 44 123 45 67 | www.example.ch | info@example.ch | link... |

## Usage
```bash
pip install requests beautifulsoup4 pandas openpyxl
python scrape_onedoc.py
