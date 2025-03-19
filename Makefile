.PHONY: setup dev clean test typecheck lint format

setup:
	python3 -m venv venv
	. venv/bin/activate && \
		pip install --upgrade pip && \
		pip install -r requirements.txt

dev:
	. venv/bin/activate && flask --app src/app.py run --debug

test:
	. venv/bin/activate && PYTHONPATH=src pytest

clean:
	rm -rf venv
	find . -type d -name __pycache__ -exec rm -rf {} + 

typecheck:
	. venv/bin/activate && mypy src/ tests/ --strict --disallow-untyped-defs --disallow-incomplete-defs

lint:
	. venv/bin/activate && pylint src/ tests/

format:
	. venv/bin/activate && autopep8 --in-place --recursive src/ tests/
