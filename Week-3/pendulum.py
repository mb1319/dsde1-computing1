import math as m
L = 0
g = 0 #variable reset

def main():
    variable_check = isinstance(L,g)

def period(L,g):
    ratio = L / g
    T = 2* m.pi * m.sqrt(ratio)
    return T
length = int(input("Length:  "))

print(period(length, 9.81))
