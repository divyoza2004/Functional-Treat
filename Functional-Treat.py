print("Welcome to the Data Analyzer and Transfomer  Program\n") 
array1d = []

def input_data():
    user_input = input("Enter data for a 1D array (separated by spaces): ")
    string_list = user_input.split()
    for item in string_list:
        number = int(item)
        array1d.append(number)
    print("Data has been stored successfully!")
     
def summary_data():
    array_length = len(array1d)
    array_min = min(array1d)
    array_max = max(array1d)
    array_sum = sum(array1d)
    array_average = array_sum/len(array1d)
    print("\nData Summary:")
    print(f"1. Total elements: {array_length}")
    print(f"2. Minimum value: {array_min}")
    print(f"3. Maximum value: {array_max}")
    print(f"4. Sum of all values: {array_sum}")
    print(f"Average value: {array_average}")
    
def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)

def filter_data():
    threshold = int(input("Enter a threshold value: "))
    result = list(filter(lambda x: x >= threshold, array1d))
    print("Filtered Data (values >=", threshold, "):")
    print(*result)
    
def sort_data():
    print("Choose Sorting option: ")
    print("1. Ascending order") 
    print("2. Descending order")
    y = int(input("Enter your sorting option numbers: ")) 
    if y==1:
        array = sorted(array1d)
        print("Sorted Data in Ascending order: ")
        print(*array) 
    elif y==2:
        array = sorted(array1d)
        print("Sorted Data in Descending order: ")
        array1 = reversed(array) 
        print(*array1)
    else: 
        print("Error: Invalid User Inputs") 

def statistics(array1d):
    minimum = min(array1d)
    maximum = max(array1d)
    total = sum(array1d)
    average = total / len(array1d)
    return minimum, maximum, total, average
        
while True: 
    print("\nSelect Your Mode")
    print("1. User Input Data")
    print("2. Display Data Summary") 
    print("3. Calcualte Factorial") 
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit") 
    x =  int(input("\nEnter your choice: ")) 
    match x:
        case 1:
            input_data()
        case 2:
            summary_data()
        case 3: 
            num = int(input("Enter a positive number and above zero: "))
            print(f"Factorial of {num} is: {factorial(num)}") 
        case 4:
            filter_data()
        case 5:
            sort_data()
        case 6:
            min, max, total, average = statistics(array1d)
            print(f"Minimum = {min}") 
            print(f"Maximum = {max}") 
            print(f"Total = {total}") 
            print(f"Average = {average}") 
        case 7:
            print("Session Closed, GoodBye!") 
            break
        case _:
            print("Error: Invalid User Input")