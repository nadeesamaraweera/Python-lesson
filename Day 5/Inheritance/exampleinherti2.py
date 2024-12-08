# you taskimplement the following classes

# base class/parenet class = libraryItem
#      attributes: title(strinh),author(string),publication_year(integer)
#      methods :display_info = print the details of the items

#                           =  book 
#      inherit from liabrary items,additional attributes,gender(string),isbn(string)
#      overtite display_info
#      print the details include gender and isbn

#                          = magazine
#      inheeit the library_items
#      issue(string) = the issue number or date of the magazine
#      overtite display_info
#      print the details including the issue

# task :

# 1.create instance of each class(Book,Magazine) with appo valuea from their attributes.
# 2.call the display_info method for each inheritance  to test inheritence and method overriding


class LibraryItem:
     def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

     def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")


class Book(LibraryItem):
     def __init__(self, title, author, publication_year, genre, isbn):
        super().__init__(title, author, publication_year)
        self.genre = genre
        self.isbn = isbn

     def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}")
        print(f"ISBN: {self.isbn}")


class Magazine(LibraryItem):
     def __init__(self, title, author, publication_year, issue):
        super().__init__(title, author, publication_year)
        self.issue = issue

     def display_info(self):
        super().display_info()
        print(f"Issue: {self.issue}")


bookInstance = Book("p dial", "Sandul Rusara", 1925, "Kaluthara", "9780743273565")
magazineInstance = Magazine("National Drug Dealer", "Nishan", 2024, "December")

print("Book Details:")
bookInstance.display_info()
print("\nMagazine Details:")
magazineInstance.display_info()
