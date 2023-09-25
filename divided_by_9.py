def check_divisible_by_9(first_number, second_number, third_number):

    # complete this function
    if first_number%9==0 or second_number%9==0 or third_number%9==0:
        return "True"
    else:
        return "False"

first_number = int(input())
second_number = int(input())
third_number = int(input())

result = check_divisible_by_9(first_number,second_number,third_number)
# Call the check_divisible_by_9 function

print(result)

"""
input:
3
9
16
output:True
"""
