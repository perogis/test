class Flat:
    def __init__(self, link, price=None, title=None,
                 description=None, date=None, city=None,
                 images=None, email=None):
        self.link = link
        self.price = price
        self.title = title
        self.description = description
        self.date = date
        self.city = city
        self.images = images
        self.emeil = email