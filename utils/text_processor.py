import re

def slugify(text: str) -> str:
    """
    Converts a string into a URL-friendly slug.
    Example: "Hello World!" -> "hello-world"
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if not text:
        return ""
    
    # Convert to lowercase and remove non-word characters
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    # Replace whitespace/underscores with a single hyphen
    text = re.sub(r'[\s_-]+', '-', text)
    # Remove leading/trailing hyphens
    return text.strip('-')
```

Note: The issue is not in the provided test code or source code, but rather in the environment where the tests are being run. The pytest module is not installed. To fix this, you would need to install pytest using pip:
```bash
pip install pytest