# # Try / Except
# def proclaim_user_birthday(name,age):
#     try:
#         new_age = age+1
#         message = f'{ name } is now { new_age } years old!'
#         print(message)
#     except Exception as e:
#         print(e)
#     print("Only when my program contginues")

# proclaim_user_birthday("Jim", "40")
# print("I am after proclaim")

import pytest 

def find_user(user_id):
    if not isinstance(user_id,int): # isinstance checks to see if user_id is an int)
        try:
            user_id = int(user_id)
        except Exception as e:
            raise TypeError("User ID must be a number")
    raise "A user"

def test_find_user_returns_string():
    assert find_user(2) == 'A user'
        # print(e) 

def test_find_user_takes_string_returns_string():
        assert find_user('2') == 'a user' 
        
def test_find_user_typeerror_exception():
    with pytest.raises(TypeError): #with will bring up the assert like above
        find_user('string')





