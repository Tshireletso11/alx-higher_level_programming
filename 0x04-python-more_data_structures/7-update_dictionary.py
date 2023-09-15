#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value


# Example usage:
if __name__ == "__main__":
    my_dict = {'a': 1, 'b': 2}
    update_dictionary(my_dict, 'c', 3)  # Add a new key-value pair
    update_dictionary(my_dict, 'b', 4)  # Update an existing key's value
    print(my_dict)
