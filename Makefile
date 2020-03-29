install:
	@pip install -U pip setuptools
	@pip install -e .
	@initialize_backend_db development.ini

run:
	@pserve development.ini

thanos_click:
	@docker stop `docker ps -qa`
	@docker container prune -f
	@docker rmi `docker images -q`

thanos_click_pp: thanos_click
	@docker volume prune -f
	@docker network prune -f

create_init_maria_sql:
	# wordpress stuff
	echo "CREATE DATABASE $(WORDPRESS_DB_NAME);\n" \
	  "CREATE USER '$(WORDPRESS_DB_USER)'@'wordpress' IDENTIFIED BY '$(WORDPRESS_DB_PASSWORD)';\n" \
	  "GRANT ALL PRIVILEGES ON $(WORDPRESS_DB_NAME).* TO '$(WORDPRESS_DB_USER)'@'%';" > \
	  init_maria.sql
