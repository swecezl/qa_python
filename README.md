## Проект по тестированию методов класса BooksCollector

    class BooksCollector:
        def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        self.genre_age_rating = ['Ужасы', 'Детективы']

### Реализованные проверки: 

1. **Метод `add_new_book` добавляет новую книгу**

        def add_new_book(self, name):
            if not self.books_genre.get(name) and 0 < len(name) < 41:
                self.books_genre[name] = ''

Тест `test_add_new_book_add_two_books` проверяет возможность добавления книг  
Тест `test_add_new_book_over_40_symbols_or_0_symbols` проверяет с помощью параметризации условие по невозможности добавления книг, превышающих в названии 40 символов или содержащих в названии 0 символов
Тест `test_add_new_book_same_title` проверяет невозможность добавления двух книг с одинаковым названием

2. **Метод `set_book_genre` устанавливает книге жанр**

        def set_book_genre(self, name, genre):
            if name in self.books_genre and genre in self.genre:
                self.books_genre[name] = genre

Тест `test_set_book_genre` проверяет возможность установить для добавленной книги жанр  
Тест `test_set_book_genre_false_genre` проверяет невозможность установить для добавленной книги жанр, который отсутствует в списке `self.genre`  

3. **Метод `get_books_genre` выводит словарь books_genre** 

        def get_book_genre(self, name):
            return self.books_genre.get(name)

Тест `test_get_books_genre` проверяет получение жанра по названию книги 


4. **Метод `get_books_with_specific_genre` выводит список книг с определённым жанром**

        def get_books_with_specific_genre(self, genre):
            books_with_specific_genre = []
            if self.books_genre and genre in self.genre:
                for name, book_genre in self.books_genre.items():
                    if book_genre == genre:
                        books_with_specific_genre.append(name)
            return books_with_specific_genre

Тест `test_get_books_with_specific_genre` проверяет получение списка книг определенного жанра  
Тест `test_get_book_with_specific_genre_false_genre` проверяет невозможность получения списка книг по жанру, который отсутствует в списке `self.genre`

5. **Метод `get_books_for_children` возвращает книги, подходящие детям**

        def get_books_for_children(self):
            books_for_children = []
                for name, genre in self.books_genre.items():
                    if genre not in self.genre_age_rating and genre in self.genre:
                    books_for_children.append(name)
                return books_for_children

Тест `test_get_books_for_children` проверяет получение книг для детей, жанр которых входит в список `self.genre_age_rating`

6. **Метод `add_book_in_favorites` добавляет книгу в избранное**

        def add_book_in_favorites(self, name):
            if name in self.books_genre:
                if name not in self.favorites:
                    self.favorites.append(name)
Тест `test_add_book_in_favorite_genre` проверяет добавление книги в избранное  
Тест `test_add_book_in_favorite_genre_same_book_twice` проверяет невозможность добавление одной и той же книги в избранное  
Тест `test_add_book_in_favorite_genre_not_in_genre_list` проверяет невозможность добавление в избранное книги, которой нет в словаре `self.books_genre`  

7. **Метод `delete_book_from_favorites` удаляет книгу из избранного**

        def delete_book_from_favorites(self, name):
            if name in self.favorites:
                self.favorites.remove(name)
        
Тест `test_delete_book_from_favorites` проверяет удаление книги из избранного  
Тест `test_delete_book_from_favorites_book_not_exists` проверяем невозможность удаление книги, котороый нет в списке избранного

***

### Запустить тесты 
```bash
pytest -v test_tests.py
```
### Оценка покрытия 
```bash 
pytest --cov=main
```
***  

### Примечание 
pytest.ini нужен для корректного отображения кириллицы в отчетах с параметризацией
