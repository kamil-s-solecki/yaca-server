FROM python:3-alpine

WORKDIR /usr/src/app

COPY src/requirements.txt ./

RUN apk update \
       && apk add gcc \
       && apk add libc-dev \
       && apk add postgresql-dev

RUN pip install --no-cache-dir -r requirements.txt

COPY src .

EXPOSE 5000

CMD [ "python", "./manage.py", "start" ]
