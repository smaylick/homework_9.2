import pytest
from selene import browser, have

@pytest.fixture
def screen_resolution():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

def test_search_google(screen_resolution): # использую фикстуру в которой задаю разрешение браузеру
    browser.open('https://www.google.ru/?hl=ru')
    browser.element('#APjFqb').click().type('hfisufhwueghwiouuehgwwegwegwageawgwg').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))

