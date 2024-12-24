from setuptools import setup, find_packages

setup(
    name="test1",
    version="0.1.0",
    description="A placeholder project for testing package creation",
    author="MUZA",
    author_email="munagreat123@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],  # Add required dependencies here
    entry_points={
        "console_scripts": [
            "test1-script1=scripts.script1:main",
            "test1-script2=scripts.script2:main",
        ]
    },
)
