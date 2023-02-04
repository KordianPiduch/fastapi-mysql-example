APP_NAME = fastapi_mysql_example

.PHONY: build
build:
	docker build -t $(APP_NAME) .

.PHONY: run
run:
	docker run --name my_app --rm -p 8000:8000 -d $(APP_NAME) 

.PHONY: stop
stop:
	docker stop my_app

.PHONY: venv
venv:
	python3 -m venv venv

.PHONY: bootstrap
bootstrap: venv ## bootstrap the development environment inside a virtualenv
	( \
		. venv/bin/activate; \
		pip install -r requirements.txt; \
		pip install -e .; \
	)
	@echo ""
	@echo "    source venv/bin/activate"
	@echo ""

.PHONY: clean
clean: clean-build clean-pyc clean-venv clean-docker

.PHONY: clean-build
clean-build: ## Remove build artifacts.
	rm -fr build/
	rm -fr dist/
	rm -fr omnibus/pkg/
	rm -fr omnibus/.bundle
	rm -fr omnibus/bin
	rm -fr omnibus/Gemfile.lock
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +

.PHONY: clean-pyc
clean-pyc: ## Remove Python file artifacts.
	find . -name '*.pyc' -exec rm -fr {} +
	find . -name '*.pyo' -exec rm -fr {} +
	find . -name '*~' -exec rm -fr {} +
	find . -name '__pycache__' -exec rm -fr {} +

.PHONY: clean-venv
clean-venv: ## Remove virtualenv.
	rm -fr venv/

.PHONY: clean-docker
clean-docker:
	docker rmi $(APP_NAME) -f