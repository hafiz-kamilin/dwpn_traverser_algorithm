#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# source 1: https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
# source 2: Convertibility and Conversion Algorithm of Well-Structured Workflow Net to Process Tree

# load package needed in this module
from collections import defaultdict
import itertools
import copy

# function that store nested-function for traversing the graph
def go(converted, start):

	""" nested function """

	# function to remove duplicated list
	def removeDuplicate(sublist):

		# sort the sublist
		sublist.sort()
		# remove the duplicate and return
		return list(sublist for sublist,_ in itertools.groupby(sublist))

	# function to add an edge to graph, create reference and initialize the input/output arc counter
	def addEdge(source, target):

		"""add an edge to graph"""

		# append the edge which contain source and target to the graph defaultdict
		graph[source].append(target)

		"""initialize reference dictionary for each node"""

		# append the source as key and 0 as value to the reference dictionary
		reference[source] = [0, 0, False, False]

	# function to check if graph's key was registered in reference or not
	def checkKey(dict, key):
		
		# utilize keys() function to find matching key in dictionary 
		if key in dict.keys():
			
			# key was found
			return True
		
		else:

			# key is not found
			return False

	# function to count the input and output arc for 'place' and 'transition' node
	def countArc(converted):

		# initialize counter for node paths numbering
		path_scanner = 0

		# while traversed path_scanner are not equal to the number of path 
		while (path_scanner != len(converted)):

			# increase the path_scanner by 1
			path_scanner += 1

			# for every sublist in converted list
			for connection in converted:

				"""count the input for 'place' and 'transition' node"""

				# if it match with the predifined source node
				if (connection[0] == "p" + str(path_scanner)):

					# increase the count found
					reference["p" + str(path_scanner)][1] += 1

					# if the count is more than 1
					if ((reference["p" + str(path_scanner)][1] > 1) and
					    (reference["p" + str(path_scanner)][3] != True)):

						# change the third reference variable to true
						reference["p" + str(path_scanner)][3] = True

				# if it match with the predifined source node
				elif (connection[0] == "t" + str(path_scanner)):

					# increase the count found
					reference["t" + str(path_scanner)][1] += 1

					# if the count is more than 1
					if ((reference["t" + str(path_scanner)][1] > 1) and
					    (reference["t" + str(path_scanner)][3] != True)):

						# change the third reference variable to true
						reference["t" + str(path_scanner)][3] = True

				"""count the output for 'place' and 'transition' node"""

				# if it match with the predifined source node
				if (connection[1] == "p" + str(path_scanner)):

					# increase the count found
					reference["p" + str(path_scanner)][0] += 1

					# if the count is more than 1
					if ((reference["p" + str(path_scanner)][0] > 1) and
					    (reference["p" + str(path_scanner)][2] != True)):

						# change the third reference variable to true
						reference["p" + str(path_scanner)][2] = True

				# if it match with the predifined source node
				elif (connection[1] == "t" + str(path_scanner)):

					# increase the count found
					reference["t" + str(path_scanner)][0] += 1

					# if the count is more than 1
					if ((reference["t" + str(path_scanner)][0] > 1) and
					    (reference["t" + str(path_scanner)][2] != True)):

						# change the third reference variable to true
						reference["t" + str(path_scanner)][2] = True

	# recursive function of custom depth first search (dfs)
	def recursiveTraverse(target): 

		# show the traversed node
		print (target + " ", end = "")

		# if there is some node's arc input left to be traversed
		if (reference[target][0] > 0):

			# reduce the node's arc input by 1
			# NOTE: if the node's arc input is 0, the node already travested
			reference[target][0] -= 1

		# for every next target node connected to the current target (source) node
		for node in graph[target]:

			# if the next target node has only 1 arc input
			if (reference[node][0] == 1):

				# execute recursive traverseOrder from this node to check the order
				traverseOrder(node)

			# else the next target node have more than 1 arc input
			# NOTE: this represent the node that joins multiple nodes
			else:

				# reduce the next target node's arc input by 1
				reference[node][0] -= 1

	# function to traverse the graph using custom depth first search (dfs)
	def traverseOrder(target): 

		# check if the node is a place with multiple output
		if ((target[0] == "p") and (reference[target][3] == True)):

			order.append("choice(")

		# check if the node is a transition with multiple output
		elif ((target[0] == "t") and (reference[target][3] == True)):

			order.append("parallel(")

		# check if the node is a place without multiple input/output
		elif ((target[0] == "p") and (reference[target][2] == False) and (reference[target][3] == False)):

			try:
				
				# try to check the previous node connected to this node if it is a node with multiple output
				# check is done on a 'graph' dictionary
				if reference[[k for k, v in graph.items() if target in v][0]][3] == True:
					
					order.append("(")
			except:

				# if checking failed do nothing
				pass
			
			# if the next node have multiple input
			if (reference[graph[target][0]][2] == True):

				order.append(")")

		# check if the node is a transition without multiple input/output
		elif ((target[0] == "t") and (reference[target][2] == False) and (reference[target][3] == False)):

			try:

				# try to check the previous node connected to this node if it is a node with multiple output
				# check is done on a 'graph' dictionary
				if reference[[k for k, v in graph.items() if target in v][0]][3] == True:
					
					order.append("(")
			
			except:

				# if checking failed do nothing
				pass
			
			# append the current target into the 'order' list
			order.append(target)

			# if the next node have multiple input
			if (reference[graph[target][0]][2] == True):

				order.append(")")

		# check if the node have multiple input
		elif (reference[target][2] == True):

			order.append(")")

		# call the recursive function of custom depth first search (dfs)
		recursiveTraverse(target)

	""" main function code """

	# initialize defaultdict type of variable to store the graph
	graph = defaultdict(list)
	# initialize dictionary type of variable to store the graph's key reference
	reference = {}
	# initialize order list
	order = []
	# initialize a counter
	count = 0

	# remove duplicated list from converted
	converted = removeDuplicate(converted)
	# find the number of arcs
	length = len(converted)

	# for every sublist in converted list
	for connection in converted:

		# add edge (arc for wf-net) into the graph
		addEdge(connection[0], connection[1])
		# increase the counter by 1
		count += 1

		# if all edges are already added into the graph
		if (count == length):

			# for every sublist in converted list
			for connection in converted:

				# for every character in connection
				for character in connection:

					# check if there is any unregistered node
					# unregistered node usually the the last 'place' node in wf-net 
					if (checkKey(reference, character) == False):

						# add unregistered node as final edge to close the graph
						addEdge(character, character)

	# count the arc input/output for 'place' and 'transition' node
	countArc(converted)
	# call the function to check the transition order
	traverseOrder(start)
	print ("\n", *order)