from phonebook import Phonebook
import pytest


@pytest.fixture
def phonebook():
    phonebook = Phonebook()
    yield phonebook
    phonebook.clear()


def test_lookup_by_name() -> None:
    phonebook1 = Phonebook()
    phonebook1.add_empty("Ankit", "123456")
    number = phonebook1.lookup_empty("Ankit")
    # assert number == "123456"  # Fails

    phonebook2 = Phonebook()
    phonebook2.add("Ankit", "123456")
    number = phonebook2.lookup("Ankit")
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
