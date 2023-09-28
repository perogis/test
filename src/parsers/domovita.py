import requests
from bs4 import BeautifulSoup
import re

from base_parser import ParserStandart
from src.data import Flat


class DomovitaParser(ParserStandart):
    """It's class-parser for parse data"""

    def get_parser_name(self):
        return "domovita"

    def get_all_last_flats_links(self, page_from=2, page_to=5):
        """function for get and filter flat links"""

        flat_links = []
        while page_from < page_to:
            resp = requests.get(f"https://domovita.by/minsk/flats/sale?page={page_from}")
            html = BeautifulSoup(resp.content, "html.parser")
            for a in html.find_all('a', href=True, class_="mb-5 title title--listing"):
                flat_links.append(a['href'])
                page_from += 1
        filter_links = list(filter(lambda el: 'flats' in el, flat_links))
        return filter_links

    def enrich_links(self, links):
        """function for parse all links and get elements"""

        flats = []
        for counter, link in enumerate(links):
            resp = requests.get(link)
            html = BeautifulSoup(resp.content, 'html.parser')

            title = html.find('h1', class_='').text.strip()
            price = html.find(attrs={"data-js": "show-tooltip"}).text
            if len(price) > 15:
                price = (re.sub('[^0-9]', '', price))
            else:
                price = 0
            description = html.find('div', class_="seo-text_content-h")
            if description is not None:
                description = description.text.strip()
            else:
                description = None
            date = html.find('span', class_="publication-info__item publication-info__publication-date").text.strip()
            city = html.find(attrs={"id": "city"}).text.strip()
            div_steet = html.find_all("div", class_="object-info__parametr")
            if len(div_steet) >= 5:
                street = div_steet[6].text.strip()
            else:
                street = None
            div_area = html.find_all("div", class_="object-info__parametr")
            if len(div_area) >= 5:
                area = div_area[7].text.strip()
            else:
                area = None

            flats.append(Flat(
                link=link,
                title=title,
                price=price,
                description=description,
                date=date,
                city=city,
                street=street,
                area=area
            ))
            print()
            print(f"Обработано {counter} из {len(links)}")
        return flats


DomovitaParser().update_with_last_flats()