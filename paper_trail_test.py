import pytest
import tempfile, shutil

from paper_trail import Scanner

def test_givenEmptyDirectory_thenCountFilesIsEmpty(tmpdir):
    scanner = Scanner(tmpdir)
    assert scanner.countFiles() == 0
