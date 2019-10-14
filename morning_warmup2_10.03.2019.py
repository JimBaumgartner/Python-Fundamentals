#10.03.2019


purchased_items = [
   {
      "id": "A088",
      "count": 32,
      "price": 4.88
   },
   {
      "id": "A002",
      "count": 29,
      "price": 3.40
   },
   {
      "id": "A199",
      "count": 2,
      "price": 8.90
   },
   {
      "id": "A332",
      "count": 78,
      "price": 22.78
   },
   {
      "id": "A001",
      "count": 10,
      "price": 3.99
   }
]


for id in purchased_items:
     print(id)

if id in purchased_items:
   print('found it')
# else:
#    print('nope')


# new_list = purchased_items

# print(new_list)

# print(purchased_items[:1:1])
new_list = purchased_items[:1:1]
print(new_list)
# if  'id' in new_list:
#    print('found it')
# else:
#    print('nope')
   


