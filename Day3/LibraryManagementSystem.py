class Book:
    def __init__(self, book_id, book_name, book_author):
        self.book_id = book_id
        self.book_name = book_name
        self.book_author = book_author
        self.available = True
    
    def checkout(self):
        self.available = False
    
    def return_book(self):
        self.available = True

    def display(self):
        if self.available:
            status = "Available"
        else:
            status = "Not Available"

        print("Book Name: " + self.book_name + "\nBook Author: " + self.book_author + "\nStatus: " + status)


class Magazine:
    def __init__(self, magazine_id, magazine_name, magazine_date, magazine_author):
        self.magazine_id = magazine_id
        self.magazine_name = magazine_name
        self.magazine_date = magazine_date
        self.magazine_author = magazine_author
        self.available = True
    
    def checkout(self):
        self.available = False
    
    def return_magazine(self):
        self.available = True
    
    def display(self):
        if self.available:
            status = "Available"
        else:
            status = "Not Available"        
        
        print("Magazine Name: " + self.magazine_name + "\nMagazine Date: " + self.magazine_date + "\nMagazine Author: " + self.magazine_author + "\nStatus: " + status)


class DVD:
    def __init__(self, dvd_id, dvd_name, dvd_size):
        self.dvd_id = dvd_id
        self.dvd_name = dvd_name
        self.dvd_size = dvd_size
        self.available = True
    
    def checkout(self):
        self.available = False
    
    def return_dvd(self):
        self.available = True
    
    def display(self):
        if self.available:
            status = "Available"
        else:
            status = "Not Available"

        print("DVD Name: " + self.dvd_name + "\nDVD Size: " + self.dvd_size + "\nStatus: " + status)


library_items = [
    Book(1, "Year2026", "James"),
    Magazine(2, "Resolution", "Jan 2026", "James"),
    DVD(3, "Dude", "4.7GB")
]


for x in library_items:
    x.display()
    print()


# library_items[0].checkout()
library_items[2].checkout()

print("After Checkout:\n")

for x in library_items:
    x.display()
    print()
