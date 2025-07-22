import pytest
from class_ui import Ui


@pytest.fixture(scope="session")
def ui():
    ui = Ui()
    yield ui
    ui.browser.quit()
