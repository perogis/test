class Flat:
    def __init__(self, link, price=None, title=None,
                 description=None, date=None, city=None,
                 street=None, area=None, images=None):
        self.link = link
        self.price = price
        self.title = title
        self.description = description
        self.date = date
        self.city = city
        self.street = street
        self.area = area
        self.images = images