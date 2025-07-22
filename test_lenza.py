import allure
from class_data import Data
import pytest
from time import sleep


dat = Data()


@allure.title("Переход на страницу авторизации / регистрации")
def test_start(ui):
    with allure.step("Страница выбора языка"):
        ui.get(dat.data("url"))


@allure.title("Выбор языка")
@pytest.mark.parametrize('selector, language', [
    (sel, lang) for sel, lang in zip(
        dat.data("selectors_of_languages"),
        dat.data("languages"))])
def test_languages(ui, selector, language):
    with allure.step("Нажатие на селект"):
        ui.click(".lang-switch.btn.with-border.btn--white.btn--inverted")
    with allure.step("Выбор языка в селекте"):
        ui.click(selector)
    with allure.step("Проверка изменения языка"):
        assert ui.text('[contenteditable="false"]') == language


@allure.title("Кнопка Начать")
def test_button_begin(ui):
    with allure.step("Нажатие на кнопку Начать"):
        ui.click(".button-ui.btn.btn--full-width.with-border.btn--lg")


@allure.title("Невалидные адреса электронной почты")
@pytest.mark.parametrize('mail',
                         [("bezsobakitest.com"),
                          ("s probelom@test.com"),
                          ("spec_symbols?,@test.com")])
def test_invalid_email_input(ui, mail):
    with allure.step("Ввод невалидного E-mail"):
        ui.input('[type="email"]', mail)
    with allure.step("Нажатие на кнопку Продолжить"):
        ui.click(".btn.btn--full-width.with-border.btn--lg")
    with allure.step("Проверка отображения аллерта о неверном адресе электронной почты"):
        assert ui.textx('/html/body/div[1]/div/div/div/div[2]/div/div/p') == 'Неверный адрес электронной почты. Повторите попытку.'
    with allure.step("Очистка поля с помощью кнопки"):
        ui.click(".form-item__icon.form-item__icon--dark")


@allure.title("Валидный адрес электронной почты")
def test_valid_email_input(ui):
    with allure.step("Ввод валидного E-mail"):
        ui.input('[type="email"]', ui.random_string(10) + "@test.com")
    with allure.step("Нажатие на кнопку 'Продолжить'"):
        ui.click(".btn.btn--full-width.with-border.btn--lg")
    with allure.step("Проверка перехода к подтверждению почты"):
        assert ui.text("#root > div > div > div > div.hdi_container.hdi_container_center.cd_code_heading > h2") == 'Проверьте почту'


@allure.title("Переход назад из подтверждения почты")
def test_mail_check_goback(ui):
    with allure.step("Нажатие кнопки 'На главную'"):
        ui.click(".btn_back")
    with allure.step("Проверка возврата к предыдущей форме"):
        assert ui.text(".hdi_title") == 'Добро пожаловать в Lenza!'


@allure.title("Невалидное подтверждение почты")
def test_mail_invalid(ui):
    with allure.step("Ввод валидного E-mail"):
        ui.input('[type="email"]', ui.random_string(10) + "@test.com")
    with allure.step("Нажатие на кнопку 'Продолжить'"):
        ui.click(".btn.btn--full-width.with-border.btn--lg")
    with allure.step("Ввод невалидного кода подтверждения"):
        ui.input("#root > div > div > div > div.cd_code__bottom > fieldset > label:nth-child(1) > input", "6")
        ui.input("#root > div > div > div > div.cd_code__bottom > fieldset > label:nth-child(2) > input", "6")
        ui.input("#root > div > div > div > div.cd_code__bottom > fieldset > label:nth-child(3) > input", "6")
        ui.input("#root > div > div > div > div.cd_code__bottom > fieldset > label:nth-child(4) > input", "5")
        ui.input("#root > div > div > div > div.cd_code__bottom > fieldset > label:nth-child(5) > input", "5")
        ui.input("#root > div > div > div > div.cd_code__bottom > fieldset > label:nth-child(6) > input", "0")
    with allure.step("Проверка отображения аллерта о неправильном коде"):
        assert ui.text("#root > div > div > div > div.cd_code__bottom > p") == 'Код введен неправильно'


