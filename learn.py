#!/usr/bin/env python

import math

def move(x,y,step,angle):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

x, y = move(100, 100, 60, math.pi/6)

aTuple = move(100, 100, 60, math.pi/6)

print(x)
print("######")
print(y)
print("$$$$$$$$$$")
print(aTuple)
print(aTuple[0])

def power(x,n=2):
	if not isinstance(x,(int,float)):
		raise TypeError("Unaccepted Type, only integer or float number can be accepted")
	result = 1
	while n>0:
		n = n -1
		result = result * x

	return result

print(power(13,9))

def person(name,age,**other):
	print("Name:", name, "Age:", age, "Other:", other)

person("Tom", 30)
person("Tom", 30, city = "Shanghai", job = "Manager", address = "Rm 202, No. 817 Laiyang Road, Pudong New Area, Shanghai", Tall = "1.90M", gender = "Male")

other={'City': "Montreal, CA", 'Tall': "1.87M", 'Job': "Engineer"}
person("Michale", 56, **other)