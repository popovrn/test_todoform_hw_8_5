from selene import browser, be, have, by, command
import os.path

def test_todo_op():
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Roman')
    browser.element('#lastName').should(be.blank).type('Popov')
    browser.element('#userEmail').should(be.blank).type('test_formtodo.ya.ru')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('81234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('January')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('1983')).click()
    browser.element('.react-datepicker__day--010').click()
    browser.element('#submit').perform(command.js.scroll_into_view)
    browser.element('#subjectsInput').type('Theory of programming languages').press_enter()
    browser.element('label[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('foto/foto.jpg'))
    browser.element('#currentAddress').should(be.blank).type('str. Malaya d.10 kv 125')
    browser.element('#state').click().element(by.text('Uttar Pradesh')).click()
    browser.element('#city').click().element(by.text('Agra')).click()
    browser.element('#submit').press_enter()

    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.element('.table-responsive').all('td:nth-of-type(2)').should(have.texts(
        'Roman Popov',
        'test_formtodo.ya.ru',
        'Male',
        '81234567890',
        '1 January,1983',
        'Theory of programming languages',
        'Music',
        'foto.jpg',
        'str. Malaya d.10 kv 125',
        'Uttar Pradesh Agra'
    ))