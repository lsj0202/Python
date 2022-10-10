s1 = {2,4,6,8,10}
s2 = {1,2,3,4,5,6,7,8,9,10}

interset = s1 & s2 #교집합
print(interset)
print(s1.intersection(s2), s2.intersection(s1)) #함수 사용
print(s1) #s1의 값이 바뀌는 것이 아님

uniset = s1 | s2 #합집합
print(uniset)
print(s1.union(s2))
print(s1) #s1의 값이 바뀌는 것이 아님

difset1 = s1 - s2 #어떤 집합에서 어떤 집합을 빼느냐에 따라 다른 결괏값
difset2 = s2 - s1
print(difset1)
print(difset2)