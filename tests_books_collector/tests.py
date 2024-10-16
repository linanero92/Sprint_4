import pytest

from main import BooksCollector
from conftests import *


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

    # paramerize #fixture в conftest, #data files
    @pytest.mark.parametrize('name',
                             ['The Little Prince', 'The Lord of The Rings']
                             )
    def test_add_two_new_books_in_dict_added(self, books_collector, name):
        books_collector.add_new_book(name)
        expected_book_dict = books_collector.books_genre.keys()
        assert name in expected_book_dict


    @pytest.mark.parametrize('name, genre',
                             [
                                 ['The Lord of The Rings', 'Фантастика'],
                                 ['The Little Prince', 'Мультфильмы']
                             ])
    def test_set_book_genre_in_dict_added(self, books_collector, name, genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert genre in books_collector.books_genre.values()

    def test_add_book_in_favorites_in_list_added(self, books_collector):
        name = 'The Lord of The Rings'
        books_collector.add_new_book(name)
        books_collector.add_book_in_favorites(name)
        favorite_books = books_collector.get_list_of_favorites_books()
        assert name in favorite_books


    def test_get_list_of_favorites_books_list_received(self, books_collector):
        name = 'The Lord of The Rings'
        books_collector.add_new_book(name)
        books_collector.add_book_in_favorites(name)
        assert name in books_collector.get_list_of_favorites_books()

    def test_get_book_genre_dict_received(self, books_collector):
        books_collector.add_new_book('The Little Prince')
        books_collector.set_book_genre('The Little Prince', 'Мультфильмы')
        assert books_collector.get_book_genre('The Little Prince') == 'Мультфильмы'


    def test_get_book_genre_no_genre_added(self, books_collector):
        books_collector.add_new_book('The Lord of The Rings')
        assert books_collector.get_book_genre('The Lord of The Rings') == ''