import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_link_add_to_cart(browser):
    browser.get(link)
    browser.get(link)
    # time.sleep(30)
    my_list = []
    element = browser.find_elements_by_css_selector("#add_to_basket_form button.btn")
    assert element != my_list, "Element not found"
