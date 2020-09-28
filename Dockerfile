FROM python:3.8.5

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "calculate_routes.py"]