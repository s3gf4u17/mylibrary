FROM python:3.11.5-alpine3.17

WORKDIR /backend

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8080"]