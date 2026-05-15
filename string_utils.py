def reverse_string(text: str) -> str:
    """
    Reverses the provided string.
    
    Args:
        text (str): The string to be reversed.
        
    Returns:
        str: The reversed string.
        
    Raises:
        TypeError: If the provided input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected a string, got {type(text).__name__}")
    return text[::-1]
