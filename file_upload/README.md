### Запуск проекта
1. с использованием Docker
в терминале в папке, где файл docker-compose.yml:
docker compose up

2. без Docker - в файле settings.py заменить
CELERY_BROKER_URL
CELERY_RESULT_BACKEND

pip install requirements.txt
в трех терминалах в папке file_upload:

redis-server

celery -A file_upload worker -l INFO

python manage.py runserver

## Задание:
Разработать Django REST API, который позволяет загружать файлы на сервер,
а затем асинхронно обрабатывать их с использованием Celery.

### Требования:
1. Создать Django проект и приложение.
2. Использовать Django REST Framework для создания API.
3. Реализовать модель File, которая будет представлять загруженные
   файлы. Модель должна содержать поля:
     ◦ file: поле типа FileField, используемое для загрузки файла.
     ◦ uploaded_at: поле типа DateTimeField, содержащее дату и
       время загрузки файла.
     ◦ processed: поле типа BooleanField, указывающее, был ли файл обработан.
4. Реализовать сериализатор для модели File.
5. Создать API эндпоинт upload/, который будет принимать POST-запросы
   для загрузки файлов. При загрузке файла необходимо создать объект
   модели File, сохранить файл на сервере и запустить асинхронную задачу
   для обработки файла с использованием Celery. В ответ на успешную
   загрузку файла вернуть статус 201 и сериализованные данные файла.
6. Реализовать Celery задачу для обработки файла. Задача должна быть
   запущена асинхронно и изменять поле processed модели File на True
   после обработки файла.
7. Реализовать API эндпоинт files/, который будет возвращать
   список всех файлов с их данными, включая статус обработки.

### Дополнительные требования:
1. Использовать Docker для развертывания проекта.
2. Реализовать механизм для обработки различных типов файлов
   (например, изображений, текстовых файлов и т.д.).
3. Предусмотреть обработку ошибок и возвращение соответствующих кодов
   статуса и сообщений об ошибках.