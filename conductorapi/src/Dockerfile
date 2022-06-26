FROM python:3.9-alpine
ENV APP_JWT_SECRET=sekret
WORKDIR /src
COPY ./requirements.txt /src/requirements.txt
COPY ./app /src/app/
RUN pip install -r requirements.txt
CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3000" ]