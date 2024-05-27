FROM python:3.11

WORKDIR /app

COPY ./app /app
COPY ./alembic /alembic
COPY alembic.ini /alembic.ini

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set the PYTHONPATH environment variable
ENV PYTHONPATH="${PYTHONPATH}:/app"

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
