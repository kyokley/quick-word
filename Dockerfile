ARG BASE_IMAGE=python:3.12-slim
FROM ${BASE_IMAGE} AS base
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=.
ENV UV_LINK_MODE=copy

RUN pip install uv

WORKDIR /code

COPY pyproject.toml uv.lock /code/

RUN uv sync --frozen --no-dev

ENTRYPOINT ["quick_word"]

FROM base AS dev
RUN uv sync --frozen
COPY . /code

FROM base AS final
COPY . /code
