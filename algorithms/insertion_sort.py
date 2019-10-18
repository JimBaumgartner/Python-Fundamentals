    
def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        print(numbers)
        item_to_insert = numbers[i]
        print(numbers)
        j = i - 1

        while j >= 0 and numbers[j] > item_to_insert:
            numbers(j + 1) = numbers.pop[1]

        numbers.insert(j + 1 , item_to_insert)

my_list = [5,4,3,2,1]
insertion_sort(my_list)
print(my_list)
