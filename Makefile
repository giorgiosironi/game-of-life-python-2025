.PHONY: setup dev clean test

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
