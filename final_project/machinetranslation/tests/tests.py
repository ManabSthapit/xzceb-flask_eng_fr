import unittest, sys
from os.path import abspath, dirname

# Add the parent directory to the sys path
current_dir = dirname(dirname(abspath(__file__)))
sys.path.append(current_dir)

# pylint: disable=import-error
from translator import englishtofrench, frenchtoenglish
# pylint: enable=import-error

class testEnglishToFrench(unittest.TestCase):
    def test_eng_fr(self):
        self.assertEqual(englishtofrench('Hello'),'Bonjour')
        self.assertEqual(englishtofrench('Apple'),'Pomme')
        #self.assertEqual(englishToFrench(''),'Empty')

class testFrenchToEnglish(unittest.TestCase):
    def test_fr_eng(self):
        self.assertEqual(frenchtoenglish('Bonjour'),'Hello')
        self.assertEqual(frenchtoenglish('Pomme'),'Apple')
        #self.assertEqual(frenchToEnglish(''),'Empty')

unittest.main()