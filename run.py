# -*- coding: utf-8 -*-
from behave import *
from pywinauto import application, findwindows, keyboard, element_info
import time

app = application.Application()
app.start(r"notepad.exe")

app['Notepad'].wait('ready')
app['Notepad']['Edit'].set_edit_text("blablabla")

app['NotepadDialog'].wait('ready')
app['NotepadDialog'].menu_select("&Файл->Выход")

app.Блокнот.wait('ready')
app.Блокнот.Сохранить.close_click()

app.Сохранение.wait('ready')
app.Сохранение.edit1.set_edit_text("Test_File.txt")

time.sleep(2)
app.Сохранение.Сохранить.wait('enabled')
app.Сохранение.Сохранить.click()

try:
    app.Подтвердитьсохранениеввиде.wait('ready')
    app.Подтвердитьсохранениеввиде.Да.click()
except pywinauto.MatchError:
    print('Skip overwriting...')