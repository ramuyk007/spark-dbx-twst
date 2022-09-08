import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from app import demo

def test_hello_user():
    result = demo.hello_user("bob")
    assert result == "hello bob"
