install:
	chmod +x ./run_scripts/env_creation.sh
	./run_scripts/env_creation.sh

test: install
	chmod +x ./run_scripts/test.sh
	./run_scripts/test.sh

run: install
	chmod +x ./run_scripts/run.sh
	./run_scripts/run.sh