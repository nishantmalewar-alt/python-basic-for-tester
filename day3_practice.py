# --- Part 1: List + Loop ---

numbers = [2,5,8,3,9]
for n in numbers:
    print(n)

print("\nEven numbers in the list:")
for n in numbers:
    if n % 2 ==0:
        print(n)

 # --- Part 2: Function print_even(numbers) ---

def print_even(numbers_list):
    """Prints even numbers from the provided list."""
    print("\nEven numbers from the provided list:")
    for num in numbers_list:
        if num % 2 == 0:
            print(num)

# --- Part 3: String + words analysis ---

sentence = input("Please enter a sentence: ")

# 2. वाक्य (sentence) को शब्दों में बाँटो (Split)
words = sentence.split()

# 3. Total words print करो
# len() function list में items की संख्या बताता है
print(f"Total words in the sentence: {len(words)}")

# 4. Uppercase sentence print करो
# .upper() method string के सभी characters को uppercase में बदल देता है
print(f"Uppercase sentence: {sentence.upper()}")