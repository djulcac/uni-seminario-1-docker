FROM python
RUN pip install -U scikit-learn
RUN pip install pandas
WORKDIR /app
COPY . /app
CMD ["python", "app.py"]