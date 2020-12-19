import unittest
from BookService import BookService


class TestBookService(unittest.TestCase):
    def setUp(self):
        self.service = (
            BookService()
        )  # Base_url could be changed for a Mock Server to avoid using external services in tests

    def test_validISBN_returns_correctly(self):
        valid_isbn = 9780140328721
        book = self.service.book_by_isbn(valid_isbn)
        self.assertEqual(
            book["title"], "Fantastic Mr. Fox", "Title should be Fantastic Mr. Fox"
        )

    def test_invalidISBN_gives_error(self):
        with self.assertRaises(Exception):
            invalid_isbn = 123
            self.service.book_by_isbn(invalid_isbn)

    def test_valid_work_id_returns_correctly(self):
        valid_work_id = "OL1678673W"
        work = self.service.book_by_isbn(valid_work_id)
        self.assertEqual(work["title"], "La mayor", "Title should be La mayor")

    def test_invalid_work_id_gives_error(self):
        with self.assertRaises(Exception):
            invalid_work_id = "AA123"
            self.service.book_by_isbn(invalid_work_id)


if __name__ == "__main__":
    unittest.main()
