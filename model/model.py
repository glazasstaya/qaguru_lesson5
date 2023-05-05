import os
import pytest
from selene import browser, have


@pytest.fixture(scope='session')
def browser_settings():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 1000
    browser.config.window_width = 1800


class RegistrationForm:

    def open(self):
        browser.open('/automation-practice-form')

    def user_first_name_fill(self, value):
        browser.element('#firstName').type(value)

    def user_last_name_fill(self, value):
        browser.element('#lastName').type(value)

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

    def user_hobbies_select(self, value):
        browser.element(f'[for = hobbies-checkbox-{value}]').click()

    def file_select(self, file_name):
        browser.element('#uploadPicture').send_keys(os.getcwd() + file_name)

    def user_address_fill(self, value):
        browser.element('#currentAddress').type(value)

    def user_state_and_sity_select(self, state_value, sity_value):
        browser.element('[id=react-select-3-input]').type(state_value).press_enter()
        browser.element('[id=react-select-4-input]').type(sity_value).press_enter()

    def form_submit(self):
        browser.element('[id=submit]').press_enter()

    def result_table(self):
        return browser.element('.table-responsive').all('td')
