
import uuid
# using uuid to represent the ids of members, librarians and books


# LMS singleton class having all the core DB to store info of members, librarians & the books
class LMS:
    _instance = None

    def __new__(cls,*args,**kwargs):
        if cls._instance is None:
            cls._instance = super(LMS,cls).__new__(cls,*args,**kwargs)
        return cls._instance
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        

# Class book having the info of books
class Book:
    def __init__(self,bId,title,author,category,rackNumber):
        self.bId = bId
        self.title = title
        self.author = author
        self.category = category
        self.rackNumber = rackNumber

# Singleton class BMS that storing all the functions related to books
class BookManagementSystem:
    _instance = None

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.books_data = {}  # map uid -> bookCount
        self.title_data = {}  # map title -> uid
        self.author_data = {} # map authorName -> uid
        self.category_data = {} # map category_data -> uid
        self.rack_data = {}    # map uid -> rackNumber
        self.members_books = {}  # tells uid -> no of books alloted
        self.reserved_books = {} 


    def __new__(cls,*args,**kwargs):
        if cls._instance is None:
            cls._instance = super(BookManagementSystem,cls).__new__(cls,*args,**kwargs)
        return cls._instance
    

    # method to add book 
    def addBook(self,bookObj,bmsObj):
        id = bookObj.bId
        bmsObj.books_data[id] = bookObj.title
            

        # associate the corresponding key to the uid
        bmsObj.title_data[bookObj.title] = bookObj.bId
        bmsObj.author_data[bookObj.author] = bookObj.bId
        bmsObj.category_data[bookObj.category] = bookObj.bId
        bmsObj.rack_data[bookObj.bId] = bookObj.rackNumber

        # while adding book, check if it is in the reserved dict, if yes remove it (set value as 0)
        if id in bmsObj.reserved_books:
            bmsObj.reserved_books[id] = 0  

        print(f"Book {bookObj.title} is successfully added !")

    # method to remove book
    def removeBook(self,bookObj,bmsObj):
        id = bookObj.bId
        bmsObj.booksData.remove(id)
        bmsObj.author_data.remove(bookObj.author)
        bmsObj.title_data.remove(bookObj.title)
        bmsObj.category_data.remove(bookObj.category)
        bmsObj.rack_data.remove(id)

        print(f"Book {bookObj.title} is successfully deleted !")

    # method to search the book
    def searchBook(self,bmsObj,searchBy,query):
        if searchBy == 1:
            # search by title
            if query in bmsObj.title_data:
                print(f"Book {query} exists !")
            else:
                print(f"Book {query} doesn't exists !")
        
        elif searchBy == 2:
            # search by author
            if query in bmsObj.author_data:
                print(f"Book with author {query} exists !")
            else:
                print(f"Book with author {query} doesn't exists !")
        
        elif searchBy == 3:
            # search by category
            if query in bmsObj.category_data:
                print(f"Book with category {query} exists !")
            else:
                print(f"Book with category {query} doesn't exists !")
        
    # method to allot the books
    def allotBook(self,bmsObj,bookObj,memObj):
        id = memObj.mId
        d = bmsObj.members_books
        maxLimit = memObj.maxBooksAllowed
        print(f"Book {bookObj.title} is successfully alloted to {memObj.name}")
        
            # print("Can't allocate more books, Max books are alloted ")
    
    # method to return the book
    def returnBook(self,bmsObj,bookObj,memObj):
        id = memObj.mId
        d = bmsObj.members_books

        print(f"Book {bookObj.title} is successfully removed from {memObj.name}'s account")
    

    # method to reserver the book
    def reserveBook(self,id,bmsObj):
        if id in bmsObj.books_data:
            print("Book already exists in the library")
        else:
            print(f"Your book with the id {id} is reserved successfully !")
            bmsObj.reserved_books[id] = 1

    # method to show all the books
    def showAllBooks(self,bmsObj):
        for keys,values in bmsObj.books_data.items():
            print(f"Book id : {keys}, title : {values}")



# Class user 
class User:
    def __init__(self,name,age,mobileNo):
        self.name = name
        self.age = age
        self.mobileNo = mobileNo
  
# Class member inheriting User class
class Member(User):
    def __init__(self,mId,name,age,mobileNo,maxBookAllowed, maxDaysAllowed):
        super().__init__(name,age,mobileNo)
        self.mId = mId
        self.maxBooksAllowed = maxBookAllowed
        self.maxDaysAllowed = maxDaysAllowed
    
