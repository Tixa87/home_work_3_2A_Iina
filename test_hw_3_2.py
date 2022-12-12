from selene.support.shared import browser
from selene import be, have


def test_positive(browser_set):
    browser.element('[name="q"]').should(be.blank).type('selene github').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in'))


def test_negative(browser_set):
    browser.element('[name="q"]').should(be.blank).type('ghsdjhouhgohjsdkljhssl;gjzhs;zlighuuhn;ln;jn').press_enter()
    browser.element('[class="card-section"]').should(have.text('No results containing all your search terms were found.'))
