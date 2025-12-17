# --- List Functions ---

def get_sum(numbers):
    """Calculates and returns the sum and average of the numbers."""
    total = 0
    for num in numbers:
        total += num

    # --- EXTRA CHANGE: Calculating Average ---
    avg = total / len(numbers) if numbers else 0     
    return total, avg

def get_max(numbers):
    """Finds and returns the maximum value in the list."""
    if not numbers:
        return None
    
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

# --- String Function ---

def analyze_string(text):
    """Prints length, upper/lower cases and returns reversed string."""
    
    # 1. Print length, Uppercase and Lowercase (New Task)
    print(f"\nThe length of the string is: {len(text)}")
    print(f"Uppercase: {text.upper()}") 
    print(f"Lowercase: {text.lower()}")

    # 2. Reverse the string (Purana Task - should be inside the function)
    reversed_text = text[::-1]
    return reversed_text # Return sabse aakhri line honi chahiye function ki

# --- Main Program Execution Logic ---

def main_program():
    
    # A. Number Analysis
    print("--- 1. Number Analysis (Sum, Average and Max) ---")
    numbers_list = []
    print("Please enter 5 numbers:")
    
    for i in range(5):
        while True:
            try:
                num_input = int(input(f"Enter number {i+1}: "))
                numbers_list.append(num_input)
                break
            except ValueError:
                print("Invalid input. Please enter a whole number.")
    
    # get_sum ab do values deta hai (sum aur avg)
    sum_result, avg_result = get_sum(numbers_list)
    max_result = get_max(numbers_list)
    
    print(f"\nList of numbers: {numbers_list}")
    print(f"Total Sum: {sum_result}")
    print(f"Average: {avg_result}") # Print average
    print(f"Maximum Value: {max_result}")
    
    # B. String Analysis
    print("\n--- 2. String Analysis (Length, Case and Reverse) ---")
    input_text = input("Please enter a word or sentence: ")
    
    # Call string function
    reversed_text = analyze_string(input_text)
    print(f"Reversed String: {reversed_text}")

# Main execution trigger
if __name__ == "__main__":
    main_program()