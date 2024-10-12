from collections import Counter

def substring(s, start, end):
    """Extracts a substring from the given string."""
    if not (0 <= start < end <= len(s)):
        raise ValueError("Invalid start or end index for substring.")
    return s[start:end]

def reverse_string(s):
    """Reverses the given string."""
    return s[::-1]

def indices_of_character(s, char):
    """Finds all indices of the specified character in the string."""
    return [index for index, c in enumerate(s) if c == char]

def to_upper(s):
    """Converts the string to uppercase."""
    return s.upper()

def to_lower(s):
    """Converts the string to lowercase."""
    return s.lower()

def most_used_character(s):
    """Finds the most used character in the string."""
    if not s:
        return None, 0
    # Using Counter for cleaner code
    char_count = Counter(s)
    most_used = char_count.most_common(1)[0]  # Get the most common character and its count
    return most_used

def compare_strings(str1, str2, ignore_case=False):
    """Compares two strings for equality, optionally ignoring case."""
    return str1.lower() == str2.lower() if ignore_case else str1 == str2

def starts_with(s, prefix):
    """Checks if s starts with the given prefix."""
    return s.startswith(prefix)

def ends_with(s, suffix):
    """Checks if s ends with the given suffix."""
    return s.endswith(suffix)

def analyze_string(s):
    """Analyzes the string and utilizes other functions."""
    print(f"Analyzing the string:
