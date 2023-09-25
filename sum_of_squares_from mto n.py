def sum_of_squares_m_to_n(m, n):
    # Complete this function
    sum=0
    for i in range(m,n+1):
        sum+=i**2
    print(sum)

m = int(input())
n = int(input())
# Call the sum_of_squares_m_to_n function
sum_of_squares_m_to_n(m,n)

"""
input:
3
5
output:50
"""
