import pytest
from selene import browser, have
import os

class RegistrationForm:

    def open(self):
        browser.open('/automation-practice-form')

    def user_first_name_fill(self, value):
        browser.element('#firstName').type('value')

    def user_last_name_fill(self, value):
        browser.element('#lastName').type('value')

    def user_email_fill(self, value):
        browser.element('#userEmail').type(value)

    def user_gender_select(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    def user_phone_fill(self, value):
        browser.element('#userNumber').type(value)

    def user_birtday(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element(f'.react-datepicker__year-select [value="{year}"]').click()
        browser.element(f'.react-datepicker__month-select [value="{month}"]').click()
        browser.element(f'.react-datepicker__day.react-datepicker__day--0{day}.react-datepicker__day').click()

    def user_subject_fill(self, value1, value2):
        browser.element('#subjectsInput').type(value1).press_enter().type(value2).press_enter()

def test_success_form_send(browser_settings):
    registration_form  = RegistrationForm()
    registration_form.open()

    registration_form.user_first_name_fill('tata')
    registration_form.user_last_name_fill('test')
    registration_form.user_email_fill('test@test.ru')
    registration_form.user_gender_select('Female')
    registration_form.user_phone_fill('79999999999')
    registration_form.user_birtday('15','5','1985')
    registration_form.user_subject_fill('co', 'ma')



    browser.element('[for = hobbies-checkbox-2]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/bradford.jpg')
    browser.element('#currentAddress').type('тестовый адрес')

    browser.element('[id=react-select-3-input]').type('NCR').press_enter()
    browser.element('[id=react-select-4-input]').type('Delhi').press_enter()
    browser.element('[id=submit]').press_enter()
    ...
    browser.element('.table-responsive').all('td').should(have.texts('Student Name', 'tata test',
                                                                     'Student Email', 'test@test.ru',
                                                                     'Gender', 'Female',
                                                                     'Mobile', '7999999999',
                                                                     'Date of Birth', '15 May,1985',
                                                                     'Subjects', 'Computer Science, Maths',
                                                                     'Hobbies', 'Reading',
                                                                     'Picture', 'bradford.jpg',
                                                                     'Address', 'тестовый адрес',
                                                                     'State and City', 'NCR Delhi'))
    ...