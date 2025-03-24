
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        bl = BookLover("Bob", "bob@gmail.com", "Fantasy")
        bl.add_book("Eragon", 5)
        self.assertTrue("Eragon" in bl.book_list['book_name'].values)
    
    def test_2_add_book(self):
        bl = BookLover("Bob", "bob@gmail.com", "Fantasy")
        bl.add_book("Eragon", 5)
        bl.add_book("Eragon", 5)
        self.assertEqual(len(bl.book_list[bl.book_list['book_name'] == "Eragon"]), 1)
    
    def test_3_has_read(self):
        bl = BookLover("Bob", "bob@gmail.com", "Fantasy")
        bl.add_book("Eldest", 4)
        self.assertTrue(bl.has_read("Eldest"))
    
    def test_4_has_read(self):
        bl = BookLover("Bob", "bob@gmail.com", "Fantasy")
        self.assertFalse(bl.has_read("Inheritence"))
    
    def test_5_num_books_read(self):
        bl = BookLover("Bob", "bob@gmail.com", "Fantasy")
        bl.add_book("Eragon", 5)
        bl.add_book("Eldest", 4)
        bl.add_book("Brisingr", 2)
        self.assertEqual(bl.num_books_read(), 3)
    
    def test_6_fav_books(self):
        bl = BookLover("Bob", "bob@gmail.com", "Fantasy")
        bl.add_book("Eragon", 5)
        bl.add_book("Eldest", 2)
        bl.add_book("Brisingr", 4)
        favs = bl.fav_books()
        self.assertTrue(all(favs['book_rating'] > 3))

if __name__ == '__main__':
    
    unittest.main(verbosity=3)
