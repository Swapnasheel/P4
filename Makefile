TREE_SCRIPT = tree.py
LINEAR_SCRIPT = linear.py

tree: 
	python $(TREE_SCRIPT) -d $(DEPTH) -f $(FANOUT)

linear:
	python $(LINEAR_SCRIPT) -s $(SW)

clean: 
	rm *.json


