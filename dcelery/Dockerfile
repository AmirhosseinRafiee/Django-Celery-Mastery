FROM python:3.11.4-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY . /usr/src/app/

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r requirements.txt && \
    chmod +x /usr/src/app/entrypoint.sh && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    chown -R django-user:django-user /usr/src/app/

ENV PATH="/py/bin:$PATH"

USER django-user

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
