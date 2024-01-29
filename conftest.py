import pytest
from main import BooksCollector
@pytest.fixture(scope="function")
def collector():
    collector = BooksCollector()
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
    collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
    return collector