FROM python:3.8.13-slim-buster
ENV APP_JWT_SECRET=sekret
RUN mkdir -p /src
COPY ./app /src/app/
WORKDIR /src
COPY ./requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt
CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3000" ]
ENTRYPOINT [ "python" ]