i=False
f = 0.2
w=1
b = 2

_list: list= [
   32, 43,  1, 4, 5, False, 'asda'
]
print(_list[1:7])
print(_list[-2])
print(_list[:-1])
print(_list[0:-1:2])
print(_list[::-1])

print(
   len( _list[::-1])
    )

_set1: set=set({i, f, w, b})
_set2: set = [
    "m", "i", 's', 's', 'p', 'p'
]
_set3: set = [
    "m", "a", 'a', 'm'
]
print(_set1, _set2) 
print(_set1.difference( _set2)) #разница
print(_set1.intersection( _set2)) 
mississipi= 'mississipi'
