numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 List to be filtered from above

#Write your 1 line code 👇 below to filter, create and store in a new list:

# new_list = [new_item for item in list if test]

result = [n for n in numbers if n % 2 == 0]

#Write your code 👆 above:

print(result)