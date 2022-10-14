# demoFile.py 

#쿼리스트링방식 전달
url = 'http://www.naver.com/?page=' + str(1) 
print(url)

for x in range(1,6):
    print(x,"*",x,"=", x*x)

print('---정렬변경')
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3))


