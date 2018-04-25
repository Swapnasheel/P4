TREE_SCRIPT = tree.py
LINEAR_SCRIPT = linear.py
SIMPLE_SWITCH_SCRIPT = simple_switch.py


tree: 
	python $(TREE_SCRIPT) -d $(DEPTH) -f $(FANOUT)

linear:
	python $(LINEAR_SCRIPT) -s $(SW)

simple_switch:
	python $(SIMPLE_SWITCH_SCRIPT) -n $(HOSTS)

clean: 
	rm *.json


