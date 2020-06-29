# migrations
migrations:
	python manage.py makemigrations
migrate:
	python manage.py migrate
create:
	python manage.py createsuperuser
server:
	python manage.py runserver

# git
commit:
	git commit --amend
push:
	git push --force origin ft-userprofile

#virtual
virtual:
	source virtual/bin/activate



