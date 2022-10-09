# # -*- coding: utf-8 -*-
# # UTF-8 encoding when using korean
# mem = {"김구름": 25, "박에듀": 23, "온라인": 24}
#
# print(mem.keys())
# names = list(mem.keys()) #새로운 리스트 변수에 초기화
#
# # names.append("윤레벨")
# # print("새로운 리스트",names)
# # print("원래 딕셔너리에서 key 모음", list(mem.keys()))
# # print(mem.values())
# # print(list(mem.values()))
# # print("key와 value를 튜플로", mem.items())
# # print("key와 value를 튜플로", mem)
# print(mem.get("정판교", "없습니다"), mem.get("온라인", "없습니다"))
#
# exist = '박에듀' in mem #굉장히 직관적인 용법
# print(exist)
#
# exist = '김구름' in mem
# print(exist)
#
# mem.clear()
# print(mem) #빈 딕셔너리 출력

dic_test={'노래제목':'highwaytohell'}

dic_test["가수"]="ACDC"
print(dic_test)
dic_test["일자"]=2022
print(dic_test)
del dic_test['노래제목']
print(dic_test)
print(dic_test["가수"])
temp = dic_test.get("성별","잉기모링")
print(temp)
print(dic_test.keys())
print(dic_test.values())
print(list(dic_test.keys()))
print(list(dic_test.values()))