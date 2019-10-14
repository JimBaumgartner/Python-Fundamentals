# new_file = open("./file_io_hub/employees_import.txt", "a") # creating a new txt file
# #     #file_io_hub-- is the FOLDER that you are going to put the new file into
# #     #testing.txt is the file to be created
# #     # "x" is the 
# new_file.write("hello world!,  10.08.2019")
# new_file.close()


import csv

with open('acess','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:
        print(line[2])



        