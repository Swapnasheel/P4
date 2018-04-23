TREE_SCRIPT = tree.py

all: tree


tree: 
	python $(TREE_SCRIPT) -d $(DEPTH) -f $(FANOUT)


clean: 
	rm *.json


