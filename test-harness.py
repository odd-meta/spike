

from spikeGenerator import *
import random

generator = spikeGenerator(60)

node_list = generator.generate()

for x in range(0,10):
	for node in node_list:
		node.signal()