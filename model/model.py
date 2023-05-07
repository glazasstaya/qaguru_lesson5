import selene
import pytest
from selene import browser, have
from dataclasses import dataclass
from enum import Enum
import os
from conftest import ROOT_DIR


def resources_path(dir_name, file_name):
    file_path_and_name = os.path.abspath(os.path.join(ROOT_DIR, dir_name, file_name))
    return file_path_and_name
@pytest.fixture(scope='session')
def browser_settings():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 1000
    browser.config.window_width = 1800

class Gender(Enum):
    Female = 'Female'
    Male = 'Male'
    Other = 'Other'

class Month(Enum):
    January = 0
    February = 1
    March = 2
    April = 3
    May = 4
    June = 5
    July = 6
    August = 7
    September = 8
    October  = 9
    November = 10
    December = 11


@dataclass
class UserData:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    pnone_number: str
    birth_day: int
    birth_month: Month
    birth_year: int
    subjects: list
    hobbies: list
    file_name: str
    address: str
    state: str
    sity: str

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
        browser.element('#uploadPicture').send_keys(resources_path('img', UserData.file_name))
        browser.element('#currentAddress').type(UserData.address)
        browser.element('[id=react-select-3-input]').type(UserData.state).press_enter()
        browser.element('[id=react-select-4-input]').type(UserData.sity).press_enter()

    def form_submit(self):
        browser.element('[id=submit]').press_enter()

    def result_table(self):
        return browser.element('.table-responsive').all('td')



