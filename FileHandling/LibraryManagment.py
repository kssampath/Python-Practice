class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
class Library:
    def __init__(self,books):
        self.books = books
    
    def add_book(self, book):
        self.books.append(book)
    
    def list_books(self):
        for book in self.books:
            print(f"Title: {book.title}\n")
    def find_book_by_title(self,title):
        return next((book for book in self.books if book.title == title), None)

if __name__ == "__main__":
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
    
    library = Library([book1, book2])
    #HAS A COMPOSITION RELATIONSHIP WITH BOOK CLASS
    library.list_books()
    
    found_book = library.find_book_by_title("The Great Gatsby")
    if found_book:
        print(f"Found: {found_book.title} by {found_book.author}")
    else:
        print("Book not found.")