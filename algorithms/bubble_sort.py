def bubble_sort(numbers):
    swapped = True

    while swapped == True:
        swapped = False
        for i in range(len(numbers) - 1 ):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[ i + 1 ]  = numbers[i + 1], numbers[i]
                swapped = True
my_list = [5,2,90,6,32]
bubble_sort(my_list)
print(my_list)
