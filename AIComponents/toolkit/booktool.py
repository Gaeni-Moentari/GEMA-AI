from crewai.tools import BaseTool
import requests

class GBookTool(BaseTool):
    name: str = "GBook Tool"
    description: str = """search the GEMA Book API FOR available books in it's API
                        API using bahasa Indonesia
                        API sample {
    "status": 200,
    "data": [
        {
            "id": "008119a7-d4da-4126-a408-4bc1c9bd781b",
            "categories": [
                "PENGEMBANGAN WEB"
            ],
            "title": "DAILY LARAVEL PADEPOKAN - Dimas dan Rahma",
            "link": "https://gbook.gaeni.org/book/008119a7-d4da-4126-a408-4bc1c9bd781b",
            "desc": "<p>Buku ini merupakan buku yang dibuat dalam kegiatan belajar PADEPOKAN SEAMEO bersama menerapkan framework laravel sebagai pembuatan website.</p>",
            "author": "Dimas Bagus feat Rahma",
            "publishyear": "2024-01-12"
        },
        {
            "id": "02baa47d-43db-456e-9154-fbbf18ae97f5",
            "categories": [
                "SPW"
            ],
            "title": "BUKU DIGITAL SMKN 1 PROBOLINGGO",
            "link": "https://gbook.gaeni.org/book/02baa47d-43db-456e-9154-fbbf18ae97f5",
            "desc": "<p>-</p>",
            "author": "SMKN 1 PROBOLINGGO",
            "publishyear": "2023-11-24"
        },..."""

    def _run(self,query:str) -> str:
        """
        Search the API for available books 
        """
        API_URL = "https://gbook.gaeni.org/api-v1/book"
        try:
            # Mengambil data dari API
            response = requests.get(API_URL)
            response.raise_for_status()
            books_data = response.json()  # Konversi JSON ke Python dictionary
            books = books_data.get('data', [])  # Ambil bagian "data" dari JSON

            # Filter buku berdasarkan query
            results = []
            for book in books:
                title = book.get('title', '').lower()
                author = book.get('author', '').lower()
                categories = [category.lower() for category in book.get('categories', [])]
                
                # Jika query ada di title, author, atau categories
                if query in title or query in author or any(query in category for category in categories):
                    results.append({
                        "id": book.get('id'),
                        "title": book.get('title'),
                        "author": book.get('author'),
                        "categories": book.get('categories', []),
                        "link": book.get('link'),
                        "desc": book.get('desc'),
                        "publishyear": book.get('publishyear')
                    })
            return results
        except Exception as e:
            return "api error"