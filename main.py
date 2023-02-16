from roman import *

roman1 = [str(vvodR) for vvodR in input('Введите римское число:').upper().split()]
for i in roman1:
    print(i, '->' ,roman_to_int(i))

arabic= [int(vvodA) for vvodA in input('Введите арабское число:').split()]
for i in arabic:
    print(i, '->',int_to_roman(i))