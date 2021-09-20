import time

import  pytest

def test_basket_button(browser):
    #starting browser
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    #waiting element "Add to basket"
    while True:
        try:
            basket = browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']").is_displayed()
            break
        except:
            time.sleep(1)

    #Checking that "Add to basket" is present at page
    assert basket == True
    time.sleep(10)