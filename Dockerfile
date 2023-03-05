FROM python:3.10-slim

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ["loan_catboost_model.cbm", "app.py", "./"]

EXPOSE 8989:8989

CMD ["python", "app.py"]