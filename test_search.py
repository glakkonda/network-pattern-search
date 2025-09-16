# test_search.py
import pytest
from search import Search

def test_text_file_search(tmp_path):
    # Create a temporary text file
    f = tmp_path / "temp.txt"
    f.write_text("Hello world\nPython is great\n")

    s = Search(str(f))
    result = s.getLines("python")

    # Verify metadata
    assert result["pattern"].lower() == "python"
    assert result["file"] == "temp.txt"
    assert result["file_type"] == "txt"

    # Verify at least one match
    assert any("Python is great" in line for _, line in result["matches"])

def test_no_matches(tmp_path):
    f = tmp_path / "empty.txt"
    f.write_text("Only cats and dogs here\n")

    s = Search(str(f))
    result = s.getLines("python")

    # Should return empty matches
    assert result["matches"] == []