# Class Librarian inheriting User class
class Librarian(User):
    def __init__(self,lId,name,age,mobileNo,):
        super().__init__(name,age,mobileNo)
        self.lId = lId


# Class system to represent a notification system
class System:
    # print list of all overdue books, when reserved book is avaialable
    def isAvailable(self,id,lsmObj):
        if id in lsmObj.reserved_books and lsmObj.reserved_books[id] == 0:
            print("The book is available in the library !")
        else:
            print(f"Sorry, The book with {id} is not available !")


#  Class UMS handling all the user related functions
class UserManagementSystem:
    _instance = None

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.members_data = {}  # tells memberid -> name
        self.librarians_data = {} # tells librarianId -> name


    def __new__(cls,*args,**kwargs):
        if cls._instance is None:
            cls._instance = super(UserManagementSystem,cls).__new__(cls,*args,**kwargs)
        return cls._instance
    
    # method to add librarian
    def addLibrarian(self,libObj,umsObj):
        id = libObj.lId
        umsObj.librarian_data[id] = libObj.name
        print(f"Librarian {libObj.name} is successfully added !")
    
    # method to remove librarian
    def removeLibrarian(self,libObj,lmsObj):
        id = libObj.lId
        lmsObj.librarian_data.remove(id)
        print(f"Librarian {libObj.name} is successfully removed !")


    # method to add member
    def addMember(self,memberObj,umsObj):
        id = memberObj.mId
        if id not in umsObj.members_data:
            umsObj.members_data[id] = memberObj.name
        print(f"Member {memberObj.name} is successfully added !")


    # method to remove member
    def removeMember(self,memberObj,umsObj):
        id = memberObj.mId
        umsObj.member_data.remove(id)
        print(f"Member {memberObj.name} is successfully removed !")


    # method to show all the users
    def showAllMembers(self,umsObj):
        for keys,values in umsObj.members_data.items():
            print(f"Member id : {keys}, Name : {values}")
def getID():
    x = str(uuid.uuid4().int)
    return x[:2]


def main():
    lms = LMS()

    m1 = Member(getID(),"prasanna",22,8920481981,5,10)
    m2 = Member(getID(),"prasoon",23,1245345435,5,10)
    m3 = Member(getID(),"prakhar",20,12312351435,5,10)
    m4 = Member(getID(),"pragyan",15,5678658943,5,10)
    m5 = Member(getID(),"parth",24,234556756,5,10)
    ums = UserManagementSystem()
    
    print("------------------------------------------------------------------------------------")


    ums.addMember(m1,ums)
    ums.addMember(m2,ums)
    ums.addMember(m3,ums)
    ums.addMember(m4,ums)
    ums.addMember(m5,ums)

    print("------------------------------------------------------------------------------------")

    print(ums.showAllMembers(ums))


    print("------------------------------------------------------------------------------------")


    bms = BookManagementSystem()

    b1 = Book(getID(),'To Kill a Mockingbird','Harper Lee', 'Fiction', 1 )
    b2 = Book(getID(),'1984','George Orwell', 'Dystopian', 1)

    b3 = Book(getID(),'Pride and Prejudice','Jane Austen','Romance',2)
    b4 = Book(getID(),'The Great Gatsby','F. Scott Fitzgerald','Fiction',3)
    b5 = Book(getID(),'The Catcher in the Rye','J.D. Salinger','Fiction',3)

    bms.addBook(b1,bms)
    bms.addBook(b2,bms)
    bms.addBook(b3,bms)
    bms.addBook(b4,bms)
    bms.addBook(b5,bms)

    print("------------------------------------------------------------------------------------")

    print(bms.showAllBooks(bms))

    bms.searchBook(bms,1,'To Kill a Mockingbird')
    bms.searchBook(bms,2,'Jane Austen')
    bms.searchBook(bms,3,'Dystopian')

    bms.allotBook(bms,b1,m1)
    bms.returnBook(bms,b1,m1)
    





    # l = lms.members_data
    # print(l)

    # for keys,values in l.items():
    #     print(keys)
    #     print(values)
    
    # l1 = Librarian(uuid.uuid4(),"prasoon",25,9810054538)
    



    
if __name__ == "__main__":
    main()
