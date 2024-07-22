from selene import browser, be, have
import pytest

def test_first():
    browser.open('https://ya.ru')
    browser.element('[name="text"]').should(be.blank).type('olololo').press_enter()
    browser.element('[id="search"]').should(have.text('pumpum'))

def test_second():
    browser.open('https://google.com')