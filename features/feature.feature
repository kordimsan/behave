Feature: Проверка стандартного блокнота
Scenario: Открытие файла и запись текста
  Given Запущена программа "notepad.exe"
  Then Пишем текст 'blablabla'
  Then Выход из файла '&Файл->Выход'
  Then Сохранить файла 'Сохранить' в диалоге
  Then Меняем название файла на 'Test_File.txt'
  Then Сохранить файла 'Сохранение'
  Then Подтвердить сохранение 'Подтвердитьсохранениеввиде'