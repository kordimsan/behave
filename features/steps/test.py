# -*- coding: utf-8 -*-
from behave import *
from pywinauto import application, findwindows, keyboard, element_info
import time

class TextNotFound(Exception):
    pass

#Откроем главную страницу. Передадим в качестве аргумента адрес страницы.
@given('Запущена программа "{app_name}"')
def step(context, app_name):
    context.app = application.Application()
    context.app.start(app_name)

#Теперь пишем текст
@then("Пишем текст '{text}'")
def step(context, text):
    context.app['Notepad'].wait('ready')
    context.app['Notepad']['Edit'].set_edit_text(text)

#Проверка написанного текста
@then("Проверка текста '{text}'")
def step(context, text):
    texts = context.app['Notepad']['Edit'].texts()
    if len(texts) == 0:
        raise TextNotFound(f'Текст: {text} не найден')
    if not context.app['Notepad']['Edit'].texts()[0] == text:
        raise TextNotFound(f'Текст: {text} не найден')

#Теперь нажмем на кнопку "Выход" в меню
@then("Выход из файла '{text}'")
def step(context, text):
    context.app['NotepadDialog'].wait('ready')
    context.app['NotepadDialog'].menu_select("&Файл->Выход")

#Теперь нажмем на кнопку "Сохранить" в диалоге
@then("Сохранить файла '{text}' в диалоге")
def step(context, text):
    context.app.Блокнот.wait('ready')
    context.app.Блокнот.Сохранить.close_click()

#Теперь меняем название файла на "Test_File.txt"
@then("Меняем название файла на '{text}'")
def step(context, text):
    context.app.Сохранение.wait('ready')
    context.app.Сохранение.edit1.set_edit_text("Test_File.txt")

#Теперь нажмем на кнопку "Сохранить" в диалоге
@then("Сохранить файла '{text}'")
def step(context, text):
    #time.sleep(2)
    context.app.СохранениеDialog['Со&хранитьButton'].wait('enabled')
    context.app.СохранениеDialog['Со&хранитьButton'].type_keys('{ENTER}')

#Теперь нажмем на кнопку "Подтвердить сохранение"
@then("Подтвердить сохранение '{text}'")
def step(context, text):
    try:
        context.app.Подтвердитьсохранениеввиде.wait('ready')
        context.app.Подтвердитьсохранениеввиде.Да.click()
    except pywinauto.MatchError:
        print('Skip overwriting...')