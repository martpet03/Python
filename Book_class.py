class Book:
    def __init__(self, book_name, book_code, book_price, book_year, book_author):
        self.book_name = book_name
        self.book_code = book_code
        self.book_price = book_price
        self.book_year = book_year
        self.book_author = book_author

    def __repr__(self):
        return f'{self.book_name} - {self.book_code} - {self.book_price}$ - {self.book_year} - {self.book_author}'


    #def __lt__(self, other):
        #return self.book_name > other.book_name

books = [
Book('1984', 34198442, 9.99, 1949, 'George Orwell'),
Book('Brave New World', 2346463, 12.99, 1932, 'Aldous Huxley'),
Book('A Hitchhiker\'s Guide to The Galaxy', 42954342, 12.99, 1965, 'Adam Douglas'),
Book('Foundation', 34561432, 10.99, 1931, 'Isacc Asimov'),
Book('Animal Farm', 3466342, 4.99, 1946, 'George Orwell')
]

def sort_name(book):
    for x in sorted(book, key = lambda x: x.book_name, reverse = True):
        print(x)

def author(book, auth):
    for x in book:
        if x.book_author == auth:
            print(x.book_name)

def search_book(book, cod):
    for x in book:
        if x.book_code == cod: 
            print(x.book_year)
            return
    print('The book is not found!')



print('')
sort_name(books)
print('')
author(books, 'George Orwell')
print('')
search_book(books, 34561432)
