
def find_element(locator, driver):
    '''

    Args:
        locator: Element locator to look for on the browser.
        driver: Driver on which the element visibility to be validated.
        time_out: Timeout user can pass in a value or defaults to 30 secs.
        log_exception: Log the exception or return None.
        poll: Poll frequency.

    Returns:

    '''
    return driver.find_element(*locator)