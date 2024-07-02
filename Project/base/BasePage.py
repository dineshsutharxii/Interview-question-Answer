import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
        pageLength = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight); var ")
        match = False
        while match == False:
            lastCount = pageLength
            time.sleep(2)
            pageLength = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight); var ")
            if lastCount == pageLength:
                match = True
        time.sleep(2)