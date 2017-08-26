test:
	py.test --cov --cov-report term-missing -v

release:
	# rm dist/*
	python setup.py sdist bdist_wheel
	twine upload dist/*
