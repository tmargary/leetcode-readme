 
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1",
    description="Recursively check a GitHub repo's files and return a README file in the format [Text](url)",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "PyGithub==1.55"
    ],
    entry_points={
        "console_scripts": [
            "get-readme-links=my_package.get_readme_links:main"
        ]
    }
)
