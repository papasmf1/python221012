# function3.py
#함수 정의(키워드 인자 방식)
def connectURI(server, port):
    strURL = "http://" + server + ":" + port 
    return strURL

#호출
print( connectURI("credu.com", "80") )
print( connectURI(port="80", server="credu.com") )

#가변인자 
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result 
#호출
print( union("HAM","EGG") )
print( union("HAM","EGG","SPAM") )