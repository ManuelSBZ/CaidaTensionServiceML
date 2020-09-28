FROM faizanbashir/python-datascience:3.6

ENV APP_HOME=/usr/src/app
WORKDIR ${APP_HOME}

ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYTECODE 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN addgroup -S app && adduser --home /usr/src/app --shell /bin/bash -S app -G app

COPY requirements.txt $APP_HOME
RUN pip install --upgrade pip
ENV INSTALL_ON_LINUX=1
RUN pip install -r requirements.txt
RUN python -m pip install djangorestframework
RUN pip install whitenoise

COPY . $APP_HOME
RUN chown -R app:app $APP_HOME
USER app:app

CMD [ "gunicorn" ,"Modelo_Caida_Tension_APIRest.wsgi:application", "--bind", "0.0.0.0:8000", "--workers=4" ]