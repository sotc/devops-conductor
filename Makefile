setup:
	python3 -m venv ~/.conductordevops

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py 

format:
	black *.py 

test:
	python -m pytest -vv --cov= test_*.py

deploy:
	docker build -t conductor-app .