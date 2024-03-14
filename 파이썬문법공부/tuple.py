#리스트와 같이 여러개의 데이터를 관리할 수 있는 또 다른 내장 자료형인 튜플이 있습니다.
#튜플은 소괄호로 묶습니다. 튜플 = (값1, 값2, ... )
#리스트와 튜플의 가장 큰 차이점은 튜플은 수정이 불가능하다는 것입니다. 
#읽기 전용(Read Only) 리스트라고 이해하셔도 될 것 같습니다

my_tuple = ('페라리', '람보르기니', '포르쉐') # 값들을 소괄호로 묶는 작업을 패킹이라고 합니다.

# 튜플도 순서가 보장됩니다.
print("-----------인덱싱-----------")
print(my_tuple[0])

print("-----------슬라이싱-----------")
print(my_tuple[0:2])

#포함여부도 확인할 수 있습니다.
print("-----------멤버 연산자-----------")
print('페라리' in my_tuple)

#길이 확인도 가능합니다!
print("-----------길이 확인, len()-----------")
print(len(my_tuple))


#파이썬에는 언패킹이라는 작업이 존재 합니다.
#패킹되어있는 튜플의 멤버들을 각각 원소에 넣는 작업입니다.

print("-----------언패킹-----------")
(str1, str2, str3) = my_tuple
print(str1)
print(str2)
print(str3)

#언패킹을 할 때 별(*)을 사용할 수 있습니다.
print("-----------언패킹 시 * 사용-----------")
numbers = (1,2,3,4,5,6,7,8,9,10)
(one, two, *others) = numbers
print(one)
print(two)
print(others) # 이때 others는 튜플이 아닌 리스트로 형성됩니다.