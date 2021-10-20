run:
	cd src && python main.py

build:
	cd src && python -m eel main.py web --onefile --noconsole
