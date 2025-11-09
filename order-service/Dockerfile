FROM python:3.13-slim AS builder

RUN python -m pip install --disable-pip-version-check uv

COPY pycommon /app/pycommon
COPY order-service /app/order-service

WORKDIR /app/order-service

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

RUN uv sync --no-dev

FROM python:3.13-slim

RUN groupadd -r polozhenie && \
    useradd -rg polozhenie polozhenie

COPY --from=builder --chown=polozhenie:polozhenie /app /app

USER polozhenie

WORKDIR /app/order-service

ENV PATH="/app/order-service/.venv/bin:$PATH"

EXPOSE 8000

ENTRYPOINT ["uvicorn", "polozhenie.order_service.app:app", "--host", "0.0.0.0"]
