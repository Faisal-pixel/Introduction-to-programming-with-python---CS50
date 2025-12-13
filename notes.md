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