@allure.title("Валидное подтверждение почты")
def test_mail_valid(ui):
    with allure.step("Ввод валидного кода подтверждения"):
        ui.input("#root > div > div > div > div.cd_code__bottom > fieldset > label:nth-child(1) > input", "6")
        ui.input("#root > div > div > div > div.cd_code__bottom > fieldset > label:nth-child(2) > input", "6")
        ui.input("#root > div > div > div > div.cd_code__bottom > fieldset > label:nth-child(3) > input", "6")
        ui.input("#root > div > div > div > div.cd_code__bottom > fieldset > label:nth-child(4) > input", "5")
        ui.input("#root > div > div > div > div.cd_code__bottom > fieldset > label:nth-child(5) > input", "5")
        ui.input("#root > div > div > div > div.cd_code__bottom > fieldset > label:nth-child(6) > input", "5")
    with allure.step("Проверка успешного перехода к следующей форме"):
        assert ui.text("#root > div > div > div > div.hdi_container.hdi_container_center.ns_title > h2") == 'Похоже, вы еще не используете Lenza'


@allure.title("Переход к созданию рабочего пространства")
def test_go_to_create_new_workspace(ui):
    with allure.step("Нажатие на кнопку 'Создать новое рабочее пространство'"):
        ui.click(".ns_create_new_ws.ns_create_new_ws_web.list-item.no-select")
    with allure.step("Проверка успешного перехода к следующей форме 'Создание рабочего пространства'"):
        assert ui.text(".hdi_title") == "Укажите имя рабочего пространства"


@allure.title("Невалидное название рабочего пространства")
def test_invalid_new_workspace(ui):
    with allure.step("Ввод невалидного названия рабочего пространства на кириллице"):
        ui.input("input", "кириллица")
    with allure.step("Проверка отображения аллерта о невалидном названии рабочего пространства"):
        assert ui.text(".form-field__error.no-select") == "Разрешены латинские буквы и символы aA-zZ, 0-9, -, _"


@allure.title("Переход назад из формы создания рабочего пространства")
def test_new_workspace_goback(ui):
    with allure.step("Нажатие на кнопку 'Назад'"):
        ui.click(".d_domain__back-link")
    with allure.step("Проверка успешного перехода к предыдущей форме"):
        assert ui.text(".hdi_title.hdi_title_nodescription") == "Похоже, вы еще не используете Lenza"


@allure.title("Валидное название рабочего пространства")
def test_valid_new_workspace(ui):
    with allure.step("Нажатие на кнопку 'Создать новое рабочее пространство"):
        ui.click(".ns_create_new_ws.ns_create_new_ws_web.list-item.no-select")
    with allure.step("Ввод валидного названия рабочего пространства"):
        ui.input("input", ui.random_string(10))
    with allure.step("Нажатие на кнопку 'Продолжить'"):
        ui.click('[type="button"]')
    with allure.step("Проверка успешного перехода к следующей форме 'Настройка личного профиля'"):
        assert ui.text(".hdi_title.hdi_title_nodescription") == "Настройка личного профиля"


@allure.title("Загрузка изображения невалидного формата")
def test_add_invalid_image(ui):
    with allure.step("Загрузка изображения формата 'ico'"):
        assert ui.add_image("invalid_image.ico") is False, 'Система принимает изображения в формате ico (отсутствует ошибка)'


@allure.title("Загрузка изображения валидного формата")
def test_add_valid_image(ui):
    with allure.step("Загрузка изображения формата 'png'"):
        assert ui.add_image("black.png") is True


@allure.title("Кнопка 'Продолжить' забизейблена")
def test_disabled_button_name(ui):
    with allure.step("Проверка: Кнопка продолжть в состоянии 'Disabled'"):
        assert ui.state_element('[type="button"]') is False


@allure.title("Имя")
def test_input_name(ui):
    with allure.step("Ввод валидного имени"):
        ui.input('[placeholder="Введите имя"]', dat.data("name"))
    with allure.step("Проверка фиксации в поле введённого имени"):
        assert ui.attribute_element('[placeholder="Введите имя"]', "value"
                                    ) == dat.data("name")


