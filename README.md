# qa_python
pytest.ini нужен для корректного отображения кириллицы в отчетах с параметризацией

1. test_add_new_book_over_40_symbols 
добавляем книгу с тайтлом >40 симолов

2. test_add_new_book_0_symbols 
добавляем книгу с тайтлом 0 символов 

3. test_add_new_book_same_title 
добавляем книгу с одинаковым тайтлом два раза

4. test_set_book_genre 
устанавливаем жанр для книги 

5. test_set_book_genre_false_genre 
устанавливаем для книги жанр, которого нет в списке

6. test_get_books_genre 
получаем жанр для книги

7. test_get_books_with_specific_genre 
получаем книги определенного жанра

8. test_get_book_with_specific_genre_false_genre 
получаем книги с жанром, которого нет в списке

9. test_get_books_for_children 
получаем книги для детей из списка genre_age_rating

10. test_add_book_in_favorite_genre 
добавляем книгу в список избранного

11. test_add_book_in_favorite_genre_same_book_twice 
добавляем два раза книгу в список избранного

12. test_add_book_in_favorite_genre_not_in_genre_list 
добавляем в список избранного книгу, которой нет в списке добавленных книг

13. test_delete_book_from_favorites
удаляем книгу из списка избранного 

14. test_delete_book_from_favorites_book_not_exists
удаляем книгу из списка избранного, которой нет в списке добавленных книг
