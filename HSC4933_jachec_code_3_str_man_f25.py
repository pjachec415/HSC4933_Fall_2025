#############################################
# A script to practice string manipulation. #
#############################################
# H. Jachec # HSC4933 # B. Jacob # 09/29/25 #
#############################################

### --- Section 1: Name Formatting --- ###
# Ask user for name
name = input ("What is your name? ")

# Print name and wrapper
print (f"Hello, {name}! Nice to meet you.")

### --- Section 2: Word Reversal --- ###
# Get word input
word = input ("Enter a word to reverse: ")

# Reverse word
word_rev = "".join(reversed(word))

# Print reversed string and wrapper
print (f"The word {word} reversed is {word_rev}.")

### --- Section 3: String Length --- ###
# Get user input sentence
sent = input("Enter a sentence to calculate its length: ")

# Calculate length
length = len(sent)

# Print output and wrapper
print (f"The length of the sentence '{sent}' is: {length}.")

### --- Section 4: Vowel Count --- ###
# Get user input
vowels = input("Enter a word or sentence to get a vowel count: ")

# Define vowel count function
def count_vowels_iterative(text):
    vwls = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vwls:
            count += 1
    return count

# Calculate numbers of vowels
vcount = count_vowels_iterative(vowels)

# Print output and wrapper
print (f"The count of vowels in '{sent}' is: {vcount}.")

### --- Section 5: Palindrome Check --- ###
# Get user input and strip capitals and spaces
pali = str(input("Enter a sentence to see if it's a palindrome: "))

pali_strip = pali.replace(" ", "")
pali_lower = pali_strip.lower()

# reverse the word and strip vowels and spaces
pali_rev = "".join(reversed(pali_lower))

print ({pali_rev})

# Check if the phrase is a palindrome and print responses
if pali_lower == pali_rev:
    print (f"The phrase '{pali}' is a palindrome.")

else:
    print (f"The phrase '{pali}' is not a palindrome.")

### --- section 6: Secret Message --- ###
# Get user input
secret = input("Enter a sentence to make it a secret phrase: ")

# Format is "encrypted"
secret = secret.replace(" ", "_").upper()

# Print output and wrapper
print (f"Encrypted secret message: {secret}")
