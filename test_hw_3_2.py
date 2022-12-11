from selene.support.shared import browser
from selene import be, have


def test_positive(browser_set):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in'))


def test_negative(browser_set):
    browser.element('[name="q"]').should(be.blank).type('ghsdjhouhgohjsdkljhssl;gjzhs;zlighuuhn;ln;jn').press_enter()
    browser.element('[class="s6JM6d"]').should(have.text('test_should_fail'))
