all:
	rm -rf build/
	rm -rf dist/
	python -m build

upload:
	twine upload --repository pypi dist/* --verbose
