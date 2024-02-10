class Book:
    def __init__(self,name,subject,price):
        self.name=name
        self.subject=subject
        self.price=price
        
    def addBook(self):
        print("name: "+self.name)
        print("subject: "+self.subject)
        print("price: "+str(self.price))
        print("\n")

book1=Book("consice physics","physics",80)
book2=Book("consice biology","biology",90)
book3=Book("conscice chemistry","chemistry",100)

book1.addBook()
book2.addBook()
book3.addBook()