# Инструкция по запуску

1) В файле config.json указать host и port redis контейнера
### Linux
2) Выполнить команду:
    * Для python2.*:
    ```shell script
       ./setup2.sh
    ```
    * Для python3.*:
   ```shell script
       ./setup3.sh
    ```
   произойдет настройка виртуального окружения и запуск сервера
### Windows
2) Установить необходимые библиотеки из файла requirements.txt
   ```shell script
      pip3 install -r requirements.txt
   ```
3) Запустить файл run.sh в IDE или с помощью команды:
   ```shell script
      python3 run.py
   ```
4) После можно переходить по ссылке http://localhost:5000 и дополнительным url. Примеры:
    * http://localhost:5000/home
    * http://localhost:5000/one
    * http://localhost:5000/two
    * http://localhost:5000/four
5) По ссылке http://localhost:5000/logs доступна таблица с логами
