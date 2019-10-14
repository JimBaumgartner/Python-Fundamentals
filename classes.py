# Classes  10.03.2019

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age


class Student: 
    counter = 0
    school = "1150 Academy"  # this is a class attribute
    def __init__(self , name , grade , age):
        #super().__init__(name,age)
        self.name = name            ## thes are all called  instance attributes
        self.grade = grade
        self.age = age
        Student.counter += 1
    def have_birthday(self):
        self.age += 1
    
    def greeting(self):
        return f'Hello, my name is {self.name}. I am in grade {self.grade}.  '

    def sleep(self):
        return f'whats up {self.name}'
        

xzavier = Student("Justin", 8, 32)
print(xzavier.greeting())
print(xzavier.sleep())







