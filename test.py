#Test 1
def is_valid_string(input_string):
    # Check if the string is at least 6 characters long
    if len(input_string) < 6:
        return False
    
    # Initialize counters and a flag for checking non-numerical characters
    num_count = 0
    prev_char_was_digit = False
    for i in range(len(input_string)):
        char = input_string[i]
        
        # Check if the current character is a digit
        if char.isdigit():
            num_count += 1
            # If this is not the first number, check if it's preceded by a non-digit
            if prev_char_was_digit:
                return False  # Two digits in a row, which is not allowed
            prev_char_was_digit = True
        else:
            # Reset the flag if it's not a digit (i.e., non-numeric character)
            prev_char_was_digit = False
    
    # Check if the number of digits is between 2 and 3
    if num_count < 2 or num_count > 3:
        return False

    return True


#Test2
import string

def count_word_frequencies(text):
    # Convert text to lowercase to ensure case-insensitive comparison
    text = text.lower()
    
    # Manually remove punctuation by filtering out characters that are punctuation
    cleaned_text = ''.join([char if char not in string.punctuation else ' ' for char in text])
    
    # Split the text into words
    words = cleaned_text.split()
    
    # Create a dictionary to store word frequencies
    word_count = {}
    
    # Count the occurrences of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Sort the words by frequency in descending order
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    # Display the word frequencies
    print("Word Frequencies:")
    for word, count in sorted_word_count:
        print(f"{word}: {count}")

# Example usage
text = "Hello world! This is a test. Hello, this test is only a test."
count_word_frequencies(text)


