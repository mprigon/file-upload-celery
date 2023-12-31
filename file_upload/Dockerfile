# pull official base image
FROM python:3.11.0

# set work directory
WORKDIR /usr/src/file_upload

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
# sed... удаляет \r в конце каждой строки во всех совпадениях в файле
# unix не ставит этого символа, а Windows - ставит
RUN sed -i 's/\r$//g' /usr/src/file_upload/entrypoint.sh
RUN chmod a+x /usr/src/file_upload/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/file_upload/entrypoint.sh"]