@allure.title("Фамилия")
def test_input_surname(ui):
    with allure.step("Ввод валидной фамилии"):
        ui.input('[placeholder="Введите фамилию"]', dat.data("surname"))
    with allure.step("Проверка фиксации в поле введённой фамилии"):
        assert ui.attribute_element('[placeholder="Введите фамилию"]', "value"
                                    ) == dat.data("surname")


@allure.title("Кнопка 'Продолжить' доступна")
def test_enabled_button_name(ui):
    with allure.step("Проверка перехода кнопки 'Продолжить' из состояния 'Disabled' в состояние 'Enabled'"):
        assert ui.state_element('[type="button"]') is True
    with allure.step("Нажатие на кнопку 'Продолжить'"):
        ui.click('[type="button"]')


@allure.title("Кнопка 'Продолжить' интерактивна")
def test_enabled_button_birth(ui):
    with allure.step("Проверка: Кнопка 'Продолжить' изначально в состоянии 'Enabled'"):
        assert ui.state_element('[type="button"]') is True


@allure.title("День рождения")
def test_birth_day(ui):
    with allure.step("Нажатие на селект 'День'"):
        ui.click(
            '#root > div > div > div > div.pr_profile__wrapper > div.pr_profile__top > div > div > div > div:nth-child(1) > label > span > input[type=text]')
    with allure.step("Выбор дня рождения в селекте"):
        ui.click('.data-index-28.list-item-component.list-item.list-item--xsm.no-select')
    with allure.step("Проверка выбранной фиксации значения в поле 'День'"):
        assert ui.attribute_element(
            '#root > div > div > div > div.pr_profile__wrapper > div.pr_profile__top > div > div > div > div:nth-child(1) > label > span > input[type=text]', "value"
                                    ) == dat.data("birth_day")


@allure.title("Месяц рождения")
def test_birth_month(ui):
    with allure.step("Нажатие на селект 'Месяц'"):
        ui.click(
            '#root > div > div > div > div.pr_profile__wrapper > div.pr_profile__top > div > div > div > div.middle-day.form-field.select.no-select > label > span > input[type=text]')
    with allure.step("Выбор месяца рождения в селекте"):
        ui.click('.select-option-active.data-index-0.list-item-component.list-item.list-item--xsm.no-select')
    with allure.step("Проверка выбранной фиксации значения в поле 'Месяц'"):
        assert ui.attribute_element(
            '#root > div > div > div > div.pr_profile__wrapper > div.pr_profile__top > div > div > div > div.middle-day.form-field.select.no-select > label > span > input[type=text]', "value"
                                    ) == dat.data("birth_month")


@allure.title("Год рождения")
def test_birth_year(ui):
    with allure.step("Нажатие на селект 'Год'"):
        ui.click(
            '#root > div > div > div > div.pr_profile__wrapper > div.pr_profile__top > div > div > div > div:nth-child(3) > label > span > input[type=text]')
    with allure.step("Выбор года рождения в селекте"):
        ui.click(
            '.data-index-85.list-item-component.list-item.list-item--xsm.no-select'
            )
    with allure.step("Проверка выбранной фиксации значения в поле 'Год'"):
        assert ui.attribute_element(
            '#root > div > div > div > div.pr_profile__wrapper > div.pr_profile__top > div > div > div > div:nth-child(3) > label > span > input[type=text]', "value"
                                    ) == dat.data("birth_year")
    with allure.step("Нажатие на кнопку 'Продолжить'"):
        ui.click('[type="button"]')


@allure.title("Удаление невалидного E-mail из поля приглашения с помощью элемента в тексте")
def test_delete_email_with_inscription(ui):
    with allure.step("Ввод невалидного адреса электронной почты с кириллицей"):
        ui.input('#tags-row-input', 'кириллица')
    with allure.step("Нажатие на кнопку 'Отправить'"):
        ui.click('[type="button"]')
    with allure.step("Нажатие на 'Удалить элементы с ошибкой'"):
        ui.click(
            '#root > div > div > div > div.inu_invite__wrapper > div.invite-users-in-company-component > div > div.layout.layout-gap-md.layout-row.layout-align-center.layout--justify-content-left > p > span > span')
    with allure.step("Проверка очистки текстового поля ввода"):
        assert ui.attribute_element(
            '#tags-row-input', "value") == ""


