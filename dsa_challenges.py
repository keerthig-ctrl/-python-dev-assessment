def filter_and_sort_evens(numbers):
    evens = [n for n in numbers if n % 2 == 0]
    return sorted(evens)



def count_character_frequency(text: str) -> dict:
    """
    Return a dictionary mapping each alphabetic
    character (lowercased)
    to its frequency in 'text'
    """
    text = text.lower()
    freq = {}
    for char in text:
        if char.isalpha():
            freq[char] = freq.get(char,0) +1
        return freq
    
print(filter_and_sort_evens([13,4,1,9,5,6,2]))

print(count_character_frequency("Hello World!"))