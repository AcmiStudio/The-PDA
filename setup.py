import os
import sys
import platform as pf
print("Приветствую! Вы находитесь в режиме установки эмулятора КПК.\nИдет установка необходимых пакетов...")

command = input("Запустить установку для Termux? (y/n): ").lower()
command_install = ["pkg update && pkg upgrade", "pkg install python3", "pkg install python-pip"]
if command == "y":
    if pf.system() == "Linux":
        print("Установка необходимых пакетов на Termux...")
        for i in command_install:
            os.system(i)
            pass
        print("Все успешно установилось!")
        
        print("Установка завершена!")
    elif pf.system() == "Windows":
        print("Установка на систему Windows 10-11, x64, x86 недоступна в ранних версиях программы!")
        input()
    else:
        print("До свидание!")
        sys.exit(1)