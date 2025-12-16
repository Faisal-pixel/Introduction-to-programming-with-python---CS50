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

# 3. Understanding the .split method:
    The string split() method in Python divides a string into a list of substrings based on a specified separator. The original string remains unchanged. 
    The basic syntax is str.split(sep=None, maxsplit=-1). 
    1. sep (separator): An optional argument that specifies the delimiter. If not provided (or if None is passed), any sequence of whitespace characters (spaces, tabs, newlines) is used as the separator, and empty strings are discarded from the result.
    
    2. maxsplit: An optional argument that limits the number of splits. The default is -1, which means all occurrences of the separator are used for splitting. If a positive integer is provided, the string will be split at most that many times, and the remaining part of the string is returned as the final element of the list. 