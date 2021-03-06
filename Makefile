install:
	pip install -r requirements.txt

serve:
	flask run

setup:
	flask initdb

dump_data:
	flask import_state
	flask import_events

drop_db:
	python manage.py flush

test:
	python manage.py test