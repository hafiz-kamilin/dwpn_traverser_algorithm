#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# load modules needed in this program
import pnml_file_translation
import wfnet_node_traverse
import wfnet_graph_viewer

# test_bugs.pnml
# test_easy.pnml
# test_hard.pnml
filepath = "test_hard.pnml"

# convert pnml file into a readable format
converted = pnml_file_translation.list(filepath)
print ("\nNodes and arcs that are extracted from the pnml file:") 

print (converted, "\n")

# visualize the wf-net using graphviz
# wfnet_graph_viewer.plot(converted)

# plot the wf-net and traverse the nodes
print ("Traversed nodes sequence:")
wfnet_node_traverse.go(converted, "p1")
