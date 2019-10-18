
my_items = [1,2,3,6,89]

    # (1 + recursive_sum[2,3,4,5)
	# (1 + (2 + recursive_sum[3,4,5]))
	# (1 + (2 + (3 + recursive_sum[4,5])))
	# (1 + (2 + (3 + (4 + recursive_sum5]))))	
	# (1 + (2 + (3 + (4 + (5)))))
    # then just order of operation
	# 1 + 3 + 9
	# 1 + 2 + 12
	# 1 + 14
	# 15




def recursion_sum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + recursion_sum(numbers[1:])

print(recursion_sum(my_items))
print(sum(my_items))


# Fibonacci rule:
# starts with 0 and 1
# subsequent numbers are the sum of the previous two

#current has default value of one
def fib(numbers, current=1 , previous=0, count = 0):
    if count < numbers:
        return fib(numbers, current+previous, current, count +1 )
    else:
        return current

print(fib(34))
