from selene import browser, be, have
import pytest


def test_first():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('fgdfsgsdfgsfdgsfd1111').press_enter()
    browser.element('[id="botstuff"]').should(be.not_.visible)


def test_second():
    browser.open('https://ya.ru')
    browser.element('[name="text"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('.OrganicTitle ').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))
