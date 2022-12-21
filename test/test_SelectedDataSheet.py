from src.Category import Category
from src.SelectedDataSheet import SelectedDataSheet
from src.Sheet import Sheet


def test_selected_data_sheet():
    sds = SelectedDataSheet()
    s = Sheet("test")

    assert s.get_sheet_name() == "test"
    assert sds.get_sheet_name() == "Selected Categories"

    data = ["d", "a", "b"]
    c = Category("Test", data)
    s.add_category(c)

    cat = s.get_category("Test")
    sds.add_category(cat)

    assert sds.get_list_of_categories()[0].get_name() == "Test"
