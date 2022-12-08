FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get install -y curl

ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH:/root/.local/bin"

RUN curl -SL https://install.python-poetry.org | python -
RUN pip install -U pip wheel

WORKDIR /code

COPY pyproject.toml /code/pyproject.toml
COPY poetry.lock /code/poetry.lock

RUN /bin/bash -c "poetry install --without dev"

COPY . /code

RUN python setup.py install

ENTRYPOINT ["quick_word"]
