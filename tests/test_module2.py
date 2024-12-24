import sys
import os
from .module1 import greet

# Add the project directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from test1.my_package.module2 import main

def test_module2():
    main()
    assert True

def main():
    print("Executing module2")
    greet()

