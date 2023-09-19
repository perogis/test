import requests
from bs4 import BeautifulSoup


class DomovitaParser:
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
        return flat_links