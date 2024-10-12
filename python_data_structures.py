from enum import Enum

# Enumeration for list operations
class ListOperations(Enum):
    APPEND = 1
    REMOVE = 2
    ACCESS = 3
    SLICE = 4
    COMPREHEND = 5

def list_operations():
    """Demonstrates various operations on lists."""
    print("\n--- List Operations ---")

    # Create a sample list
    sample_list = [1, 2, 3, 4, 5]
    print(f"Original List: {sample_list}")

    # Iterate through the enumeration of list operations
    for operation in ListOperations:
        if operation == ListOperations.APPEND:
            sample_list.append(6)  # Append 6 to the list
            print(f"After appending 6: {sample_list}")
        elif operation == ListOperations.REMOVE:
            sample_list.remove(3)  # Remove the first occurrence of 3
            print(f"After removing 3: {sample_list}")
        elif operation == ListOperations.ACCESS:
            print(f"Element at index 2: {sample_list[2]}")  # Access element at index 2
        elif operation == ListOperations.SLICE:
            sliced_list = sample_list[1:4]  # Slice the list from index 1 to 3
            print(f"Sliced List (index 1 to 3): {sliced_list}")
        elif operation == ListOperations.COMPREHEND:
            squared_list = [x ** 2 for x in sample_list]  # List comprehension to square each element
            print(f"Squared List: {squared_list}")

def tuple_operations():
    """Demonstrates various operations on tuples."""
    print("\n--- Tuple Operations ---")

    # Create a sample tuple
    sample_tuple = (1, 2, 3, 4, 5)
    print(f"Original Tuple: {sample_tuple}")

    # Use enumerate to iterate through the tuple and print index-value pairs
    for index, value in enumerate(sample_tuple):
        print(f"Element at index {index}: {value}")

    # Slice the tuple from index 2 to 3
    sliced_tuple = sample_tuple[2:4]
    print(f"Sliced Tuple (index 2 to 3): {sliced_tuple}")

    print("Tuples are immutable, cannot modify directly!")

def set_operations():
    """Demonstrates various operations on sets."""
    print("\n--- Set Operations ---")

    # Create a sample set
    sample_set = {1, 2, 3, 4, 5}
    print(f"Original Set: {sample_set}")

    # Add an element to the set
    sample_set.add(6)
    print(f"After adding 6: {sample_set}")

    # Remove an element from the set
    sample_set.discard(3)  # Discard 3 (does not raise an error if not found)
    print(f"After discarding 3: {sample_set}")

    # Iterate over the set elements
    print("Iterating over set elements:")
    for element in sample_set:
        print(f"Set element: {element}")

    # Perform set operations: union and intersection
    another_set = {4, 5, 6, 7, 8}
    union_set = sample_set.union(another_set)  # Union of sets
    intersection_set = sample_set.intersection(another_set)  # Intersection of sets
    print(f"Union of sets: {union_set}")
    print(f"Intersection of sets: {intersection_set}")

def dictionary_operations():
    """Demonstrates various operations on dictionaries."""
    print("\n--- Dictionary Operations ---")

    # Create a sample dictionary
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print(f"Original Dictionary: {sample_dict}")

    # Add a new key-value pair
    sample_dict['d'] = 4
    print(f"After adding 'd': {sample_dict}")  # Directly refer to the new key

    # Remove a key-value pair
    sample_dict.pop('b')  # Remove key 'b'
    print(f"After removing key 'b': {sample_dict}")

    # Iterate over the dictionary items and print key-value pairs
    print("Iterating over dictionary:")
    for key, value in sample_dict.items():
        print(f"Key: {key}, Value: {value}")

    # Dictionary comprehension to create a new dictionary with squared values
    squared_dict = {k: v ** 2 for k, v in sample_dict.items()}
    print(f"Squared Values Dictionary: {squared_dict}")

def string_operations():
    """Demonstrates various operations on strings."""
    print("\n--- String Operations ---")

    sample_string = "Hello, World!"
    print(f"Original String: '{sample_string}'")

    # Accessing a character in the string
    print(f"Character at index 7: '{sample_string[7]}'")

    # Slicing the string
    sliced_string = sample_string[7:12]  # Slice from index 7 to 11
    print(f"Sliced String (index 7 to 11): '{sliced_string}'")

    # Convert string to uppercase and lowercase
    upper_string = sample_string.upper()
    lower_string = sample_string.lower()
    print(f"Uppercase String: '{upper_string}'")
    print(f"Lowercase String: '{lower_string}'")

    # Split the string into a list
    split_string = sample_string.split(", ")  # Split at ", "
    print(f"Split String: {split_string}")

    # Use enumerate to iterate over characters in the string
    print("Iterating over string characters:")
    for index, char in enumerate(sample_string):
        print(f"Index {index}: '{char}'")

def main():
    """Main function to test all data structure operations."""
    list_operations()
    tuple_operations()
    set_operations()
    dictionary_operations()
    string_operations()

if __name__ == "__main__":
    main()
