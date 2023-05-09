from selene import browser, have
import os
from definition import ROOT_DIR


class RegistrationForm:

    def open(self):
        browser.open('/automation-practice-form')

    def form_fill(self, UserData):
        browser.element('#firstName').type(UserData.first_name)
        browser.element('#lastName').type(UserData.last_name)
        browser.element('#userEmail').type(UserData.email)
        browser.all('[name=gender]').element_by(have.value(UserData.gender)).element('..').click()
        browser.element('#userNumber').type(UserData.pnone_number)
        browser.element('#dateOfBirthInput').click()
        browser.element(f'.react-datepicker__year-select [value="{UserData.birth_year}"]').click()
        browser.element(f'.react-datepicker__month-select [value="{UserData.birth_month}"]').click()
        browser.element(f'.react-datepicker__day.react-datepicker__day--0{UserData.birth_day}.react-datepicker__day').click()
        for subject in UserData.subjects:
            browser.element('#subjectsInput').type(subject).press_enter()
        for hobbie in UserData.hobbies:
            browser.element(f'[for = hobbies-checkbox-{hobbie}]').click()
        browser.element('#uploadPicture').send_keys(os.path.abspath(os.path.join(ROOT_DIR, 'img', UserData.file_name)))
        browser.element('#currentAddress').type(UserData.address)
        browser.element('[id=react-select-3-input]').type(UserData.state).press_enter()
        browser.element('[id=react-select-4-input]').type(UserData.sity).press_enter()

    def form_submit(self):
        browser.element('[id=submit]').press_enter()

    def result_table(self):
        return browser.element('.table-responsive').all('td')



