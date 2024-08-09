# IntelliESG

## Description

IntelliESG is a Django-based web application designed to help organizations manage 
their Environmental, Social, and Governance (ESG) activities. 
The application offers comprehensive features for carbon footprint management, 
setting and tracking NET Zero targets, ESG risk management, compliance with EU Taxonomy, health and safety features, and governance policies. 
The platform includes forms and charts for each ESG topic, along with detailed graphs for emissions and carbon footprint measurement.

## Installation


### Prerequisites

- Python 3.x
- Poetry for Python dependency management
- PostgreSQL database
- Virtual environment (optional but recommended)

### Steps

1. Clone the repository or download the source code.
2. (Optional) Create a virtual environment:

  ```bash
    python -m venv venv
    venv\Scripts\activate
  ```

3. Install dependencies using Poetry:

  ```bash
    poetry install
  ```

4. Set up your environment variables in the .env file ,
including the PostgreSQL database settings.

- DB_AVAILABLE
- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT (this should be set to 5432)
- SECRET_KEY



To generate a new django secret key use the following command:
```bash
python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```


5. Run database migrations:

  ```bash
   python manage.py migrate
   ```

6. Create a superuser for Django admin:

  ```bash
  python manage.py createsuperuser
  ```  
7. Start the server:
```bash
python manage.py runserver

```


### Quick Start with Docker image

```bash

docker-compose up -d --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

```


### Usage

After installation, access the web application at http://localhost:8000.
The Django admin panel at http://localhost:8000/admin 
can be used for advanced management.

### Features

- Carbon Footprint Management: Track and analyze your carbon emissions.
- NET Zero Targets: Set and monitor progress towards net zero goals.
- ESG Risk Management: Identify and manage ESG-related risks.
- EU Taxonomy Compliance: Ensure compliance with EU Taxonomy regulations.
- Social Features: Health and safety management tools.
- Governance Features: Manage organizational policies and governance activities.
- Detailed Graphs and Charts: Visualize data for better insights.
- Export PDF reports 
- Upload data from Excel files 



### Technologies 

- Django (Python web framework)
- HTML/CSS for front-end design
- PostgreSQL as the database backend
- Poetry for dependency management


### Contributing

Contributions to IntelliESG are welcome. 
Please follow the coding standards and contribute to tests for new features.

### Licence

This project is licensed under the GPL licence - see the LICENSE file for details.