#10.07.2019

# Creating new fies
new_file = open("./file_io_hub/employees_import.txt", "x") # creating a new txt file
    #file_io_hub-- is the FOLDER that you are going to put the new file into
    #testing.txt is the file to be created
    # "x" is the 

new_file.write("hello world!")

new_file.close()
newer_file = open("./file_io_hub/what_ever.py", "a") 
newer_file.write("""
newest_file = open("./file_io_hub/what_ever.py", "a") 
newest_file.write()
newest_file.close()
"""
newer_file.close()

create a python file in python that itself mofifies the testing.txt file to say
"Im sorry, i cannont do that"

python_file = open("./file_io_hub/change_text.py", "x") # creating a new txt file
file_io_hub-- is the FOLDER that you are going to put the new file into
    #testing.txt is the file to be created
    # "x" is the characteer (if it can overwrite etc)
valid_code = """
to_change = open("./testing.txt","a")

to_change.write("Im sorry i cannot do that")
to_change.close()

"""

python_file.write(valid_code)
python_file.close()


with open("with_statement.py", "w") as f:  # with will close the file for me
    f.write("# I'm a comment\nprint('Hello World')")