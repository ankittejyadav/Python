from phonebook import Phonebook
import pytest


@pytest.fixture
def phonebook(tmpdir):
    "Provides an empty phonebook"
    phonebook = Phonebook(tmpdir)
    yield phonebook
    phonebook.clear()


def test_lookup_by_name(phonebook) -> None:
    # phonebook = Phonebook()
    phonebook.add("Ankit", "123456")
    number = phonebook.lookup("Ankit")
    assert number == "123456"


def test_all_names(phonebook) -> None:
    # phonebook = Phonebook()
    phonebook.add("Ankit", "123456")
    # assert phonebook.all_names() == {"Ankit", "Varun"}
    # assert "Varun" in phonebook.all_names()
    assert phonebook.all_names() == {"Ankit"}


def test_name_not_present(phonebook) -> None:
    # phonebook = Phonebook()
    # phonebook.add("Bob", "123456")
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")


def test_phonebook_is_consistent_with_different_entries(phonebook):
    phonebook.add("Ankit", "12345")
    phonebook.add("Varun", "67890")
    assert phonebook.is_consistent()


def test_phonebook_inconsistent_with_same_entries(phonebook):
    phonebook.add("Ankit", "12345")
    phonebook.add("Varun", "12345")
    assert not phonebook.is_consistent()


def test_phonebook_inconsistent_with_same_prefix(phonebook):
    phonebook.add("Ankit", "1234567890")
    phonebook.add("Varun", "12345")
    assert not phonebook.is_consistent()


@pytest.mark.parametrize(
    "entry1,entry2,is_consistent",
    [
        (("Ankit", "12345"), ("Varun", "67890"), True),
        (("Ankit", "12345"), ("Varun", "12345"), False),
        (("Ankit", "1234567890"), ("Varun", "12345"), False),
    ],
)
def test_is_consistent(phonebook, entry1, entry2, is_consistent):
    phonebook.add(*entry1)
    phonebook.add(*entry2)
    assert phonebook.is_consistent() == is_consistent
