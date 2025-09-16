import re

class Search:
    def __init__(self, filename="Rhyme.txt"):
        self.filename = filename
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.lines = f.readlines()
        except FileNotFoundError:
            # Raise again so server can handle
            raise FileNotFoundError(f"File '{self.filename}' not found.")

    def clean(self, text):
        # Remove special characters, keep alphanumeric + spaces
        return re.sub(r'[^A-Za-z0-9\s]', '', text)

    def getLines(self, pattern):
        # Ensure cleaning is applied
        cleaned_lines = [self.clean(line.strip()) for line in self.lines]

        results = [pattern]
        for idx, line in enumerate(cleaned_lines, start=1):
            if re.search(pattern, line, re.IGNORECASE):
                results.append((idx, line))
        return results
