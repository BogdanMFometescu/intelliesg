FROM python:3.12

#Set the environment variables

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

#Set the working directory

WORKDIR /app

#Install Postrgresql client, gcc and cmake

#  RUN apt-get update && \
#      apt-get install -y postgresql-client gcc libpq-dev cmake && \#     rm -rf /var/lib/apt/lists/*




#Install poetry

RUN pip install poetry && \
    poetry config virtualenvs.create false

#Copy the poetry dependencies before installing

COPY pyproject.toml poetry.lock* /app/

#Install dependencies

RUN poetry install --no-root

#Copy all files 

COPY  . . 

EXPOSE 8000

