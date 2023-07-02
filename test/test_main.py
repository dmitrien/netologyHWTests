import pytest
from main import tusckOne, tusckThree, tusckTwo
from yndexFolder import create_folder, show_folder, delete_folder
from unittest import TestCase


# ---------unittest---------------
class TestSame(TestCase):

    def test_First(self):
        result_funk = tusckOne()
        for number in result_funk:
            number = result_funk.pop(result_funk.index(number))
            self.assertNotIn(number, result_funk, f"Число {number} не уникально")

    def test_Second(self):
        name = "yandex"
        popular_company = tusckTwo()
        self.assertEqual(name, popular_company, f'Компания {popular_company} не самая популярная!')

    def test_creation_folder(self):
        path = "Тестовщина"
        create_folder(path)
        self.assertEqual(200, show_folder(path), f'Нет папки с названием "{path}"')
        delete_folder(path)

    def test_creation_folder_empty(self):
        path = " "
        create_folder(path)
        self.assertEqual(200, show_folder(path), f'Нет папки с названием "{path}"')
        delete_folder(path)

    def test_creation_fail_name(self):
        path = "Тестовщина"
        create_folder(path)
        fail_path = "Тест"
        self.assertEqual(404, show_folder(fail_path), f'Папки с названием "{fail_path}" присутствует')
        delete_folder(path)

    




#---------pytest---------------
@pytest.mark.xfail
@pytest.mark.parametrize(
"expected", [
        ("Россия"),
        ("Европа")
    ]
)
def test_Third(expected):
    cities = tusckThree()
    for city in cities:
        assert expected in list(city.values())[0], f'Город {list(city.values())[0][0]} не находится в {expected}'





