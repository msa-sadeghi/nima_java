# عدد = int(input("enter a number: "))
# if (عدد < 10 and عدد >= 0) or (عدد <= 0 and عدد > -10):
#     print("one digit")
# else:
#     print("not one digit")

# عدد = int(input("enter a number: "))
# عدد = abs(عدد)
# if عدد < 10:
#     print("one digit")
# else:
#     print("not one digit")

# x = int(input("ente a number: "))
# x = abs(x)
# print(x)

# def my_abs(num):
#     if num < 0:
#         num *= -1    
#     return num

# print(my_abs(1000))
# print(my_abs(-1000))





# age = int(input("enter student's age: "))

# if age >= 40:
#     print("old")
# elif age >= 18:
#     print("adult")
# elif age >= 13:
#     print("junior")
# elif age >= 8:
#     print("teenager")
# else:
#     print("kid")
 
    
    
# students = []
# for i in range(6):
#     name = input("enter a name: ")
#     students.append(name)
    
# print(students[::2])
# for i in range(0, len(students), 2):
#     print(students[i])


# x1 = (1,2)
# x2 = (3,4)
# print("x1 address in memory : ",id(x1))
# print("x2 address in memory : ",id(x2))

# x1 = x1 + x2
# print(x1)
# print("x1 address in memory : ",id(x1))

# scores = []
# for i in range(2):
#     s = float(input(f"enter the score #{i+1} "))
#     scores.append(s)
    
# scores = tuple(scores)
# print(scores.count(20))


# scores = ()
# for i in range(2):
#     s = float(input(f"enter the score #{i+1} "))
#     scores += (s,)
# print(scores.count(20))   

# ages = ()

# for i in range(3):
#     a = int(input("enter an age:> "))
#     ages += (a,)
# print(ages)
# c = 0
# for x in ages:
#     if x > 20:
#         c += 1
# print(c)
        
# for n in range(11, 100, 2):
#     print(n)

# count = 0
# for i in range(7):
#     year = int(input("enter the year: "))
#     if year >= 1380 and year < 1390:
#         count += 1
# print(count)

# string = input("enter a string: ")
# for s in string:
#     print(s)

# for i in range(1,5):
#     print(i * str(i))
# s = 0
# for i in range(1,11):
#     s += i
# print(s)
    
import turtle

sc = turtle.Screen()
sc.register_shape("python.gif")
# name = sc.textinput("info", "enter your name")
t = turtle.Turtle()
t.shape('turtle') #'turtle', 'circle', 'square', 'triangle', 'classic'
# t.write(name, align="center", font=("arial", 23))
t.shape("python.gif")
t.pensize(4)
t.pencolor("green")
t.fillcolor("red")
t.begin_fill()
for i in range(3):
    t.forward(200)
    t.left(120)
t.end_fill()
t.penup()
t.goto(-150, 100)
t.pendown()
t.begin_fill()
for i in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()
turtle.done()