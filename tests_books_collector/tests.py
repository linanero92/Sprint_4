import pytest

class TestBooksCollector:

    @pytest.mark.parametrize('name',
                             ['The Little Prince', 'The Lord of The Rings']
                             )
    def test_add_two_new_books_in_dict_is_added(self, books_collector, name):
        books_collector.add_new_book(name)
        expected_book_dict = books_collector.books_genre.keys()
        assert name in expected_book_dict

    @pytest.mark.parametrize('name, genre',
                             [
                                 ['The Lord of The Rings', 'Фантастика'],
                                 ['The Little Prince', 'Мультфильмы']
                             ])
    def test_set_book_genre_in_dict_is_added(self, books_collector, name, genre):
        books_collector.add_new_book(name)
        books_collector.set_book_genre(name, genre)
        assert genre in books_collector.books_genre.values()

    def test_add_book_in_favorites_in_list_is_added(self, books_collector):
        name = 'The Lord of The Rings'
        books_collector.add_new_book(name)
        books_collector.add_book_in_favorites(name)
        favorite_books = books_collector.get_list_of_favorites_books()
        assert name in favorite_books

    def test_delete_book_from_favorites_book_is_deleted(self, books_collector):
        name = 'The Little Prince'
        books_collector.add_new_book(name)
        books_collector.add_book_in_favorites(name)
        books_collector.delete_book_from_favorites(name)
        assert name not in books_collector.favorites

    def test_get_book_genre_dict_is_received(self, books_collector):
        books_collector.add_new_book('The Little Prince')
        books_collector.set_book_genre('The Little Prince', 'Мультфильмы')
        assert books_collector.get_book_genre('The Little Prince') == 'Мультфильмы'

    def test_get_book_genre_no_genre_added(self, books_collector):
        books_collector.add_new_book('The Lord of The Rings')
        assert books_collector.get_book_genre('The Lord of The Rings') == ''

    @pytest.mark.parametrize('book_name, book_genre',
                             [
                                 ['Кэрри', 'Ужасы'],
                                 ['Дракула', 'Фантастика']
                             ])
    def test_get_books_with_specific_genre_books_are_received(self, books_collector, book_name, book_genre):
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, book_genre)
        assert books_collector.get_books_with_specific_genre(book_genre) == [book_name]

    @pytest.mark.parametrize('book_name, book_genre',
                             [
                                 ['Английский для попугаев', 'Комедии'],
                                 ['Русалочка', 'Мультфильмы'],
                                 ['Машина времени', 'Фантастика']
                             ])
    def test_get_books_for_children_book_is_received(self, books_collector, book_name, book_genre):
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, book_genre)
        assert books_collector.get_books_for_children() == [book_name]

    @pytest.mark.parametrize('book_name, book_genre',
                             [
                                 ['Дракула', 'Ужасы'],
                                 ['Концы в воду', 'Детектив']
                             ])
    def test_get_books_for_children_book_is_not_received(self, books_collector, book_name, book_genre):
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, book_genre)
        assert books_collector.get_books_for_children() != [book_name]

    @pytest.mark.parametrize('book_name, book_genre',
                             [
                                 ['Английский для попугаев', 'Комедии'],
                                 ['Русалочка', 'Мультфильмы'],
                                 ['Машина времени', 'Фантастика'],
                                 ['The Little Prince', 'Мультфильмы'],
                                 ['Кэрри', 'Ужасы'],
                                 ['Странные игры', 'Детективы']
                             ])
    def test_get_books_genre_books_genre_is_received(self, books_collector, book_name, book_genre):
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, book_genre)
        assert books_collector.get_books_genre() == {book_name: book_genre}
