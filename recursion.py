# num = int(input("Enter the number: "))
# def factorial(num):
#     if (num==0 or num==1):
#         return 1
#     else: 
#         return num * factorial(num-1)
# print(factorial(num))    



# numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4,4,4]

# # Find the most repetitive number
# # most_repitative = max(numbers,key=numbers.count)
# # print(most_repitative)

# print(max(numbers.count))

# a = (1, 5, 3, 9)
# x = max(a)
# print(x)

num = int(input("Enter the number: "))

if num ==1 or num ==0:
    fact = 1 
    print(fact)
else:
    for i in num:
        fact = num * i
        i = num - 1 
        print(fact)   


# def fact(num):
#     if num == 1 or num ==0:
#         return 1
#     else:
#         return num * fact(num-1)
# print(fact(num))
# fact(num)
