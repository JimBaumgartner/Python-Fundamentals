
employees = open('employees.csv', 'r').readlines()
access_list = open('access_list.csv', 'r').readlines()


employees.pop(0)  # this is removeing the header level
employees.pop() # this is removing the last one
access_list.pop(0)
access_list.pop()
modified_employees = []  # createing a blank list
for row in employees:  # for every row in the employees file
    info = row.split(',') # this is seperateing the entries at the ","
    modified_employees.append(info[3])

modified_access_list = []  # createing a blank list
for row in employees:  # for every row in the access file
    info = row.split(',') # this is seperateing the entries at the ","
    modified_access_list.append(info[0])  # adds from modified employees at index of 0 (first entry)
# unauthorized = [ip for ip in modified_access_list if ip not in modified_employees]
unauthorized = []  # creating a list for just the unautghorized ones
for ip in modified_access_list:
    if ip not in modified_employees:
        unauthorized.append(ip)
print(unauthorized)



# # other way
# def convert_to_list_dictionaries(the_list):
#     keys = the_list.pop(0).split(',')  # pop removes an item and returns it.  0 will remove the header, split is ?
#                                         # turning columns from csv file into a variablbe "keys"
#     to_return = []  # createing a blank list, need somewhere to put the data
    
#     for row in the_list:  #we are turning rows into dictionaries
#         entry = {} # creating an empty dictionary
#         values = row.split(',')
#         for i, key in enumerate(keys):  # loading up dictionary with keys
#             entry[key] = values[i]
#         to_return.append(entry)
#     return to_return
