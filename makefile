
build : applot/*.py applot/svg/*.py applot/plot_structure/*.py 
	python setup.py sdist bdist_wheel

upload : build
	python -m twine upload --repository pypi dist/*

clean : 
	rm -r dist/*
	rm -r build/*
	rm -r applot.egg-info

