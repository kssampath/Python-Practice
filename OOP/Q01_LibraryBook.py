class Book:
    def __init__(self,title,author,is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    def borrow(self):
        if self.is_borrowed:
            print(f"Sorry, '{self.title}' is already borrowed.")
        else:
            self.is_borrowed = True
            print(f"You have borrowed '{self.title}'.")
        
    def return_book(self):
        if not self.is_borrowed:
            print(f"'{self.title}' was not borrowed.")
        else:
            self.is_borrowed = False
            print(f"You have returned '{self.title}'.")
    def __str__(self):
        return (
    f"Title: {self.title}\n"
    f"Author: {self.author}\n"
    f"Borrowed: {self.is_borrowed}" )

if __name__ == "__main__":
    b1 = Book("Atomic Habits", "James Clear")
    print(f"Title: {b1.title}, Author: {b1.author}, Is Borrowed: {b1.is_borrowed}")
    b1.borrow()
    print(b1)
    b1.return_book()
    print(b1)
