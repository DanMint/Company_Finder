install:
	./run_scripts/env_creation.sh

test: install
	./run_scripts/test.sh

run: install
	./run_scripts/run.sh