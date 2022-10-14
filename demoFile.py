# demoFile.py 

#쿼리스트링방식 전달
url = 'http://www.naver.com/?page=' + str(1) 
print(url)

for x in range(1,6):
    print(x,"*",x,"=", x*x)

print('---정렬변경')
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3))

print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(1500000))

#파일 쓰기(유니코드로 저장)
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close() 

#파일 읽기
f = open("c:\\work\\demo.txt", "rt", encoding="utf-8")
print( f.read() )
#어디쯤 읽고 있어? 
print( f.tell() )
#리셋(다시 처음)
f.seek(0)
print("---readline()---")
result = f.readline() 
print( result.replace("\n", "") )
print( f.readline(), end="" )
#리셋(다시 처음)
f.seek(0)
result = f.readlines()
print(result)

f.close() 