
import re
import os

try:
    from pypdf import PdfReader  
except ImportError:
    PdfReader = None


class Search:
    def __init__(self, filename):
        if not filename or not os.path.exists(filename):
            raise FileNotFoundError(f"File not found: {filename}")

        self.filename = filename
        self.ext = os.path.splitext(filename)[1].lower()
        self.lines = self._load_file()

    def _load_file(self):
        """Load file lines depending on extension."""
        if self.ext == ".txt":
            with open(self.filename, "r", encoding="utf-8", errors="ignore") as f:
                return [line.rstrip("\n") for line in f]

        elif self.ext == ".pdf":
            if not PdfReader:
                raise ImportError("pypdf required for PDF search. Install with `pip install pypdf`")

            lines = []
            try:
                with open(self.filename, "rb") as f: 
                    reader = PdfReader(f)
                    for page in reader.pages:
                        text = page.extract_text()
                        if text:
                            lines.extend(text.splitlines())
            except Exception as e:
                raise ValueError(f"Error reading PDF file: {e}")

            return lines

        else:
            raise ValueError(f"Unsupported file type: {self.ext}")

    def clean(self, text: str) -> str:
        """Remove non-alphanumeric characters (except whitespace)."""
        return re.sub(r"[^A-Za-z0-9\s]", "", text)

    def getLines(self, pattern: str):
        """
        Search for `pattern` in the file (case-insensitive, regex supported).
        Returns: ["pattern", (line_no, line_text), ...]
        """
        regex = re.compile(pattern, flags=re.IGNORECASE)
        matches = []

        for i, original in enumerate(self.lines, start=1):
            cleaned = self.clean(original)
            if regex.search(cleaned):
                matches.append((i, original))  

        return [pattern] + matches
