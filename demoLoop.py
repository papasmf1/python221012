# demoLoop.py
value = 5 
while value > 0:
    print(value)
    value -= 1 

print("---for in---")
d = {100:"apple", 200:"kiwi"}
for k,v in d.items():
    print(k,v)

lst = [100, "apple", 3.14]
for item in lst:
    print(item, type(item))

#구구단출력(outer loop)
for i in [2,3,4,5,6]:
    print("---{0}단---".format(i))
    #inner loop
    for j in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(i, j, i*j))


print("---break구문---")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    #블럭 주석:ctrl + / 
    if i > 5:
        break 
    print("item:{0}".format(i))

print("---continue구문---")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    #블럭 주석:ctrl + / 
    if i % 2 == 0:
        continue
    print("item:{0}".format(i))

print("---range()---")
print( list(range(10)) )
print( list(range(2000,2023)) )
for i in range(5):
    print(i)

print("---리스트컴프리핸션---")
lst = list(range(1,11))
print( [i**2 for i in lst if i > 5] )
tp = ("apple","orange","kiwi")
print( [len(i) for i in tp] )



