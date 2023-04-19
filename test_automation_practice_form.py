import pytest
from selene import browser

def test_success_form_send():
    browser.config.timeout = 20
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('id="firstName"').type('tata')
    browser.element('id="lastName"').type('tata')
    browser.element('id="userEmail"').type('test@test.ru')
    browser.element('[id="gender-radio-2"]').double_click()
    browser.element('id="userNumber"').type('7999999999')
    browser.element('id="dateOfBirthInput"').click()
    browser.element('[class="react-datepicker__month-select" ] [value="2"]').click()
