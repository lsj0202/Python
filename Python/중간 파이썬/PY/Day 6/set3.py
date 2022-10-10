s1 = {1, 2, 3, 4}

s1.add("hello")
print(s1)

s1.add(10)
print(s1)

s1.add((1,2,3)) #add() 사용 시 튜플/문자열은 값 하나로 인식
print(s1)


s1.update(['a', 'b', 'c']) #set()과 같이 여러 값을 한 요소로 저장
s1.update((11,12))
print(s1)

s1.update("zyx") #s1.add("hello")와의 차이
print(s1)

s1.remove("hello") #하나의 값만 제거 가능
print(s1)

s1.remove((1,2,3))
print(s1)