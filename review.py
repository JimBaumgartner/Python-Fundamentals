name = 'adam' , 13
print(type(name))

def multiple_returns(a,b):
    data = 0
    if a>b:
        data = b,a
    return True, data
print(multiple_returns(2,1))



def name_of_function(x, t): #(parameter or  positional arguement)
	return f'(t)' # -- this is calling the function
n = 3, "y"
# name_of_function(3, "y")
name_of_function(3,5)	

captured = name_of_function(3,5)  # this is captureing , asign it to a variable

print(captured)
#something.update( {"update" : 56 })


items = [1,2,3,4,5]
		
for  item in items:   # in is the iterable
	k = item + 12 
	print(k) # putting print here prints each line

print(k)    # putting print here prints just the last one



z = True
flag = 0
while z:
    flag += 1
    scoped = "Do i exist"
    if flag > 34:
        z = False

print(scoped)


if scoped:
    potato = "spuds"
    
print(potato)
