from selene import browser
from selene.support.conditions import be, have


def test_positive(browser_set):

    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in'))

def test_negative(browser_set):

    browser.element('[name="q"]').should(be.blank).type('ghsdjhouhgohjsdkljhssl;gjzhs;zlighuuhn;ln;jn').press_enter()
    browser.element('[class="s6JM6d"]').should(have.text('ghsdjhouhgohjsdkljhssl;gjzhs;zlighuuhn;ln;jn'))