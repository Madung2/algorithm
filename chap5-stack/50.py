"""
문제: 
선생님은 혀수에게 숫자 하나를 주고, 해당 숫자의 자리수들 중 m개 숫자를 제거하여 가장 큰 수를 만들라고 했습니다. 
만약 5276823 이 주어지고 3개의 자릿수를 제거한다면 7823이 가장 큰 숫자가 됩니다.
예제1:
5276823 3 => 7823
예제2:
9977252641 5  => 99776
"""
"""
풀이:
5부터 앞에 끄집어낼 수 있는지 확인. 자기보다 작은 수 out
2는 앞에 드랍 불가
7은 앞에 52 드랍가능
6은 앞에 7 드랍 불가
8은 앞에 7 ,6  드랍 가능 그중에 1개만 드랍하면 됨으로 
7>6으로 6 드랍

"""

num, m = map(int, input().split())
nums = list(map(int, str(num)))

print(num)

# current_list = [5,2,7,6,8,2,3] 
# for i, num in enumerate([5,2,7,6,8,2,3]):
#     # num은 주인공,  이전숫자= before_nums
#     before_nums =current_list[:i]
#     possible_drop_list = []
#     for j in  before_nums:
#         if j < i :
#             possible_drop_list.append(j)
#     current_
    
stack = []
for num in  nums:
    while stack and m > 0 and stack[-1]< num: # 스택이 빈값이 아니고 스택에 가장 최근게 num보다 작으면 최근걸 pop 한다.
        stack.pop()
        m-=1
    stack.append(num)

if m!=0:
    stack = stack[:-m]

print(stack)


