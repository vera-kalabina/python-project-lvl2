install:
		poetry install

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user --force-reinstall dist/*.whl

lint:
		poetry run flake8 gendiff

test:
		poetry run pytest

test-cov:
		poetry run pytest --cov=gendiff tests --cov-report xml