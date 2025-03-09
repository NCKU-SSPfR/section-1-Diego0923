# TODO: Install the backend dependency package into the app folder inside the container.

FROM python:3.11

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

RUN useradd -m -u 1000 myuser
RUN chown -R myuser:myuser /app

COPY --chown=myuser:myuser ./src/ /app/src
USER myuser

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
