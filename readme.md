# Folder Structure Generator

## Overview
This Python script automates the creation of directories and files based on a predefined list. It ensures that necessary parent directories exist before creating files, preventing errors due to missing paths.

## How It Works
- The script defines a list of directories and files to be created.
- It iterates over the list and determines whether each path is a **directory** or a **file**.
- If it is a directory, it creates it (including any missing parent directories).
- If it is a file, it ensures the parent directory exists before creating an empty file.
- The script logs every step to provide feedback on what has been created or already exists.

## Installation & Usage
### Prerequisites
Ensure you have **Python 3.6+** installed on your system.

### Running the Script
1. Save the script as `create_structure.py`.
2. Open a terminal or command prompt.
3. Navigate to the script's directory.
4. Run the script using:
   ```bash
   python create_structure.py
   ```

## Code Breakdown
### 1. **Logging Setup**
The script starts by configuring logging to display messages with timestamps:
```python
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : [%(message)s]')
```

### 2. **List of Paths to Create**
```python
paths_to_create = [
    "data/", 
    "log/", 
    "data/file1.txt", 
    ".env", 
    "log/folder1/test.py"
]
```
- Directories are identified with a trailing `/`.
- Files do not have a trailing `/`.

### 3. **Processing Each Path**
```python
path = Path(path_str)
```
Converts each string path into a `Path` object for easier manipulation.

### 4. **Handling Directories**
```python
if path_str.endswith('/'):
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
```
- `mkdir(parents=True, exist_ok=True)` ensures parent directories are created if missing.
- The script logs whether the directory was created or already exists.

### 5. **Handling Files**
```python
if not path.parent.exists():
    path.parent.mkdir(parents=True, exist_ok=True)
```
Ensures the parent directory exists before creating a file.

```python
if not path.exists():
    path.touch()
```
Creates an empty file if it doesn’t already exist.

## Example Output
```bash
[2025-03-01 12:00:00] : [Created directory: data]
[2025-03-01 12:00:01] : [Created empty file: data/file1.txt]
[2025-03-01 12:00:02] : [Created empty file: .env]
[2025-03-01 12:00:03] : [Created directory: log/folder1]
```

## Notes
- The script **avoids overwriting** existing files and directories.
- Hidden files (like `.env`) are correctly handled as files, **not directories**.

## Conclusion
This script is a simple yet powerful utility for setting up project structures effortlessly. 🚀

