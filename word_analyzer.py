# Word Analyzer App

def analyze_sentence(sentence):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    # Count vowels and consonants
    for char in sentence:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    # Word count
    words = sentence.split()
    word_count = len(words)

    # Character count
    char_count = len(sentence)

    # Palindrome check
    cleaned = sentence.replace(" ", "").lower()
    is_palindrome = cleaned == cleaned[::-1]

    # Store results in a tuple
    results = (word_count, char_count, vowel_count, consonant_count, is_palindrome)
    return results

# Main program
sentence = input("Enter a sentence: ")
word_count, char_count, vowel_count, consonant_count, is_palindrome = analyze_sentence(sentence)

print("\n--- Analysis Results ---")
print(f"Words: {word_count}")
print(f"Characters: {char_count}")
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
print("Palindrome:", "Yes" if is_palindrome else "No")

Output:
Enter a sentence: madam
--- Analysis Results ---
Words: 1
Characters: 5
Vowels: 2
Consonants: 3
Palindrome: Yes

