FROM python:3.6.8-slim

ENV USER=user UID=1000

RUN mkdir /county-wards
RUN mkdir /county-wards/logs

RUN groupadd -g ${UID} -r ${USER} \
    && useradd -u ${UID} -r -g ${USER} ${USER}

ADD requirements.txt /county-wards

WORKDIR /county-wards

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY app /county-wards/app
COPY settings.py /county-wards/settings.py
COPY entrypoint.sh /county-wards/entrypoint.sh
COPY wsgi.py /county-wards/wsgi.py

ENV FLASK_APP=wsgi.py

RUN chmod +x entrypoint.sh

RUN chown -R ${USER}:${USER} /county-wards/logs

EXPOSE 8004

USER ${USER}

CMD ["./entrypoint.sh"]