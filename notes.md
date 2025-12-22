# 1. Using tripple quotted strings as comments in python:
    You can also use triple-quoted strings (either """ or ''') to create text blocks that function like comments, provided they are not assigned to a variable. The Python interpreter reads this as a string literal but ignores it because it has no function or variable association.
```python
    """
This text is a string, but because it's not assigned
to a variable, it is effectively ignored by the
interpreter and acts as a comment.
"""
print("Hello, World!")

```

    Note: If a triple-quoted string is the very first statement within a module, function, or class, it becomes a docstring (documentation string), which is a special type of string used for documentation and is accessible at runtime via the __doc__ attribute

# 2. Explaining the difference between mutable and immutable in python:
    Mutable means "Changeable." You can change what’s inside without getting a whole new thing.
    
    Immutable means "Unchangeable." Once you make it, you cannot change even a tiny bit of it. If you want something different, you have to throw the old one away and make a brand-new on

    Yes, strings in Python are immutable. This means that once a string object is created, its contents cannot be changed in-place. Any operation that appears to modify a string, such as concatenation or using a string method like replace(), actually creates a new string object in memory, and the variable is then updated to reference this new object. 

    1. You cannot change characters by index: Attempting to modify a single character using item assignment will result in a TypeError
        
```python
        my_string = "hello"
        # This will cause an error:
        # my_string[0] = "J"
        # TypeError: 'str' object does not support item assignment
```
    2. Operations return new strings: Methods like upper(), lower(), or replace() do not alter the original string; they return a new string with the specified changes.

```python
    greeting = "Hello"
    new_greeting = greeting.replace("H", "J")
    print(greeting) # Output: Hello (original is unchanged)
    print(new_greeting) # Output: Jello (new string)
```
    3. Reassignment creates a new object: When you reassign a variable to a new value (e.g., s = s + " world"), the variable name is simply updated to point to a new string object in a different memory location. 
    
    Why are strings immutable?
    This design choice provides several advantages in Python: 

    1. Thread Safety: Immutable objects can be safely shared across multiple threads in a program without the need for synchronization, as their values cannot be changed unexpectedly.

    2. Efficiency and Hashing: Immutability allows strings to be used as keys in dictionaries (and elements in sets) because their hash value can be calculated once and cached. If strings were mutable, their hash value could change, breaking the dictionary's internal structure.

    3. Predictability: Functions that take strings as arguments cannot modify the original data, preventing unintended side effects in other parts of the program. 
    If you need a mutable sequence of characters, Python provides the bytearray type or you can convert the string to a list of characters, modify the list, and then join it back into a string. 


# 3. Understanding the .split method:
    The string split() method in Python divides a string into a list of substrings based on a specified separator. The original string remains unchanged. 
    The basic syntax is str.split(sep=None, maxsplit=-1). 
    1. sep (separator): An optional argument that specifies the delimiter. If not provided (or if None is passed), any sequence of whitespace characters (spaces, tabs, newlines) is used as the separator, and empty strings are discarded from the result.
    
    2. maxsplit: An optional argument that limits the number of splits. The default is -1, which means all occurrences of the separator are used for splitting. If a positive integer is provided, the string will be split at most that many times, and the remaining part of the string is returned as the final element of the list. 

# 4. Understanding the enumerate function:
    enumerate() is a built-in Python function that adds a counter to an iterable and returns it as an enumerate object. This object can then be used directly in loops to easily access both the index (or count) and the corresponding item of the iterable [1]. 

    It works with a variety of iterables, including lists and dictionaries. 

>    **Using enumerate() with Lists**
>    When using enumerate() with a list, the function provides a tuple for each item containing the index (starting from 0 by default) and the value at that index.

>    **How to use it:**
>    ```python
>   fruits = ['apple', 'banana', 'cherry']
>    # The basic way to iterate with enumerate
>    for index, fruit in enumerate(fruits):
>        print(f"Index: {index}, Fruit: {fruit}")
>    # Output:
>    # Index: 0, Fruit: apple
>    # Index: 1, Fruit: banana
>    # Index: 2, Fruit: cherry
>   ```
    You can also specify a different starting index using the optional start parameter: 
```python
for index, fruit in enumerate(fruits, start=1):
    print(f"Index: {index}, Fruit: {fruit}")

# Output:
# Index: 1, Fruit: apple
# Index: 2, Fruit: banana
# Index: 3, Fruit: cherry
```
>    **Using enumerate() with Dictionaries**
        When you iterate over a dictionary directly, you are iterating over its keys. enumerate() works the same way: it adds a counter (index) to each key. 

>    **How to use it:**
```python
    # A dictionary where keys are items and values are quantities
    stock_levels = {'apples': 15, 'bananas': 20, 'cherries': 30}

    # Iterate over the dictionary's keys using enumerate
    for index, key in enumerate(stock_levels):
        # You can then use the key to access the value
        value = stock_levels[key]
        print(f"Index: {index}, Key: {key}, Value: {value}")

    # Output:
    # Index: 0, Key: apples, Value: 15
    # Index: 1, Key: bananas, Value: 20
    # Index: 2, Key: cherries, Value: 30
```
    Alternatively, you can iterate over the dictionary's .items() view, which already provides key-value pairs, and then use enumerate() to add an index to each pair: 
```python
for index, (key, value) in enumerate(stock_levels.items()):
    print(f"Index: {index}, Key: {key}, Value: {value}")

# Output:
# Index: 0, Key: apples, Value: 15
# Index: 1, Key: bananas, Value: 20
# Index: 2, Key: cherries, Value: 30
```
    In summary, enumerate() is a versatile tool for cleanly iterating through data structures when you need access to the index of the current item within the loop
