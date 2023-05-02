# Древовидное меню

Древовидное меню, как тестовый проект

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/bogdanpracticum/tree_menu.git
cd tree_menu

### Cоздать и активировать виртуальное окружение:

python -m venv env
source env/bin/activate

### Установить зависимости из файла requirements.txt:

python -m pip install --upgrade pip
pip install -r requirements.txt

### Выполнить миграции:

python manage.py makemigrations
python manage.py migrate 

### Запустить проект:

python manage.py runserver

### Взять меня на работу или стажировку :)