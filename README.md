
# Introduction
    Resolved Issue: When reading a file, the inadvertent use of "w" mode will erase the original file's contents.
# Install
```Shell
    pip install safe_open
```
# How to use
```Python
    from safe_open import safe_open

    with safe_open("test.txt", "w") as f:
        f.write("Hello, World!")  # 正常写入
    
    with safe_open("test.txt", "r") as f:
        content = f.read()  # 正常读取

    with safe_open("test.txt", "w") as f: # OSError: file mode error: cannot read in write mode
        content = f.read()  # 异常读取

    with safe_open("test.txt", "r") as f: # OSError: file mode error: cannot write in read mode
        content = f.write()  # 异常写入
```