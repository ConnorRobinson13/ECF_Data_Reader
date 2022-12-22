import pytest

from src.Category import Category
from src.Sheet import Sheet
from src.SheetManager import SheetManager


def test_set_current_sheet():
    sm = SheetManager()
    sheet = Sheet("Test")
    sm.set_current_sheet(sheet)
    assert sm.get_current_sheet() == sheet


def test_get_current_sheet():
    sm = SheetManager()

    with pytest.raises(Exception):
        sm.get_current_sheet()


def test_get_category():
    sm = SheetManager()

    with pytest.raises(Exception):
        sm.get_category("Bruh")

    data = ["a", "b", "c"]
    c = Category("test", data)
    c2 = Category("test2", data)
    sheet = Sheet("test")
    sheet.add_category(c)
    sm.set_current_sheet(sheet)

    assert sm.get_category(c) == c

    with pytest.raises(Exception):
        sm.get_category(c2)


def test_get_categories():
    sm = SheetManager()

    with pytest.raises(Exception):
        sm.get_categories()

    data = ["a", "b", "c"]
    c = Category("test", data)
    c2 = Category("test2", data)
    sheet = Sheet("test")
    sheet.add_category(c)
    sheet.add_category(c2)
    sm.set_current_sheet(sheet)

    assert len(sm.get_categories()) == 2
    assert sm.get_categories()[0].get_name() == "test"


def test_get_selected_sheet():
    sm = SheetManager()

    with pytest.raises(Exception):
        sm.get_selected_sheet()

    data = ["a", "b", "c"]
    c = Category("test", data)
    c2 = Category("test2", data)
    sheet = Sheet("test")
    sheet.add_category(c)
    sheet.add_category(c2)
    sm.set_current_sheet(sheet)
    sm.add_to_selected(c)

    assert len(sm.get_selected_sheet().get_categories()) == 1


def test_add_to_selected():
    sm = SheetManager()

    data = ["a", "b", "c"]
    c = Category("test", data)
    c2 = Category("test2", data)
    sheet = Sheet("test")

    with pytest.raises(Exception):
        sm.add_to_selected(c)


def test_remove_from_selected():
    sm = SheetManager()

    data = ["a", "b", "c"]
    c = Category("test", data)

    with pytest.raises(Exception):
        sm.remove_from_selected(c)

    c2 = Category("test2", data)
    sheet = Sheet("test")
    sheet.add_category(c)
    sheet.add_category(c2)
    sm.set_current_sheet(sheet)
    sm.add_to_selected(c)
    sm.add_to_selected(c2)
    sm.get_selected_sheet().get_categories()

    assert len(sm.get_selected_sheet().get_categories()) == 2
    sm.remove_from_selected(c2)
    assert len(sm.get_selected_sheet().get_categories()) == 1
