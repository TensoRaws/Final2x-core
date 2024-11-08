.DEFAULT_GOAL := default

.PHONY: test
test:
	poetry run pytest --cov=Final2x_core --cov-report=xml --cov-report=html

.PHONY: lint
lint:
	poetry run pre-commit install
	poetry run pre-commit run --all-files

.PHONY: gen
gen:
	poetry run python scripts/gen_config.py

.PHONY: gen-ts
gen-ts:
	poetry run python scripts/gen_pretrained_model_name.py

.PHONY: build
build:
	poetry build --format wheel

.PHONY: pyinstaller
pyinstaller:
	poetry run pyinstaller -n Final2x-core -i assets/favicon.ico Final2x_core/__main__.py
	poetry run python scripts/post_pyinstaller.py
