import src.Element as Element


def test_set_name():
    element = Element.Element("Test", 1)
    element.set_name("Test1")
    assert element.get_name() == "Test1"


def test_set_occurrences():
    element = Element.Element("Test", 1)
    element.set_occurrences(12)
    assert element.get_occurrences() == 12


def test_to_string():
    element = Element.Element("Test", 314)
    assert element.to_string() == "Element Name: Test, Occurrences: 314"
