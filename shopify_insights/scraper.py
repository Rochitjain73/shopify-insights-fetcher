import re
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def extract_brand_name(url):
    return url.split("//")[-1].split(".")[0].capitalize()

def scrape_shopify_data(website_url):
    data = {}

    try:
        res = requests.get(urljoin(website_url, "/products.json"))
        if res.status_code == 200:
            data['product_catalog'] = res.json().get("products", [])
        else:
            data['product_catalog'] = []
    except:
        data['product_catalog'] = []

    try:
        home = requests.get(website_url)
        soup = BeautifulSoup(home.text, "html.parser")

        # Hero Products
        hero_links = soup.find_all("a", href=re.compile("/products/"))
        data['hero_products'] = list({a.text.strip() for a in hero_links if a.text.strip()})

        # Social Links
        social_links = []
        for tag in soup.find_all("a", href=True):
            href = tag['href']
            if any(s in href for s in ['instagram', 'facebook', 'twitter', 'tiktok']):
                social_links.append(href)
        data['social_links'] = list(set(social_links))

        # Contact Info
        text = soup.get_text()
        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
        phones = re.findall(r"\+?\d[\d\s\-()]{7,}", text)
        data['contact_details'] = {
            "emails": list(set(emails)),
            "phones": list(set(phones))
        }

        # Static pages
        static_pages = {
            "about": "about",
            "contact": "contact",
            "privacy_policy": "privacy",
            "return_policy": "return",
            "faq": "faq",
            "order_tracking": "track",
            "blog": "blog"
        }

        for key, keyword in static_pages.items():
            data[key] = ""
            for link in soup.find_all("a", href=True):
                if keyword in link['href'].lower():
                    try:
                        subpage = requests.get(urljoin(website_url, link['href']))
                        text = BeautifulSoup(subpage.text, "html.parser").get_text()
                        text = re.sub(r'\s{2,}', ' ', text)
                        data[key] = text.strip()[:1500]
                        break
                    except:
                        continue
    except Exception as e:
        data['error'] = str(e)

    return data