@allure.title("Удаление невалидного E-mail из поля приглашения с помощью кнопки в поле ввода")
def test_delete_email_with_cross(ui):
    with allure.step("Ввод невалидного адреса электронной почты с кириллицей"):
        ui.input('#tags-row-input', 'кириллица')
    with allure.step("Нажатие на кнопку 'Отправить'"):
        ui.click('[type="button"]')
    with allure.step("Нажатие на кнопку очистки поля"):
        ui.click(
            '#root > div > div > div > div.inu_invite__wrapper > div.invite-users-in-company-component > div > div.layout.layout-gap-none.layout-row.layout-column.layout-align-center.chats-tags__container > div > div > div.tags-row-tag.tags-row-tag__error.order-1.tag.no-select.tag--lg.common > button')
    with allure.step("Проверка очистки текстового поля ввода"):
        assert ui.attribute_element(
            '#tags-row-input', "value") == ""


@allure.title("Копировать ссылку для приглашения участников")
def test_copy_link(ui):
    with allure.step("Нажатие на кнопку 'Копировать ссылку'"):
        ui.click('#root > div > div > div > div.inu_invite__wrapper > div.cp_wrapper > p')
    with allure.step("Отображение попапа с текстом об успешном копировании ссылки"):
        assert ui.text('div.cp_popup') == 'Ссылка скопирована. Теперь вы можете поделиться ей и с другими!'


@allure.title("Отправка приглашения")
def test_send_invite(ui):
    with allure.step("Ввод валидного E-mail для приглашения"):
        ui.input('#tags-row-input', 'test@test.com')
    with allure.step("Нажатие 'Enter'"):
        ui.input_key_enter('#tags-row-input')
    with allure.step("Нажатие на кнопку 'Отправить'"):
        ui.click('.inu_invite__buttons_send.btn.btn--full-width.with-border.btn--lg.no-select')
    with allure.step("Проверка успешной отправки приглашения и перехода к следующей форме 'Приглашение отправлено'"):
        assert ui.text(
            '.ui-btn__title.mobile-select-none') == "Готово"


