install:
	pip install -U pip setuptools
	pip install -e .
	initialize_backend_db development.ini
run:
	pserve development.ini
