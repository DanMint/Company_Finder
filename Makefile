install:
	./run_scripts/env_creation.sh

test: install
	./run_scripts/test.sh

run:
	./run_scripts/run.sh