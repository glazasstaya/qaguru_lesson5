import pytest
from selene import have
import os
from conftets import browser_settings
from page_objects.registration_page_object import RegistrationForm
from data_objects.registrathion_page_data_object import Gender, Month, UserData


def test_success_form_send(browser_settings):

    registration_form = RegistrationForm()

    user = UserData(first_name = 'tata',
                    last_name = 'test',
                    email = 'test@test.ru',
                    gender = Gender.Female.value,
                    pnone_number = '7999999999',
                    birth_day = 11,
                    birth_month = Month.June.value,
                    birth_year = 1985,
                    subjects = ['co', 'ma'],
                    hobbies = [1, 2],
                    file_name ='bradford.jpg',
                    address = 'тестовый адрес',
                    state = 'NCR',
                    sity = 'Delhi'
                    )

    registration_form.open()
    registration_form.form_fill(user)
    registration_form.form_submit()

    registration_form.result_table().should(have.texts('Student Name', 'tata test',
                                                     'Student Email', 'test@test.ru',
                                                     'Gender', 'Female',
                                                     'Mobile', '7999999999',
                                                     'Date of Birth', '11 June,1985',
                                                     'Subjects', 'Computer Science, Maths',
                                                     'Hobbies', 'Reading',
                                                     'Picture', 'bradford.jpg',
                                                     'Address', 'тестовый адрес',
                                                     'State and City', 'NCR Delhi'))
