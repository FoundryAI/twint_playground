FROM python:3.7

WORKDIR /src

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "src/main.py"]
