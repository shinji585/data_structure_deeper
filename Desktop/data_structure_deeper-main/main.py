"""
Data Structure Learning Project - Main Entry Point

This module serves as the main entry point for the data structure implementations.
All tests are located in the 'tests/' folder.

To run all tests:
    pytest tests/ -v

To run specific test files:
    pytest tests/test_singly_linked_list.py -v
    pytest tests/test_doubly_linked_list.py -v

To view code coverage:
    pytest tests/ --cov=linkendlist --cov-report=html
    
    Then open: htmlcov/index.html (requires: cd htmlcov && python -m http.server 8000)
"""


def main() -> None:
    """Main entry point - for future use with different structures"""
    print("Data Structure Deeper - Learning Project")
    print("=" * 50)
    print("Available structures:")
    print("  - Singly Linked List")
    print("  - Doubly Linked List")
    print("\nTo run tests:")
    print("  pytest tests/ -v")
    print("\nTo check code coverage:")
    print("  pytest tests/ --cov=linkendlist --cov-report=html")


if __name__ == "__main__":
    main()