@allure.title("Приглашение участников позже")
def test_invite_later(ui):
    global name_workspace
    global email
    name_workspace = ui.random_string(10)
    email = ui.random_string(10) + "@test.com"
    with allure.step("Обновление страницы"):
        ui.refresh()
    with allure.step("Нажатие на кнопку 'Начать'"):
        ui.click(".button-ui.btn.btn--full-width.with-border.btn--lg")
    with allure.step("Ввод валидного E-mail"):
        ui.input('[type="email"]', email)
    with allure.step("Нажатие на кнопку 'Продолжить'"):
        ui.click(".btn.btn--full-width.with-border.btn--lg")
    with allure.step("Ввод валидного кода подтверждения электронной почты"):
        ui.input("#root > div > div > div > div.cd_code__bottom > fieldset > label:nth-child(1) > input", "6")
        ui.input("#root > div > div > div > div.cd_code__bottom > fieldset > label:nth-child(2) > input", "6")
        ui.input("#root > div > div > div > div.cd_code__bottom > fieldset > label:nth-child(3) > input", "6")
        ui.input("#root > div > div > div > div.cd_code__bottom > fieldset > label:nth-child(4) > input", "5")
        ui.input("#root > div > div > div > div.cd_code__bottom > fieldset > label:nth-child(5) > input", "5")
        ui.input("#root > div > div > div > div.cd_code__bottom > fieldset > label:nth-child(6) > input", "5")
    with allure.step("Нажатие на кнопку 'Создать новое рабочее пространство'"):
        ui.click(".ns_create_new_ws.ns_create_new_ws_web.list-item.no-select")
    with allure.step("Ввод имени рабочего пространства"):
        ui.input("input", name_workspace)
    with allure.step("Нажатие на кнопку 'Продолжить'"):
        ui.click('[type="button"]')
    with allure.step("Ввод валидного имени"):
        ui.input('[placeholder="Введите имя"]', dat.data("name"))
    with allure.step("Ввод валидной фамилии"):
        ui.input('[placeholder="Введите фамилию"]', dat.data("surname"))
    with allure.step("Нажатие на кнопку 'Продолжить'"):
        ui.click('[type="button"]')
    with allure.step("Нажатие на селект 'День'"):
        ui.click(
            '#root > div > div > div > div.pr_profile__wrapper > div.pr_profile__top > div > div > div > div:nth-child(1) > label > span > input[type=text]')
    with allure.step("Выбор дня рождения в селекте 'День'"):
        ui.click('.data-index-28.list-item-component.list-item.list-item--xsm.no-select')
    with allure.step("Нажатие на селект 'Месяц'"):
        ui.click(
            '#root > div > div > div > div.pr_profile__wrapper > div.pr_profile__top > div > div > div > div.middle-day.form-field.select.no-select > label > span > input[type=text]')
    with allure.step("Выбор месяца рождения в селекте 'Месяц'"):
        ui.click('.select-option-active.data-index-0.list-item-component.list-item.list-item--xsm.no-select')
    with allure.step("Нажатие на селект 'Год'"):
        ui.click(
            '#root > div > div > div > div.pr_profile__wrapper > div.pr_profile__top > div > div > div > div:nth-child(3) > label > span > input[type=text]')
    with allure.step("Выбор года рождения в селекте 'Год'"):
        ui.click(
            '.data-index-85.list-item-component.list-item.list-item--xsm.no-select'
            )
    with allure.step("Нажатие на кпонку 'Продолжить'"):
        ui.click('[type="button"]')
    with allure.step("Нажатие на кнопку 'Пригласить позже'"):
        ui.click('.inu_invite__link_skip')
        sleep(2)  # Вынужденное ожидание
    with allure.step("Проверка перехода на страницу 'Моё пространство'"):
        assert ui.current_url() == "https://chat.lenzaos.com/" + name_workspace + "/home"


@allure.title("Проверка имени пользователя")
def test_validation_name(ui):
    with allure.step("Закрытие приветственного попапа"):
        ui.click('#close-view')
    with allure.step("Нажатие на профиль (слева внизу)"):
        ui.click('[data-test-id="chat-off-avatar-item"]')
    with allure.step("Закрытие попапа об улучшении аккаунта"):
        ui.click('.ui-btn.ui-btn-variant-outlined.ui-btn-size-md.ui-btn-color-white.ui-btn-effect-opacity.no-select.ui-btn-radius-8.ui-btn-full-width-text')
    with allure.step("Нажатие на профиль в дропдауне"):
        ui.click('.profile-button__current-account.enable-gif-by-hover.list-item.list-item--lg.no-select')
    with allure.step("Проверка поля 'Имя пользователя' на совпадение с введённым ранее значением при регистрации"):
        assert ui.textx('/html/body/div[5]/div/div/div[2]/div[3]/div[2]/div[1]/div/div[1]/div/span') == name_workspace, "Имя пользователя не совпадает с заданным при регистрации"


@allure.title("Проверка электронной почты")
def test_validation_email(ui):
    with allure.step("Проверка поля 'Электронная почта' на совпадение с введённым ранее значением при регистрации"):
        assert ui.textx('/html/body/div[5]/div/div/div[2]/div[3]/div[2]/div[2]/div/div[1]/div/span') == email


@allure.title("Проверка даты рождения")
def test_validation_birthday(ui):
    with allure.step("Переход в таб 'О себе'"):
        ui.click('[data-index="1"][data-id="1"]')
    with allure.step("Проверка поля 'Дата рождения' на совпадение с введённым ранее значением при регистрации"):
        assert ui.textx('/html/body/div[5]/div/div/div[2]/div[3]/div[3]/div/div/div[1]/div/span') == dat.data("birth_date")
