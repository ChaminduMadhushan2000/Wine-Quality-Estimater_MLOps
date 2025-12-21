FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install pandas scikit-learn mlflow numpy
CMD ["python", "train.py"]