# get an input from user a number, total.
# Sum the numbers starting from 1 to n till they are greater than total given number.
# For example given total is 20, you stop at 7. and give the total as 24.
# 1 + 2 +3 +5 +6 = 17
# 1 + 2 +3 +5 +6 + 7 = 24

# For example given total is 60, you stop at 11. 
# and give the total as 62.
# 1 + 2 +3 +5 +6 + 7 + 8 + 9 + 10 = 51
# 1 + 2 +3 +5 +6 + 7 + 8 + 9 + 10 + 11 = 62

str_total = input("give me a number, total, to find 1..n > total")
given_total = int(str_total)

total = 0
for n in range(1,given_total):
    total = total + n
    print(total,n)
    if( total > given_total):
        break



print(f"1..{n}={total}")

