def get_odd_numbers_in_range(start_number, end_number):
    
    # complete this function
    odd=""
    for i in range(start_number,end_number+1):
        if i%2!=0:
            odd+=str(i)+" "
    return odd
        
    

start_number = int(input())
end_number = int(input())

odd_numbers = get_odd_numbers_in_range(start_number,end_number)
# Call the odd_numbers_in_range function

print(odd_numbers)

"""
input:
2
7
output:3 5 7 

"""
