import requests
import os
from datetime import datetime, timedelta

DATA_DIR = "../data/raw"

def download_oc_data(date, product="MODISA_L3m_CHL"):
    base_url = "https://oceandata.sci.gsfc.nasa.gov/cgi/getfile"
    filename = f"A{date.strftime('%Y%j')}.L3m_DAY_CHL_chlor_a_4km.nc"
    url = f"{base_url}/{filename}"
    
    response = requests.get(url)
    if response.status_code == 200:
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(os.path.join(DATA_DIR, filename), 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {filename}")

if __name__ == "__main__":
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2020, 12, 31)
    
    current_date = start_date
    while current_date <= end_date:
        download_oc_data(current_date)
        current_date += timedelta(days=1)