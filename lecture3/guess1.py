# def sum( #объяв функ и называем ее
#         x: int, #переменная х
#         y: int,
# ) -> int: #функция вернет инт
#     ans=x+y
#     return ans
# print(sum)


# def mySum(
#         num_list: list
# ) -> int:
#     answer = 0
#     for num in num_list:
#         answer
#     return answer
# print(mySum([3,5,1]))



def mySum(*args, **kwargs) -> int:
    answer=0
    for num in args:
        answer+=num
    return answer
print(mySum(3, 5, 1 ,4, 1, name='bob'))
