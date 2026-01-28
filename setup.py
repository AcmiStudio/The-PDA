
#============================================
# Привет!
# Я работал над этим проектом: 15 часов
#============================================

#Импорт библиотек которые входяти в обычный пакет python
import os
import sys
import platform as pf
import pathlib as pl

#Приветствие для пользователя + глобальные переменные.

print("Приветствую! Вы находитесь в режиме установки эмулятора КПК.\nИдет установка необходимых пакетов...")
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
#Тута будут функции

def install():
    clear()
    com = input("Приветствую! Добро пожаловать в матсер установки PDA-termux. Выберите действие: \n1.Установить ручным путем(Для Опытных пользователей)\n2.Установить в режиме автономности(рекомендуется новичкам)\n3.Выйти из установщика\n>>>")
    if com == "1":
        #Note: Добавь установку ручным способом
        print("Ручная установка еще не реализована")
        return install()
    elif com == "2":
        #Note: Добавь установку автономным способом, само проверка пакетов, нужные pip версии, проверка версии пайтон и тд.
        print("Запуск автономной установки...")
        #===================================
        arhitecture = pf.architecture()
        pythonVer = pf.python_version()
        system = pf.system()
        version = pf.version()
        print("="*50)
        print(f"Архитектура: {arhitecture}\nВерсия Python: {pythonVer}\nСистема: {system}\nВерсия Android: {version}")
        print("="*50)
        print()
        #===================================
        print("Установка необходимых pip-пакетов...")
        os.system("pip install python-time")
        os.system("pip install termcolor")
        os.system("echo Установка завершена")
        #===================================
        import time
        time.sleep(1)
        #===================================
        print("Поздравляю пользователь, установка нужных пакетов была завершена! \nШаг 2: Выдадим нужные права, нажмите принять, это очень нужно!")
        os.system("echo Выдача прав...")
        os.sleep(2)
        os.system("termux-setup-storage")
        os.sleep(1)
        os.system("echo Выдача прав завершена")
        time.sleep(1)
        print("В будущем нужно выбрать зелкала для установки пакетов, но это можно сделать чуть позже,\nИнструкцию можно посмотреть у меня на страничке,\nссылка будет в конце установки программы.")
        time.sleep(1)
        print("Молодцы, теперь нужно проверить все файлы системы и создать нужные папки для сохранения данных!")
        time.sleep(1)
        if os.path.exists("root"):
            print("Папка root уже существует")
        else:
            print("Папки root не существует, создаем...")
            os.mkdir("root")
        time.sleep(1)
        if os.path.exists("root/users"):
            print("Папка users уже существует")
        else:
            print("Папки users не существует, создаем...")
            os.mkdir("root/users")
        time.sleep(1)  
        if os.path.exists("root/APP"):
            print("Папка APP уже существует")
        else:
            print("Папки APP не существует, создаем...")
            os.mkdir("root/APP")
        time.sleep(1)
        if os.path.exists("root/APP/games"):
            print("Папка games уже существует")
        else:
            print("Папки games не существует, создаем...")
            os.mkdir("root/APP/games")
        time.sleep(1)
        if os.path.exists("root/documents"):
            print("Папка documents уже существует")
        else:
            print("Папки documents не существует, создаем...")
            os.mkdir("root/documents")
        time.sleep(1)
        if os.path.exists("root/APP/programs"):
            print("Папка programs уже существует")
        else:
            print("Папки programs не существует, создаем...")
            os.mkdir("root/APP/programs")
        time.sleep(1)
        if os.path.exists("root/downloads"):
            print("Папка games уже существует")
        else:
            print("Папки games не существует, создаем...")
            os.mkdir("root/APP/programs/games")
        time.sleep(1)
        print("callibrated...")
        time.sleep(5)
        clear()
        print("Установка завершена!")
        time.sleep(1)
        print("Внимание! Вам пришло сообщение от разработчика! Отказаться нельзя.")
        time.sleep(1)
        print()
        print("=" * 50)
        print("Приветствую Друг! Я создал эту программу для termux чтоб можно было повесилиться!\nНо я понимаю пользователей которые вообще не знакомы с Linux.\nНо не беда, программа вам будет четко объяснять и помогать.\nТак же если вам не удобно запускать программы через терминал -\nто вы можете прочитать гайдына оффициальной странице проекта.\nОбновления будут выходить старательно по выходным,\nхорошо вам развлечься и успехов вам!")
        print("Сайт: https://github.com/AcmiStudio/THE-PDA")
        print("=" * 50)
        time.sleep(1)
        print("Автоматический запуск программы...")
        os.system("python3 PDA/main.py")
        
    elif com == "3":
        print("До свидание")
        sys.exit(0)
    else:
        print("Неизвестная команда")
        return install()
#Запускается установка

try:
    command = input("Запустить установку для Termux? (да/нет): ").lower()
    
    command_install = ["pkg update && pkg upgrade", "pkg install python3", "pkg install python-pip", "pkg install vim && pkg install nano"] #Список нужных для установки команд и обновление пакетов
    if command == "y" or command == "да" or command == "yes" or command == "д":
        if pf.system() == "Linux": # Ранняя быстрая проверка устройства для установки.
            print("Установка необходимых пакетов на Termux...")
            for i in command_install: #Цикл для установки пакетов
                os.system(i)
            
            print("Все успешно установилось!")
            install()
            print("Установка завершена!")
        elif pf.system() == "Windows": # Ранняя быстрая проверка устройства для установки. говорит что нельзя скачивать на Win, пока что.
            print("Установка на систему Windows 10-11, x64, x86 недоступна в ранних версиях программы!")
            input("Нажмите Ввод для выхода...")
        else:
            print("До свидание!") # при выборе (n) или случайно нажатой клавиши закрываеться программа
            sys.exit(1)
    else:
        print("Установка отменена пользователем")
        sys.exit(0)
except KeyboardInterrupt:
    print("\nУстановка прервана пользователем")
    sys.exit(0)
except Exception as e:
    print(f"Простите! Произошла ошибка: {e}")
    sys.exit(1)
