import requests


class BookService:
    def __init__(self, base_url="https://openlibrary.org"):
        self.base_url = base_url

    def book_by_isbn(self, isbn):
        response = requests.get(f"{self.base_url}/isbn/{isbn}.json")
        if response:
            return response.json()
        else:
            raise Exception("Book Not Found")

    def work_by_id(self, work_id):
        response = requests.get(f"{self.base_url}/works/{work_id}.json")
        if response:
            return response.json()
        else:
            raise Exception("Work Not Found")
