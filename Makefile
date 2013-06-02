install:
	virtualenv env
	env/bin/pip install -r requirements.txt

run:
	env/bin/python mediamover.py
