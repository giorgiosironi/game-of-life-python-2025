.PHONY: setup dev clean

setup:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

dev:
	. venv/bin/activate && flask --app src/app.py run --debug

clean:
	rm -rf venv
	find . -type d -name __pycache__ -exec rm -rf {} + 
