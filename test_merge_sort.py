import pytest
from merge_sort import merge_sort   # Import the function (not implemented yet)


# Test case 1: Sorting an empty list should return an empty list
def test_empty_list():
    assert merge_sort([]) == []


def main():
    pass


if __name__ == "__main__":
    pytest.main()