str = "Hello goorm!!!"
print(str, type(str))

s0 = set(str)
print(s0, type(s0))

newstr = tuple(s0)
print(newstr, newstr[4], newstr[5:], type(newstr)) #인덱싱, 슬라이싱 가능

l = [1,2,3,4,5,6,7,8]
print(l, type(l))

s1 = set(l)
print(s1, type(s1))

newlist = list(s1)
print(newlist, newlist[4], newlist[:-5], type(newlist))