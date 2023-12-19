# initialize book with attributes: name (str)
class Author:
    all = []

    def __init__(self, name):
        self.name = name
    
    # this method should return a list of related contracts / list comprehension
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
        # (need to go down to append this to Contract class)


    # should return list of related books using the Contract class as an intermediary
    def books(self):
        return [contract.book for contract in self.contracts()]

    # create and return new Contract object between author/specified book with specified date/royalties
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
        
    # return total amount of royalties author earned from all of their contracts
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

# initialize book with attributes: title (str)
class Book:
    all = []

    def __init__(self, title):
        self.title = title
    
    # returns a list of contracts
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    # book object should have authors attribute
    # returns a list of its authors
    def authors(self):
        return [contract.author for contract in self.contracts()]

# has properties: author, book, date (str), royalties (int)
class Contract:
    # keep track of all members using class variable
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        # add contract to list of all contracts
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.getter
    def author(self):
        return self._author

# need to raise exception for Author
    @author.setter
    def author(self, val):
        if isinstance(val, Author):
            self._author = val
        else:
            raise Exception

    @property
    def book(self):
        return self._book
    
    @book.getter
    def book(self):
        return self._book
# need to raise exception for Book
    @book.setter
    def book(self, val):
        if isinstance(val, Book):
            self._book = val
        else:
            raise Exception
    
    @property
    def date(self):
        return self._date
    
    @date.getter
    def date(self):
        return self._date
    
# need to raise exception for Date
    @date.setter
    def date(self, val):
        # in isinstance needs to be a str not _date!!
        # check if the val (value) is an instance of str (string)
        if isinstance(val, str):
            self._date = val
        else:
            raise Exception

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.getter
    def royalties(self):
        return self._royalties

# need to raise exception for royalties
    @royalties.setter
    def royalties(self, val):
        # in isinstance needs to be a int not royalties!!
        # check if the val (value) is an instance of int (integer)
        if isinstance(val, int):
            self._royalties = val
        else:
            raise Exception

# class method needs to return ALL contracts that have same date = date passed into the method
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]