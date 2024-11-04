def get_file_content(file: str) -> str:
    with open(file, 'r') as f:
        return f.read()