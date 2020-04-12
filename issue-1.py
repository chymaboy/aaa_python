import json


class Object:
    def __init__(self, mapping):
        for k, v in mapping.items():
            if isinstance(v, dict):
                self.__dict__[k] = Object(v)
            else:
                self.__dict__[k] = v


class ColorizeMixin:
    def __str__(self):
        return f'\033[1;{self.repr_color_code};48m {self.__repr__()}'


class Advert(ColorizeMixin):
    repr_color_code = 32  # green

    def __init__(self, mapping):
        self.price = 0
        self.__dict__.update(Object(mapping).__dict__)
        if 'title' not in self.__dict__.keys():
            raise ValueError("Title is required parameter")
        if self.price < 0:
            raise ValueError("Price must be >= 0")

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


if __name__ == "__main__":
    lesson_str = """{
        "title": "python",
        "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
        }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.location.address)
    print(lesson_ad.price)

    iphone_ad = Advert({'title': 'iPhone X', 'price': 100})
    print(iphone_ad)
