import pytest
from pages.home_page import HomePage
from pages.result_page import ResultPage


class TestValidate:
    def test_valid_input(self,driver):
        driver.get("https://agrichain.com/qa/input")

        home = HomePage(driver)
        home.enter_string("abcabcbb")
        home.click_submit()

        result = ResultPage(driver)
        output = result.get_output()

        try:
            assert output == "3"
        except AssertionError:
            driver.save_screenshot(".\\screenShots\\output_mismatch.png")
            print(f"Test failed — screenshot saved at screenshot Directory")
            raise
        finally:
            driver.quit()

