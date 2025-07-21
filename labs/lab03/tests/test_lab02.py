import subprocess
import sys

def test_lab02_prints_hello():
    output = subprocess.check_output([sys.executable, "labs/lab03/exercise.py"])
    assert b"Hello, Lab 03" in output
