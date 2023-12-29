import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import quote

sharepoint_url = 'https://www.mylocalsharepoint.local/cve_data.xlsx'
encoded_url = quote(sharepoint_url) #quote(sharepoint_url) to 'quote' special reserved characters
urls = ['https://www.thehackernews.com',
        'https://www.bleepingcomputer.com',
        'https://www.packetstormsecurity.com/',
        'https://www.cisa.gov/known-exploited-vulnerabilities-catalog',
        'https://www.getinfosec.news/#/list/popular/0']
data = [] 

for url in urls:
    try:
        page = requests.get(url)
        page.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        continue

    soup = BeautifulSoup(page.content, 'html.parser')

    for link in soup.find_all('a'):
        href = link.get('href')
        if href and 'CVE' in href:
            cve_page = requests.get(href)
            cve_soup = BeautifulSoup(cve_page.content, 'html.parser')
            
            score = cve_soup.find(text=lambda text: text and 'CVSS Score:' in text)
            score = float(score.split(':')[1])

            if score >= 7.8:
                vendor = cve_soup.find(text=lambda text: text and 'Vendor:' in text)
                vendor = vendor.split(':')[1].strip()

                desc = cve_soup.find(text=lambda text: text and 'Description:' in text)
                desc = desc.split(':')[1].strip()
                
                data.append({'CVE Score': score, 
                             'Vendor': vendor,
                             'Short Description': desc,
                             'Link': href})

df = pd.DataFrame(data)
df.drop_duplicates(inplace=True)

try:
    df.to_excel(encoded_url, index=False)
except Exception as e:
    print(f"Failed to write Excel file: {e}")