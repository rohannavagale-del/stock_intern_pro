# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     return fact(n-1) *n

# print(fact(4))

# def cal(n):
#     if(n==0):
#         return 0

#     return cal(n-1)+n

# print(cal(5))

# def print_list(list , idx=0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list , idx+1)
# fruits = ["apple", "litchi", "banana", "watermeloon"]
# print_list(fruits)

# def sum(a , b):
#     add = a*b
#     print(add)
# sum( 3, 4)
# sum(200, 300)

# FILE I/O

# with open("demo.txt","r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt","w") as f:
#     f.write("hello my coders")

# import os
# os.remove("rohan.txt")  # use for deleting files 

# with open("pratice.txt", "r") as f:
#     data = f.read()
# new_data = data.replace("python", "java")
# print(new_data)
    
# with open("pratice.txt", "w") as f:
#     f.write(new_data)

# def check_for_word():
#     word = "learning"
#     with open("pratice.txt", "r") as f:
#         data = f.read()
#         if(word in data):
#             print("FOUND")
#         else:
#             print("NOT FOUND")

# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("pratice.txt", "r") as f:
#         while data :
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return 
#             line_no+= 1
# check_for_line()

# i = 0
# with open("pratice.txt", "r") as f:
#     data = f.read()
    
#     nums = data.split(",")
#     for val in nums :
#         if(int(val)%2==0):
#             i+=1
# print(i)


    # OOPS 

# class Student:
#     def __init__(self , fullname , marks):
#         self.name = fullname
#         self.marks = marks
    
#     def welcome(self):
#         print("welcome uuu :",s1.name)

#     def score(self):
#         return self.marks
       

# s1 = Student("rohan" , 98)

# s1.welcome()
# print("ur score is :" ,s1.score())

# class Student:
#     def __init__(self , name , marks):
#         self.name = name
#         self.marks = marks
#     def enterName(self):
#         print("Enter ur Name : " ,s1.name)

#     def score(self):
#         return self.marks

#     def avg(self):
#         sum = 0
#         for val in self.marks:
#             sum+=val
#         print("avg score is :" , sum/3)

# s1 = Student("Rohan" , [99,95,96])
# s1.enterName()
# print("ur score for this subject is :" ,s1.score())
# s1.avg()

# class Account:
#     def __init__(self , balance, accno):
#         self.balance = balance
#         self.accno = accno

#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs:" ,amount ,"debited")
#         print("total balance :", self.get_balance())

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs:" ,amount ,"credited")
#         print("total balance :",self.get_balance())

#     def get_balance(self):
#         return self.balance

# acc1 = Account(10000 , 1234)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(40000)
# acc1.debit(25000)

# private methods 
# class Student :
#     __name = "rohan"
#     def __hello(self):
#         print("hello person")

#     def welcome(self):
#         self.__hello()

# p1 = Student()
# print(p1.welcome())
    
# INHERITANCE 

# class Car:
#     color = "black in color"
#     @staticmethod
#     def start():
#         print("car started..")
#     @staticmethod
#     def stop():
#         print("car stoped..")

# class ToyoCar(Car):
#     def __init__(self ,name):
#         self.name = name 

# class Fourtuner(ToyoCar):
#      def __init__(self , type):
#         self.type = type
   
# car1 = Fourtuner("disel type")
# car1.start()
# car1.stop()
# print(car1.type)
# print(car1.color)

# POLYMORPHISM

# class Complex:
#     def __init__(self , real, image):
#         self.real = real 
#         self.image = image
#     def ShowNumber(self):
#         print(self.real ,"i+", self.image, "j")

#     def __add__(self , c2):
#         newReal = self.real + c2.real
#         newImage = self.image + c2.image
#         return Complex(newReal , newImage)

#     def __sub__(self , c2):
#         newReal = self.real - c2.real
#         newImage = self.image - c2.image
#         return Complex(newReal , newImage)


# c1 = Complex(3, 4)
# c1.ShowNumber()

# c2 = Complex(5, 6)
# c2.ShowNumber()

# c3 = c1 - c2
# c3.ShowNumber()
 
# class Order:
#     def __init__(self , item , price):
#         self.item = item 
#         self.price = price

#     def __gt__(self,o2):
#         return self.price > o2.price
  
# o1 = Order("chips :" , 20)
# o2 = Order("doritos :", 30)
# print( o1 > o2)
