print("Welcome to the Data Analyzer and Transfomer Program") 
array1d = []

def input_data():
    """----Add Input Data----"""
    user_input = input("Enter data for a 1D array (separated by spaces): ")
    string_list = user_input.split()
    for item in string_list:
        number = int(item)
        array1d.append(number)
    print("Data has been stored successfully!")
     
def display_summary(**kwargs):
    """Print out any dataset details passed to it."""
    print("\n--- Dataset Summary ---")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
def factorial(n):
    """----Factorial----"""
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)

def filter_data():
    """----Filter Data----"""
    threshold = int(input("Enter a threshold value: "))
    result = list(filter(lambda x: x >= threshold, array1d))
    print("Filtered Data (values >=", threshold, "):")
    print(*result)
    
def sort_data():
    """----Sorted Array----"""
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
    """----Statistics Datasets Information----"""
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
            print(input_data.__doc__)
            input_data()
        case 2:
            print(display_summary.__doc__)
            display_summary(total_elements = len(array1d), minimum_value = min(array1d), maximum_value = max(array1d), sum = sum(array1d))
        case 3: 
            print(factorial.__doc__)
            num = int(input("Enter a positive number and above zero: "))
            print(f"Factorial of {num} is: {factorial(num)}") 
        case 4:
            print(filter_data.__doc__)
            filter_data()
        case 5:
            print(sort_data.__doc__)
            sort_data()
        case 6:
            min, max, total, average = statistics(array1d)
            print(statistics.__doc__)
            print(f"Minimum = {min}") 
            print(f"Maximum = {max}") 
            print(f"Total = {total}") 
            print(f"Average = {average}") 
        case 7:
            print("Session Closed, GoodBye!") 
            break
        case _:
            print("Error: Invalid User Input")      
