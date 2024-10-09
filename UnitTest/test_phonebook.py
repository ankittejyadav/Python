import unittest

from phonebook import Phonebook


class PhonebookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.phonebook = Phonebook()

    def tearDown(self) -> None:
        pass

    def test_lookup_by_name(self):
        # phonebook = Phonebook()
        self.phonebook.add("Ankit", "123456")
        number = self.phonebook.lookup("Ankit")

        self.assertEqual(number, "123456")

    def test_name_not_present(self):
        # phonebook = Phonebook()
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    # @unittest.skip("Working on it")
    def test_empty_phonebook_is_consistent(self):
        # phonebook = Phonebook()
        is_consistent = self.phonebook.is_consistent()
        self.assertTrue(is_consistent)

    # def test_is_consistent(self):
    #     self.phonebook.add("Ank", "1234567")
    #     self.assertTrue(self.phonebook.is_consistent)
    #     self.phonebook.add("Var", "4567890")
    #     self.assertTrue(self.phonebook.is_consistent)
    #     self.phonebook.add("Sam", "1234567")
    #     self.assertFalse(self.phonebook.is_consistent)
    #     self.phonebook.add("Sam", "123")
    #     self.assertFalse(self.phonebook.is_consistent)

    def test_is_consistent_with_different_entries(self):
        self.phonebook.add("Ank", "1234567")
        self.phonebook.add("Var", "4567890")
        self.assertTrue(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate(self):
        self.phonebook.add("Ank", "1234567")
        self.phonebook.add("Sam", "1234567")
        self.assertFalse(self.phonebook.is_consistent())

    def test_inconsistent_with_same_prefix(self):
        self.phonebook.add("Ank", "1234567")
        self.phonebook.add("Sam", "123")
        self.assertFalse(self.phonebook.is_consistent())
