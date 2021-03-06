install:
	pip install -r requirements.txt

serve:
	flask run

setup:
	flask initdb

drop_db:
	python manage.py flush

test:
	python manage.py test