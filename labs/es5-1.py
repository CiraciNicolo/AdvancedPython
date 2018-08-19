import unittest
import string

def anagram(s):
    s = s.translate(None, string.punctuation).lower().replace(' ', '')
    return s==s[::-1]

class FunctionsTests(unittest.TestCase):
    def test_anagram(self):
        self.assertEqual(False, anagram("Test"))
        self.assertEqual(True, anagram("I topi non avevano nipoti."))
        self.assertEqual(True, anagram("Do geese see God?"))
        self.assertEqual(True, anagram("Rise to vote, sir."))

if __name__ =='__main__':
    unittest.main()
