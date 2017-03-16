import sys
import pytest

def main():
    print(sys.modules['pytest'])
    # => <module 'pytest' from 'path\\to\\python_mock_sample\\env\\lib\\site-packages\\pytest.py'>

if __name__ == '__main__':
    main()