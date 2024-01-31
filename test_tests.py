import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Объединил два теста в один через параметризацию
    @pytest.mark.parametrize('book', ['Удивительное путешествие Нильса Хольгерссона с дикими гусями по Швеции', ''])
    def test_add_new_book_over_40_symbols_or_0_symbols(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        assert collector.get_books_genre() == {}

    # def test_add_new_book_over_40_symbols(self):
    #     collector = BooksCollector()
    #     collector.add_new_book('Удивительное путешествие Нильса Хольгерссона с дикими гусями по Швеции')
    #     assert collector.get_books_genre() == {}
    #
    # def test_add_new_book_0_symbols(self):
    #     collector = BooksCollector()
    #     collector.add_new_book('')
    #     assert collector.get_books_genre() == {}

    def test_add_new_book_same_title(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    # Убрал использование фикстуры
    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.books_genre['Гордость и предубеждение и зомби'] == 'Ужасы'

    # Убрал параметризацию. На самом деле я ее добавил сюда, потому что не знал куда еще можно было бы впихнуть
    def test_set_book_genre_false_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Сказки')
        assert 'Сказки' not in collector.get_book_genre('Гордость и предубеждение и зомби')

    def test_get_books_genre(self, collector):
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_books_with_specific_genre(self, collector):
        assert collector.get_books_with_specific_genre('Комедии') == ['Что делать, если ваш кот хочет вас убить']

    def test_get_book_with_specific_genre_false_genre(self, collector):
        assert collector.get_books_with_specific_genre('Сказки') == []

    def test_get_books_for_children(self, collector):
        assert collector.get_books_for_children() == ['Что делать, если ваш кот хочет вас убить']

    def test_add_book_in_favorite_genre(self, collector):
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert 'Что делать, если ваш кот хочет вас убить' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorite_genre_same_book_twice(self, collector):
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorite_genre_not_in_genre_list(self, collector):
        collector.add_book_in_favorites('Гарри Поттер и философский камень')
        assert 'Гарри Поттер и философский камень' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_book_not_exists(self, collector):
        assert collector.delete_book_from_favorites('Гарри Поттер и философский камень') is None
