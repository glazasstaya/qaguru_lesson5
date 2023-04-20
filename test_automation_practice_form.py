import pytest
from selene import browser

def test_success_form_send():
    browser.config.timeout = 2
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('tata')
    browser.element('#lastName').type('test')
    browser.element('#userEmail').type('test@test.ru')
    browser.element('#gender-radio-2').double_click()
    browser.element('#userNumber').type('7999999999')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select [value="3"]').click()
    browser.element('.react-datepicker__year-select [value="1985"]').click()
    browser.element('.react-datepicker__day.react-datepicker__day--011.react-datepicker__day--weekend').click()
    browser.element('.css-1g6gooi').click().type('test')