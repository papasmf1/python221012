# demoIndex.py
strA = "python is very powerful"
strB = "파이썬은 강력해"
print( strA[0] )
print( strA[0:6] )
print( strA[:6] )
print( strA[-3:] )
print( strA[-8:] )
print( strA[:] )
print( strB[-3:] )

#리스트 형식을 연습
colors = ["red","blue","green"]
print( len(colors) )
print( colors[0] )
#자동완성
colors.append("white")
print(colors)
colors.insert(1, "pink")
print(colors)
colors += ["red"]
colors += "red"
print(colors)
print( colors.index("red") )
print( colors.index("red",1) )
colors.append("red")
print("---red 2번째---")
print( colors )
print( colors.count("red") )
print( colors.index("red",2) )

print( colors.count("red") )
print("---pop()---")
print( colors.pop() )
print( colors.pop() )
print( colors.pop(1) )
colors.remove("red")
colors.extend(["blue","white","black"])
colors.sort()
print(colors)
colors.reverse()
print(colors)

