test: robot.mdl lex.py main.py matrix.py mdl.py display.py draw.py gmath.py yacc.py
	python main.py robot.mdl

clean:
	rm *pyc *out parsetab.py

clear:
	rm *pyc;rm *out;rm parsetab.py;rm *.ppm;rm *#;rm *~
