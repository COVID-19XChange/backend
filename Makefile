install:
        pip install -U pip setuptools
        pip install -e .
        initialize_backend_db development.ini
run:
        pserve development.ini
docker-build:
        docker build -t oi .
docker-run:
        docker run -p 0.0.0.0:6543:6543/tcp hi
docker-wp:
        docker run -p 0.0.0.0:8081:80/tcp wordpress:5.3.2-php7.2-apache
