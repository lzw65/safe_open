from safe_open import safe_open
import pytest

def test_open_read():
    with safe_open("test.txt", "w") as f:
        f.write("Hello, World!")

    with safe_open("test.txt", "r") as f:
        content = f.read() 
        assert content, "Hello, World!"

    with pytest.raises(OSError, match="file mode error: cannot read in write mode"):
        with safe_open("test.txt", "w") as f:
            content = f.read() 

    with safe_open("test.txt", "r") as f:
        content = f.read() 
        assert content, "Hello, World!"

def test_open_write():
    with safe_open("test.txt", "w") as f:
        f.write("Hello, World!")

    with pytest.raises(OSError, match="file mode error: cannot write in read mode"):
        with safe_open("test.txt", "r") as f:
            f.write("Hello, World2!")

    
    with safe_open("test.txt", "r") as f:
        content = f.read() 
        assert content, "Hello, World!"