# 
FROM python:3.12-slim

# 
WORKDIR /app

# 
COPY ./requirements.txt ./requirements.txt

# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

# 
COPY ./app ./app

EXPOSE 8000

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]