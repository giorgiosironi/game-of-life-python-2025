.PHONY: setup dev clean test typecheck lint format

setup:
	python3 -m venv venv
	. venv/bin/activate && \
		pip install --upgrade pip setuptools && \
		pip install poetry && \
		poetry install --all-groups

dev:
	. venv/bin/activate && flask --app src/app.py run --debug

setup-prod:
	python3 -m venv venv-prod
	. venv-prod/bin/activate && \
		pip install --upgrade pip setuptools && \
		pip install poetry && \
		poetry install --only=main

prod:
	. venv-prod/bin/activate && \
	uwsgi --http 127.0.0.1:8000 --master -p 4 --pythonpath=src -w app:app

test:
	. venv/bin/activate && PYTHONPATH=src pytest

clean:
	rm -rf venv venv-prod
	find . -type d -name __pycache__ -exec rm -rf {} + 

typecheck:
	. venv/bin/activate && mypy src/ tests/ --strict --disallow-untyped-defs --disallow-incomplete-defs

lint:
	. venv/bin/activate && pylint src/ tests/

format:
	. venv/bin/activate && autopep8 --in-place --recursive src/ tests/
