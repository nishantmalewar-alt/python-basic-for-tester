# --- List Functions ---

def get_sum(numbers):
    """Calculates and returns the sum of the numbers in the list."""
    total = 0
    # Loop through each number and add it to the total
    for num in numbers:
        total += num
    return total

def get_max(numbers):
    """Finds and returns the maximum value in the list."""
    if not numbers:
        return None # Handle case where the list is empty
    
    max_val = numbers[0]
    # Loop through the rest of the list to find a larger value
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

# --- String Function ---

def analyze_string(text):
    """Prints the length of the string and returns the reversed string."""
    
    # Print the length of the string
    # len() is a built-in Python function
    length = len(text)
    print(f"\nThe length of the string is: {length}")
    
    # Reverse the string using simple slicing [::-1]
    reversed_text = text[::-1]
    return reversed_text


# --- Main Program Execution Logic ---

def main_program():
    
    # A. Get 5 Numbers from User and Analyze
    print("--- 1. Number Analysis (Sum and Max) ---")
    
    numbers_list = []
    print("Please enter 5 numbers:")
    
    # Loop to ensure we collect exactly 5 valid integer inputs.
    for i in range(5):
        while True:
            try:
                # Get input and convert it to an integer.
                num_input = int(input(f"Enter number {i+1}: "))
                numbers_list.append(num_input)
                break
            except ValueError:
                print("Invalid input. Please enter a whole number (integer).")
    
    # Call the list functions and receive the returned values.
    sum_result = get_sum(numbers_list)
    max_result = get_max(numbers_list)
    
    # Print the final results for the numbers analysis.
    print(f"\nList of numbers: {numbers_list}")
    print(f"Total Sum: {sum_result}")
    print(f"Maximum Value: {max_result}")
    
    
    # B. Get String from User and Analyze
    print("\n--- 2. String Analysis (Length and Reverse) ---")
    
    input_text = input("Please enter a word or sentence: ")
    
    # Call the string function.
    reversed_text = analyze_string(input_text)
    
    # Print the reversed string (length was printed inside the function).
    print(f"Reversed String: {reversed_text}")

# This standard Python line ensures the main_program() function runs when the script is executed directly.
if __name__ == "__main__":
    main_program()