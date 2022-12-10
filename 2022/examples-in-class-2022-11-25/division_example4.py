print("please enter two numbers for division")
s_dividend = input("please enter dividend: ")
s_divisor = input("please enter divisor: ")

try:

	# we get a ValueError if the s_dividend or s_divisor is not a number
	# like aaa bbb ccc
	dividend = float(s_dividend)
	# we get a ZeroDivisionError if s_divisior is 0 (Zero)
	divisor = float(s_divisor)


	division = dividend / divisor
	print(f"division result for {dividend}/{divisor} = {division}")

# since exception is more GENERAL than ValueError or ZeroDivisionError
# this line works others does not work
except Exception:
	print("an exception occured")

except ValueError:
	print("You entered an incorrect value for dividend or divisor")

except ZeroDivisionError:
	print("You entered 0 (Zero) for divisor")
