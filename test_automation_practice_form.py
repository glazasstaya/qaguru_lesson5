import pytest
from selene import browser, have
import os


def test_success_form_send(browser_settings):
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('tata')
    browser.element('#lastName').type('test')
    browser.element('#userEmail').type('test@test.ru')
    browser.element('[for = gender-radio-2]').click()
    browser.element('#userNumber').type('7999999999')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select [value="3"]').click()
    browser.element('.react-datepicker__year-select [value="1985"]').click()
    browser.element('.react-datepicker__day.react-datepicker__day--011.react-datepicker__day--weekend').click()

    browser.element('#subjectsInput').type('co').press_enter().type('ma').press_enter()
    browser.element('[for = hobbies-checkbox-2]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/img/bradford.jpg')
    browser.element('#currentAddress').type('тестовый адрес')

    browser.element('[id=react-select-3-input]').type('NCR').press_enter()
    browser.element('[id=react-select-4-input]').type('Delhi').press_enter()
    browser.element('[id=submit]').press_enter()
    ...
    browser.element('.table-responsive').all('td').should(have.texts('Student Name', 'tata test',
                                                                     'Student Email', 'test@test.ru',
                                                                     'Gender', 'Female',
                                                                     'Mobile', '7999999999',
                                                                     'Date of Birth', '11 May,1985',
                                                                     'Subjects', 'Computer Science, Maths',
                                                                     'Hobbies', 'Reading',
                                                                     'Picture', 'bradford.jpg',
                                                                     'Address', 'тестовый адрес',
                                                                     'State and City', 'NCR Delhi'))
    ...