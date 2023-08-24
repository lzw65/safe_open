from setuptools import setup, find_packages

setup(
    name="safe_open",
    version="0.2.1",
    packages=find_packages(),
    install_requires=[
        # your dependencies here
    ],
    author="lzw65",
    author_email="zhuimengboy65@gmail.com",
    description="Safe open function",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lzw65/safe_open",
)
