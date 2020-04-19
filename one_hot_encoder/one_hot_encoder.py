from typing import List, Tuple
import unittest
import pytest


class TestTF(unittest.TestCase):
    def test_empty(self):
        actual = fit_transform([])
        expected = []
        self.assertEqual(actual, expected)

    def test_len0(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_single(self):
        actual = fit_transform(['A', 'A', 'A'])
        expected = [('A', [1]), ('A', [1]), ('A', [1])]
        self.assertEqual(actual, expected)

    def test_type(self):
        actual = fit_transform(['a', 'b', 'c'])
        self.assertIsInstance(actual, List)


def test_empty():
    assert fit_transform([]) == []


def test_exception():
    with pytest.raises(TypeError):
        fit_transform()


def test_type():
    assert type(fit_transform('pass')) == list


def test_similarity():
    x = [1, 2, 3]
    y = [4, 5, 6]
    assert fit_transform(x)[0][1] == fit_transform(y)[0][1]


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


if __name__ == '__main__':
    pass
