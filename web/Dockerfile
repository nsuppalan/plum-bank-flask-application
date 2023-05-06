FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY swaggerurl.json ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "app.py" ]
