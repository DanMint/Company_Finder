install:
	pip install --upgrade pip
	pip install -r requirements.txt

test:
	python3 -m unittest unit_tests/test_builtInScrape.py