from selene import have
from registration_page_object.registration_page import RegistrationForm


def test_success_form_send(browser_settings):
    registration_form = RegistrationForm()
    registration_form.open()

    registration_form.user_first_name_fill('tata')
    registration_form.user_last_name_fill('test')
    registration_form.user_email_fill('test@test.ru')
    registration_form.user_gender_select('Female')
    registration_form.user_phone_fill('79999999999')
    registration_form.user_birtday('15', '5', '1985')
    registration_form.user_subject_fill('co', 'ma')
    registration_form.user_hobbies_select('2')
    registration_form.file_select('bradford.jpg')
    registration_form.user_address_fill('тестовый адрес')
    registration_form.user_state_and_sity_select('NCR', 'Delhi')
    registration_form.form_submit()

    registration_form.result_table().should(have.texts('Student Name', 'tata test',
                                                       'Student Email', 'test@test.ru',
                                                       'Gender', 'Female',
                                                       'Mobile', '7999999999',
                                                       'Date of Birth', '15 June,1985',
                                                       'Subjects', 'Computer Science, Maths',
                                                       'Hobbies', 'Reading',
                                                       'Picture', 'bradford.jpg',
                                                       'Address', 'тестовый адрес',
                                                       'State and City', 'NCR Delhi'))

