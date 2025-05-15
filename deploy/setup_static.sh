#!/bin/bash

# Перейти в корневую директорию проекта
cd "$(dirname "$0")/.."

# Собрать статические файлы
python manage.py collectstatic --noinput

# Создать символические ссылки
cd static/
ln -sf admin/jazzmin jazzmin
ln -sf admin/vendor vendor

echo "Статические файлы настроены успешно!"
