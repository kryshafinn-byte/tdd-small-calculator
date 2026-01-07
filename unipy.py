# def subtract(a, b):
#     return a - b


# def run_pytest():
#     print("Running the pytest-style tests...")

#     assert subtract(200, 30) == 170
#     assert subtract(-42, 52) == -94

#     # Intentional failing test
#     assert subtract(0, 10) == -10

#     print("Pytest-style tests passed!\n")


# if __name__ == "__main__":
#     run_pytest()


#     assert subtract(200, 30) == 170
#     assert subtract(-42, 52) == -94
#     assert subtract(0, 10) == -10

#     print("Pytest-style tests passed!\n")

# import unittest

# class TestSubtract(unittest.TestCase):
#     def test_subtract(self):
#         self.assertEqual(subtract(100,80),20)
#         self.assertEqual(subtract(20,0),20)
#         self.assertEqual(subtract(-90,-30), -60)

def reverse_text(name):
    """Return the reverse of the given string"""
    result = ""
    for letter in name:
        result = letter + result
    return result


def run_pytest():
    print("Running pytest-style tests...")

    assert reverse_text("krystal") == "latsyrk"

    print("All tests passed!\n")

if __name__ == "__main__":
    run_pytest()