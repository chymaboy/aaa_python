import json


class Object:
    def __init__(self, mapping):
        for k, v in mapping.items():
            if isinstance(v, dict):
                self.__dict__[k] = Object(v)
            else:
                self.__dict__[k] = v


class Advert:
    def __init__(self, mapping):
        self.price = 0
        self.__dict__.update(Object(mapping).__dict__)
        if 'title' not in self.__dict__.keys():
            raise ValueError("Title is required parameter")
        if self.price < 0:
            raise ValueError("Price must be >= 0")


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
