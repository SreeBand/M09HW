# Student Info

# Name:  Sree Prabhav Bandakavi
# Net UD: kqy9hc
# URL of this file in GitHub: https://github.com/SreeBand/DS5100-kqy9hc/blob/main/lessons/M08/hw08.pdf


import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame(columns=['book_name', 'book_rating'])
        
    def add_book(self, book_name, book_rating):
        if book_name not in self.book_list['book_name'].values:
            new_book = pd.DataFrame({'book_name': [book_name],
                                     'book_rating': [book_rating]
                                    })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        else:
            print(f"'{book_name}' is already in the book list.")

    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].values

    def num_books_read(self):
        return self.num_books

    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]