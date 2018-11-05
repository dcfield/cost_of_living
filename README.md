# Cost of Living

## Description
Calculate the average cost of rent in any area in the United Kingdom by inputting an area code.

## Technology Used
- Django
- Zoopla API
- Materialize CSS by Google
- Django unit tests


## Start
### Clone the repo, new virtualenv, install pip packages.
```
git clone https://github.com/dcfield/cost_of_living.git
cd cost_of_living
virtualenv cost_of_living
source cost_of_living/bin/activate
pip install -r requirements.txt

```

### Start up the server
```
python manage.py runserver
```

### Go to given address
This will something like `http://127.0.0.1:8000/`

### Run all unit tests

```
python manage.py test
```

