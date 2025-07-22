from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
from time import sleep
import random
import string


class Ui:
    def __init__(self) -> None:
        self.browser = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))
        self.browser.maximize_window()

    def get(self, URL: str) -> None:
        """
        Переход на указанную страницу
        """
        self.browser.get(URL)

    def current_url(self):
        """
        Возвращает адрес текущей страницы
        """
        return self.browser.current_url

    def random_string(self, length=8) -> str:
        """
        Генерирует и возвращает случайное значение заданной длины,
        состоящее из строчной латиницы
        """
        return ''.join(random.choices(string.ascii_lowercase, k=length))

    def cookies(self, cookie: dict[str, any]) -> None:
        """
        Добавление всех куки из списка с помощью цикла
        """
        self.browser.add_cookie(cookie)

    def refresh(self) -> None:
        """
        Обновление текущей страницы
        """
        self.browser.refresh()

    def back(self) -> None:
        """
        Переход на страницу назад
        """
        self.browser.back()

    def click(self, selector: str) -> None:
        """
        Ожидание отображения элемента с указанным CSS-селектором,
        скролл до него и нажатие на него
        """
        try:
            WebDriverWait(self.browser, 2).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, selector)))
        except Exception:
            WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, selector)))
        self.browser.execute_script("arguments[0].scrollIntoView();",
                                    self.browser.find_element(By.CSS_SELECTOR,
                                                              selector))
        self.browser.find_element(By.CSS_SELECTOR, selector).click()

    def clickx(self, path: str) -> None:
        """
        Ожидание отображения элемента с указанным XPath,
        скролл до него и нажатие на него
        """
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            (By.XPATH, path)))
        self.browser.execute_script("arguments[0].scrollIntoView();",
                                    self.browser.find_element(By.XPATH,
                                                              path))
        self.browser.find_element(By.XPATH, path).click()

    def input(self, selector: str, text: str) -> None:
        """
        Ожидание отображения элемента с указанным CSS-селектором,
        скролл до него и ввод в него указанного текста
        """
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, selector)))
        self.browser.execute_script("arguments[0].scrollIntoView();",
                                    self.browser.find_element(By.CSS_SELECTOR,
                                                              selector))
        self.browser.find_element(By.CSS_SELECTOR, selector).send_keys(text)

    def inputx(self, path: str, text: str) -> None:
        """
        Ожидание отображения элемента с указанным XPath,
        скролл до него и ввод в него указанного текста
        """
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            (By.XPATH, path)))
        self.browser.execute_script("arguments[0].scrollIntoView();",
                                    self.browser.find_element(By.XPATH,
                                                              path))
        self.browser.find_element(By.XPATH, path).send_keys(text)

    def hover(self, selector: str) -> None:
        """
        Ожидание отображения элемента с указанным CSS-селектором,
        скролл до него и наведение курсора на него
        """
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, selector)))
        self.browser.execute_script("arguments[0].scrollIntoView();",
                                    self.browser.find_element(By.CSS_SELECTOR,
                                                              selector))
        ActionChains(self.browser).move_to_element(
                self.browser.find_element(By.CSS_SELECTOR,
                                          selector)).perform()

    def hoverx(self, path: str) -> None:
        """
        Ожидание отображения элемента с указанным CSS-селектором,
        скролл до него и наведение курсора на него
        """
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            (By.XPATH, path)))
        self.browser.execute_script("arguments[0].scrollIntoView();",
                                    self.browser.find_element(By.XPATH,
                                                              path))
        ActionChains(self.browser).move_to_element(
                self.browser.find_element(By.XPATH,
                                          path)).perform()

    def dnd(self, selector_element: str, selector_place: str) -> None:
        """
        Ожидание отображения перемещаемого элемента с указанным CSS-селектором,
        ожидание отображения элемента-места с указанным CSS-селектором,
        скролл до элемента-места и перемещение элемента
        """
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, selector_element)))
        self.browser.execute_script("arguments[0].scrollIntoView();",
                                    self.browser.find_element(By.CSS_SELECTOR,
                                                              selector_place))
        ActionChains(self.browser).drag_and_drop(self.browser.find_element(
            By.CSS_SELECTOR, selector_element), self.browser.find_element(
                By.CSS_SELECTOR, selector_place)).perform()

    def dndx(self, path_element: str, path_place: str) -> None:
        """
        Ожидание отображения перемещаемого элемента с указанным XPath,
        ожидание отображения элемента-места с указанным XPath,
        скролл до элемента-места и перемещение элемента
        """
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            (By.XPATH, path_element)))
        self.browser.execute_script("arguments[0].scrollIntoView();",
                                    self.browser.find_element(By.XPATH,
                                                              path_element))
        self.browser.execute_script("arguments[0].scrollIntoView();",
                                    self.browser.find_element(By.XPATH,
                                                              path_place))
        ActionChains(self.browser).drag_and_drop(self.browser.find_element(
            By.XPATH, path_element), self.browser.find_element(
                By.XPATH, path_place)).perform()

    def text(self, selector: str) -> str:
        """
        Ожидание отображения элемента с указанным CSS-селектором,
        скролл до него и возвращение текста внутри элемента
        """
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, selector)))
        self.browser.execute_script("arguments[0].scrollIntoView();",
                               self.browser.find_element(By.CSS_SELECTOR,
                                                    selector))
        return self.browser.find_element(By.CSS_SELECTOR, selector).text

    def textx(self, path: str) -> str:
        """
        Ожидание отображения элемента с указанным XPath,
        скролл до него и возвращение текста внутри элемента
        """
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            (By.XPATH, path)))
        self.browser.execute_script("arguments[0].scrollIntoView();",
                                    self.browser.find_element(By.XPATH,
                                                              path))
        return self.browser.find_element(By.XPATH, path).text

    def add_image(self, image: str) -> bool:
        """
        Ожидание появления на странице элемента для загрузки изображения,
        загрузка изображения, ожидание отображения на странице элемента
        с изображением
        """
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.avatar__img-upload.avatar__img-upload--full')))
        path = os.path.abspath(image)
        self.browser.find_element(
            By.CSS_SELECTOR, 'input[type="file"]').send_keys(path)
        sleep(2)  # Вынужденное ожидание
        try:
            WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((
                By.CSS_SELECTOR, 'img.avatar-thumb')))
            return True
        except Exception:
            return False

    def state_element(self, selector: str) -> bool:
        """
        Ожидание момента, когда существующий на странице элемент станет
        кликабельным
        """
        try:
            WebDriverWait(self.browser, 2).until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, selector)))
            return True
        except Exception:
            return False

    def attribute_element(self, selector: str, attribute: str):
        """
        Находит элемент страницы по указанному CSS-селектору и
        возвращает значение указанного атрибута этого элемента
        """
        return self.browser.find_element(By.CSS_SELECTOR, selector
                                         ).get_attribute(attribute)

    def input_key_enter(self, selector: str):
        """
        Имитирует нажатие клавиши Enter на полноразмерной клавиатуре
        """
        self.browser.find_element(By.CSS_SELECTOR, selector).send_keys(
            Keys.ENTER)
