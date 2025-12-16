# --- STEP 1: Squares of Numbers ---

numbers = [1,2,3,4,5]

def square_list(nums):
    print("--- Squares of Numbers ---")
    for n in nums:
        square = n*n
        print(f"the square of {n} is : {square}")

# Function ko call karna
square_list(numbers)

# --- STEP 2: Palindrome Check ---
print("\n--- STEP 2: Palindrome Checker ---")
word =input("Enter a word to check: ")

# Method 1: Slicing
# Iska matlab hai word ko peeche se likhna
reversed_word = word[::-1]

print(f"Original word: {word}")
print (f"Reversed word: {reversed_word}")

#We will check them in lowercase to avoid mistakes with 'M' and 'm'
if word.lower() == reversed_word.lower():
    print("Result : yes, it is a Palindrome")
else:
    print("Result : no, it is not a Palindrome")    

#--- step 3: Even or Odd check_---

def check_even_odd(nums):
 print("\n--- STEP 3: Even or Odd Check ---")
 for n in nums:
        # % operator se pata chalta hai ki number even hai ya odd
       if n%2==0:
        print(f"{n} is Even")
       else:   
        print(f"{n} is Odd")    

# Calling the function to check even or odd
check_even_odd(numbers) 

