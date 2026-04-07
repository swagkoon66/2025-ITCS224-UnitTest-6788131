import unittest
import age
import threading

def print_is_what(number, output):
    return str(number) + " is considered as a  " + str(output) 

class test_all_ages(unittest.TestCase):
    # def test_even_number(self):
    #     for number in [2, 4, 6, -8, -10, -12]:
    #         with self.subTest(number=number):
    #             self.assertEqual((number) %2 == 0, True)

    
    def test_is_child(self):
        for _ in range(0,10,1):
            with self.subTest(_=_):
                self.assertEqual(age.categorize_by_age(_),"Child")
                print()
                print(print_is_what(_,age.categorize_by_age(_)))
    def test_is_adolescent(self):
        for _ in range(10,19,1):
            with self.subTest(_=_):
                self.assertEqual(age.categorize_by_age(_),"Adolescent")
                print()
                print(print_is_what(_,age.categorize_by_age(_)))
    def test_is_adult(self):
        for _ in range(19,66,1):
            with self.subTest(_=_):
                self.assertEqual(age.categorize_by_age(_),"Adult")
                print()
                print(print_is_what(_,age.categorize_by_age(_)))
    def test_is_golden_age(self):
        for _ in range(66,151,1):
            with self.subTest(_=_):
                self.assertEqual(age.categorize_by_age(_),"Golden age")
                print()
                print(print_is_what(_,age.categorize_by_age(_)))
        
if __name__ == "__main__":
    unittest.main(verbosity=2)
