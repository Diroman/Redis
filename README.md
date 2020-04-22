#Инструкция по запуску

###Linux
1) В файле config.json указать host и port redis контейнера
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
3) После можно переходить по ссылке http://localhost:5000 и дополнительным url. Примеры:
    * http://localhost:5000/home
    * http://localhost:5000/one
    * http://localhost:5000/two
    * http://localhost:5000/four
4) По ссылке http://localhost:5000/logs доступна таблица с логами

###Windows
Никак))