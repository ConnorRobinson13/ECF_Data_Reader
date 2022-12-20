import pytest
import src.Sheet as Sheet
import src.Category as Category
import src.Element as Element


def test_set_sheet_name():
    s = Sheet.Sheet("Test")

    with pytest.raises(Exception):
        s = Sheet.Sheet(None)

    with pytest.raises(Exception):
        s.set_sheet_name(None)

    with pytest.raises(Exception):
        s.set_sheet_name("")

    assert s.get_sheet_name() == "Test"

    s.set_sheet_name("test1")
    assert s.get_sheet_name() == "test1"


def test_add_category():
    s = Sheet.Sheet("Test")
    assert len(s.get_list_of_categories()) == 0
    data = ["1", "2", "3", "4"]
    c = Category.Category("test", data)
    s.add_category(c)

    assert len(s.get_list_of_categories()) == 1
    assert s.get_list_of_categories()[0].get_name() == "test"
    assert s.get_list_of_categories()[0].get_elements()[1].get_name() == "2"


def test_get_category():
    s = Sheet.Sheet("Test")

    data = ["1", "2", "3", "4"]
    c = Category.Category("test", data)
    s.add_category(c)

    data2 = ["5", "6", "7"]
    c2 = Category.Category("test2", data2)
    s.add_category(c2)

    temp = s.get_category("test")
    assert temp.get_name() == "test"
    assert temp.get_elements()[0].get_name() == "1"

    temp2 = s.get_category("test2")
    assert temp2.get_name() == "test2"
    assert temp2.get_elements()[0].get_name() == "5"

    with pytest.raises(Exception):
        s.get_category("dagsda")
