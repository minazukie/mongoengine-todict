.PHONY: build test publish

build:
	rm -fr build && rm -fr dist && python3 setup.py sdist bdist_wheel
publish:
	twine upload dist/*
test:
	pytest
