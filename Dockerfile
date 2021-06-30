FROM python:3.8
LABEL maintainer="Marawan Shalaby"

# copy and install requirements
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# copy the app
COPY . /app
WORKDIR /app

CMD [ "python", "app.py" ]
