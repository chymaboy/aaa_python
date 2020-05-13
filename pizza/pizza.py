import click
from typing import Tuple
from random import randint


class Pizza:
    size: str = NotImplemented
    ingredients: Tuple[str, ...] = NotImplemented

    def __init__(self, size):
        self.size = size

    def __eq__(self, other):
        return self.size == other.size

    def dict(self):
        return self.ingredients


class Margherita(Pizza):
    name = 'Margherita'
    ingredients = ('tomato sauce', 'mozzarella', 'tomatoes')


class Pepperoni(Pizza):
    name = 'Pepperoni'
    ingredients = ('tomato sauce', 'mozzarella', 'pepperoni')


class Hawaiian(Pizza):
    name = 'Hawaiian'
    ingredients = ('tomato sauce', 'mozzarella', 'chicken', 'pineapples')


# def log(func: callable):
#     f_name = func.__name__
#
#     def inner(*args, **kwargs):
#         res = func(*args, **kwargs)
#         print(f'{f_name} completed for {randint(10, 99)}c')
#         return res
#     return inner


def log(string):
    def outer(func: callable):
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            print(string.format(randint(10, 99)))
            return res
        return inner
    return outer


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
@click.argument('size', nargs=1)
def bake(pizza: str, size: str, delivery: bool = False):
    return raw_bake(pizza, size, delivery)


def print_status(state, order):
    print(f'{state} {order.name} размера {order.size} за {randint(10, 100)}с!')


@log('Доставили за {}с!')
def bake_pizza(pizza: str, size: str, delivery: bool = False):
    return raw_bake(pizza, size, delivery)


def raw_bake(pizza: str, size: str, delivery: bool = False):
    pizzas = {'margherita': Margherita(size),
              'pepperoni': Pepperoni(size),
              'hawaiian': Hawaiian(size)}
    if pizza in pizzas.keys():
        order = pizzas[pizza]
        print_status('Приготовили', order)
        if delivery:
            print_status('Доставили', order)
    else:
        print('We dont have such pizza')


@cli.command()
def menu():
    print('Наши пиццы!')
    m = Margherita('x')
    p = Pepperoni('x')
    h = Hawaiian('x')
    for pizza in (m, p, h):
        print(pizza.name, ':', ', '.join(pizza.ingredients))


if __name__ == '__main__':
    # cli()
    bake_pizza('pepperoni', 'X')
