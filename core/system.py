# core/system.py
class System:
    def get_version(self):
        return "1.0.0"

    def process_data(self, data):
        if not data: return None
        return data.strip().lower()
```

However, the actual issue is that pytest is not installed in the environment. To fix this, you can install pytest using pip:

```bash
pip install pytest
```

Alternatively, you can also install pytest using a requirements file (e.g., `requirements.txt`):

```bash
pip install -r requirements.txt
```

Make sure to add `pytest` to your `requirements.txt` file:

```bash
# requirements.txt
pytest