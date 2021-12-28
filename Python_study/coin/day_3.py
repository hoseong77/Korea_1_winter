# -*- coding: utf-8 -*-
#인코딩을 utf-8로 변환 한글 오류 해결

#3장 클래스와 PyQt
#ch03/03_01.py ==> 절차지향 코드
pos = 0
def forward(pos):
    return pos + 20
pos = forward(pos)
print(pos)

#ch03/03_02.py ==> 객체지향 코드
class SuperMario:
    def __init__(self):
        self.pos = 0
    def forward(self):
        self.pos = self.pos + 20
mario = SuperMario()
mario.forward()
print(mario.pos)

#ch03/03_03.py ==> 절차지향 코드
p1_pos = 0
p2_pos = 0
def forward(pos):
    return pos + 20
p1_pos = forward(p1_pos)
p2_pos = forward(p2_pos)

#ch03/03_04.py ==> 객체지향 코드
class SuperMario:
    def __init__(self):
         self.pos = 0
    def forward(self):
         self.pos = self.pos + 20 
mario_p1 = SuperMario()
mario_p2 = SuperMario()
mario_p1.forward()
mario_p2.forward()

a = 3
print(type(a))
print(a.bit_length())

b = "python"
print(type(b))
print(b.upper())

#class
class MyClass:
    pass

obj = MyClass()
print(id(obj))

#ch03/03_05.py
class Myclass:
    def method(self):
        print("method") #class 안의 함수(def) : method
obj = MyClass()
obj.method()

#ch03/03_06.py
class Myclass:
    def add(self,a,b):
        return a+b
obj = MyClass()
ret = obj.add(3,4)
print(ret)

#ch03/03_07.py
class Customer:
    def __init__(self,id,name):
        self.id = id
        self.name = name
customer1 = Customer(1,"김은수")
customer2 = Customer(2,"이영희")