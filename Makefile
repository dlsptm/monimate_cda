.PHONY: db-init
db-init:
	poetry run flask db init

.PHONY: db-migrate
db-migrate:
	poetry run flask db migrate

.PHONY: db-upgrade
db-upgrade:
	poetry run flask db upgrade


# Equivalent de phpcs
.PHONY: pycs
pycs:
	poetry run autopep8 --in-place --aggressive --recursive .
	poetry run flake8 app/
	poetry run black app/
	poetry run isort app/

# Equivalent de phpstan
.PHONY: pystan
pystan:
	poetry run mypy app/
	poetry run pylint app/
	poetry run bandit -r app/



.PHONY: test
test:
	poetry run pytest


.PHONY: docker-image-back
docker-image-back:
	docker build -t monimate-back-python .

.PHONY: docker-run-back
docker-run-back:
	 docker run --name test-monimate-back -it --rm -w /app -v ./:/app -p 9898:5000 monimate-back-python
