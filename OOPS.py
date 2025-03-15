#class
# class Car():
#     name="BMW"
#     def engine_start(self):
#         print("Engine Starts")
#     def engine_off(x):
#         print("Engine is off now")
# Car().engine_start()

# class Student():
#     def __init__(self,name,age,marks):
#         self.stu_name=name
#         self.stu_age=age
#         self.stu_marks=marks
#     def print_marks(self):
#         print("Your marks is",self.stu_marks)

# x=Student("Esakki",25,450)
# y=Student("Vijay",24,375)
# x.print_marks()
# y.print_marks()

#Instance Method

# class Car():
#     name="BMW"
#     def engine_start(self):
#         print("Engine Starts")
#     def engine_off(x):
#         print("Engine is off now")

# o=Car()
# o1=Car()
# o2=Car()

# o.engine_start()
# o2.engine_off()

#Practice 

#1

# class Student():
#     def __init__(self):
#         self.stu_list=[]
#     def add(self):
#         i="Yes"
#         while i=="Yes":
#             name=input("Enter Name:")
#             age=int(input("Enter Age:"))
#             regno=input("Enter Register Number:")

#             details={"Name":name,"Age":age,"Register Number":regno}
#             self.stu_list.append(details)
#             print("Do you want to add another student's detail:")
#             i=input("Yes or No:")
    
# o=Student()
# o.add()
# print(o.stu_list)



#2

# class College:
#     def __init__(self):
#         self.bsc=[]
#     def add_info(self,info):
#         self.bsc.append(info)
#     def change_marks(self,name,marks):
#       for i in self.bsc:
#         if name==i.name:
#             i.change__marks(marks)

            

# class Students():
#     def __init__(self,name,age,mark):
#         self.name=name
#         self.age=age
#         self.mark=mark
#     def add(self):
#         i=1
#     def change__marks(self,marks):
#         self.mark=marks
# a=College()

# i="Yes"
# while i=="Yes":
            
            
#     name=input("Enter Name:")
#     age=int(input("Enter Age:"))
#     mark=input("Enter Marks:")

#     globals()[f"x{i}"]=Students(name,age,mark)
#     a.add_info(globals()[f"x{i}"])


#     print("Do you want to add another student's detail:")
#     i=input("Yes or No:")

# q=input("Do you want to change marks, Yes or No?   :")

# if q=="Yes":
#     n=input("Enter name:")
#     m=input("Enter the changed mark:")
#     a.change_marks(n,m)


# for j in a.bsc:
#     print(j.name,j.age,j.mark)




class Library:
    def __init__(self,books):
        self.books=books
        self.myBooks=[]
        
    def showBooks(self):
        print("Available Books are:")
        for i in self.books:
            print(i)
    def borrow_books(self,book_name):
        if book_name in cbooks:
            self.books.remove(book_name)
            self.myBooks.append(book_name)
        else:
            print("The book is not in the history of our library")

    def return_books(self,book_name):
        if book_name in cbooks:
            
            self.books.append(book_name)
            self.myBooks.remove(book_name)


class user(Library):
    def __init__(self,users,books):
        self.users=users
        super().__init__(books)

    def register(self):
        self.email=email
        self.password=password
        self.name=name
        self.age=age
        self.location=location
        email=input("Enter your email:")
        password=input("Enter your password:")
        name=input("Enter your name:")
        age=int(input("Enter your age:"))
        location=input("Enter your city:")
        user_info={"Name":name,"Age":age,"Location":location}
        users.append(user_info)
    def login(self):
        check=input("Enter your email:")
        check2=input("Enter password:")
        for i in users:
            if check == i["Email"] and check2 ==i["password"]:
                print("You're logged in")
                print(i["Name"])
                print(i["Age"])
                print(i["Location"])
                return True
        return False
            


j="Yes"
books=["Tamil","English","Maths","Science"]
cbooks=["Tamil","English","Maths","Science"]
users=[{"Email":"sakthi@gmail.com","password":"12345678","Name":"Sakthi","Age":19,"Location":"Chennai"},{"Email":"Jeevan@gmail.com","password":"12345678","Name":"Jeevan","Age":19,"Location":"Chennai"},{"Email":"Magesh@gmail.com","password":"12345678","Name":"Magesh","Age":20,"Location":"Chennai"}]

o=user(users,books)
t=1
while t==1:
    print('''
    1.Login
    2.Register
    ''')
    l=int(input("Option here:"))
    if l==1:
        w= o.login()
        if w == False:
            print("Login Failed")
        while j=="Yes" or j=="yes":

    
            print('''
            1.Show All Books
            2.Borrow Books
            3.Return Books
            4.Show My Books
            ''')
            i= int(input("Options here:"))

            if i==1:
                o.showBooks()
            elif i==2:
                name=input("Enter book name:")
                o.borrow_books(name)
            elif i==3:
                n=input("Enter book name:")
                o.return_books(n)
            else:
                print(o.myBooks)
        
            j=input("Want to continue? Yes or No :  ")


    else:   
        o.register()
