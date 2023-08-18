class SafeFileProxy:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file_obj = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_obj:
            self.file_obj.close()

    def read(self, *args, **kwargs):
        if "w" in self.mode or "a" in self.mode or "x" in self.mode:
            raise OSError("file mode error: cannot read in write mode")
        
        self.file_obj = open(self.filename, self.mode)
        return self.file_obj.read(*args, **kwargs)

    def write(self, *args, **kwargs):
        if "r" in self.mode:
            raise OSError("file mode error: cannot write in read mode")
        
        self.file_obj = open(self.filename, self.mode)
        return self.file_obj.write(*args, **kwargs)

    def __getattr__(self, attr):
        return getattr(self.file_obj, attr)

def safe_open(filename, mode):
    return SafeFileProxy(filename, mode)


if __name__ == "__main__":
    # 使用示例

    with safe_open("test.txt", "w") as f:
        f.write("Hello, World!")  # 正常写入
    
    with safe_open("test.txt", "r") as f:
        content = f.read()  # 正常读取

    with safe_open("test.txt", "w") as f: # OSError: file mode error: cannot read in write mode
        content = f.read()  # 异常读取

    with safe_open("test.txt", "r") as f: # OSError: file mode error: cannot write in read mode
        content = f.write()  # 异常写入