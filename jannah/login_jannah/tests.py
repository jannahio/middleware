# login_jannah/tests.py
from channels.testing import ChannelsLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class LoginWithGoogleConsumerTests(ChannelsLiveServerTestCase):
    serve_static = True  # emulate StaticLiveServerTestCase

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        try:
            # NOTE: Requires "chromedriver" binary to be installed in $PATH
            cls.driver = webdriver.Chrome()
        except:
            super().tearDownClass()
            raise

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_when_workflow_message_posted_then_seen_by_everyone_in_same_workflow(self):
        try:
            self._enter_workflow("login_with_google_1")

            self._open_new_window()
            self._enter_workflow("login_with_google_1")

            self._switch_to_window(0)
            self._post_message("hello")
            WebDriverWait(self.driver, 2).until(
                lambda _: "hello" in self._workflow_log_value,
                "Message was not received by window 1 from window 1",
            )
            self._switch_to_window(1)
            WebDriverWait(self.driver, 2).until(
                lambda _: "hello" in self._workflow_log_value,
                "Message was not received by window 2 from window 1",
            )
        finally:
            self._close_all_new_windows()

    def test_when_workflow_message_posted_then_not_seen_by_anyone_in_different_workflow(self):
        try:
            self._enter_workflow("login_with_google_1")

            self._open_new_window()
            self._enter_workflow("login_with_google_2")

            self._switch_to_window(0)
            self._post_message("hello")
            WebDriverWait(self.driver, 2).until(
                lambda _: "hello" in self._workflow_log_value,
                "Message was not received by window 1 from window 1",
            )

            self._switch_to_window(1)
            self._post_message("world")
            WebDriverWait(self.driver, 2).until(
                lambda _: "world" in self._workflow_log_value,
                "Message was not received by window 2 from window 2",
            )
            self.assertTrue(
                "hello" not in self._workflow_log_value,
                "Message was improperly received by window 2 from window 1",
                )
        finally:
            self._close_all_new_windows()

    # === Utility ===

    def _enter_workflow(self, workflow_name):
        self.driver.get(self.live_server_url + "/login/")
        ActionChains(self.driver).send_keys(workflow_name, Keys.ENTER).perform()
        WebDriverWait(self.driver, 2).until(
            lambda _: workflow_name in self.driver.current_url
        )

    def _open_new_window(self):
        self.driver.execute_script('window.open("about:blank", "_blank");')
        self._switch_to_window(-1)

    def _close_all_new_windows(self):
        while len(self.driver.window_handles) > 1:
            self._switch_to_window(-1)
            self.driver.execute_script("window.close();")
        if len(self.driver.window_handles) == 1:
            self._switch_to_window(0)

    def _switch_to_window(self, window_index):
        self.driver.switch_to.window(self.driver.window_handles[window_index])

    def _post_message(self, message):
        ActionChains(self.driver).send_keys(message, Keys.ENTER).perform()

    @property
    def _workflow_log_value(self):
        return self.driver.find_element(
            by=By.CSS_SELECTOR, value="#with-google-log"
        ).get_property("value")