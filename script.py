# a = "try"

# # try:
# #     print(int("4m"))
# # except:
# #     print("მეგობარო, ფრთხილად წარმოიქმნა შეცდომა გადააკეთე შენი კოდი")

# print(int("4m"))
# print("hello")


# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         x = x/0
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
#     except ZeroDivisionError:
#         print("Oops!  That was zero division, please dont do it again! :) ")

from math import *
from turtle import *
count = 0

# while count<8:
#     print("Saba")
#     count+=1
    
# def a():
#     return 5
# try:

#     print(g)
#     print("gamarjoba")
# except:
#     print("რაღაც შეცდომა მოხდა")

# print(g)
# # print("gamarjoba"+5)

# a = input('შეიყვანეთ პირველი გვერდის სიგრძე:')
# try:
#     a = int(a)
# except:
#     print('შეცდომაა! შეიყვანე მხოლოდ რიცხვი, ტექსტის გარეშე')
#     a = int(input('შეიყვანეთ პირველი გვერდის სიგრძე:'))
# b = input('შეიყვანეთ მეორე გვერდის სიგრძე:')
# try:
#     b = int(b)
# except:
#     print('შეცდომაა! შეიყვანე მხოლოდ რიცხვი, ტექსტის გარეშე')
#     b = int(input('შეიყვანეთ მეორე გვერდის სიგრძე:'))
# s = a * b
# print('სამკუთხედის ფართობი:', s)


color('red', 'yellow')
begin_fill()
while True:
    print(pos())
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
