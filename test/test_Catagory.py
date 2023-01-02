import pytest

import src.Category as Category


def test_set_name():
    data = ["a", "b", "c"]
    c = Category.Category("Test", data)

    with pytest.raises(Exception):
        c.set_name(None)

    with pytest.raises(Exception):
        c.set_name("")

    c.set_name("bruh")
    assert c.get_name() == "bruh"


def test_find_unique_elements():
    data = ["a", "b", "c", "a", "a", "b"]
    c = Category.Category("Test", data)

    unique = c.find_unique_elements()
    assert len(unique) == 3

    assert unique[0] == "a"
    assert unique[1] == "b"
    assert unique[2] == "c"

    assert c.get_elements()[0].get_name() == "a"
    assert c.get_elements()[1].get_name() == "b"
    assert c.get_elements()[2].get_name() == "c"

    assert c.get_elements()[0].get_occurrences() == 3
    assert c.get_elements()[1].get_occurrences() == 2
    assert c.get_elements()[2].get_occurrences() == 1


def test_to_string():
    data = ["a", "b", "c", "a", "a", "b"]
    c = Category.Category("Test", data)
    assert c.to_string() == "Category Name: Test\n" \
                            "- Element Name: a, Occurrences: 3\n" \
                            "- Element Name: b, Occurrences: 2\n" \
                            "- Element Name: c, Occurrences: 1\n"
