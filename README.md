# Where_to_go

Этот проект показывает интересные места по миру с помощью яндекс афиши.

[Пример работающего сайт](https://karmirotter.pythonanywhere.com/)
      
## Подготовка к запуску    
Уставновить [Python 3+](https://www.python.org/downloads/)    

Установить, создать и активировать виртуальное окружение.
```
pip3 install virtualenv
python3 -m venv env
source env/bin/activate
```
Установить библиотеки командой.  
```
pip3 install -r requirements.txt  
``` 
     
## Переменные окружения     
Создайте файл ".env" в него надо прописать ваши настройки    
`DEBUG` - режим отладки      
`SECRET_KEY` - секретный ключ    
`ALLOWED_HOSTS` - Список хостов/доменов, для которых может работать текущий сайт.    
     
Пример .env файла    
```
SECRET_KEY=sdkfhsdklfdsJHFdlskhflkASH121Jk@2323dlasjdSKLAjls2323dlasjdSKLAjlssdkfhsdklfdsJHFdlskhflkASH121Jk
DEBUG=false
ALLOWED_HOSTS=webargs,konch,ped
```
## Запуск кода  
```
python3 manage.py runserver
```
## Добавление мест
предусмотрен функционал по добавлению новых мест в формате geojson
```
python3 manage.py load_place http://адрес/файла.json
```
[Данные, которые можете загрузить](https://github.com/devmanorg/where-to-go-places).    
     
Тестовые данные взяты с сайта [KudaGo](https://kudago.com).