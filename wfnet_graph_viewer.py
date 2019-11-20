#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# load package needed in this module
from graphviz import Digraph

# function to plot the converted list into a graph
def plot(converted):

    # initialize the digraph
    g = Digraph("G")
    # draw the graph from left to right
    g.attr(rankdir = "LR")

    """set the shape for transition as box"""

    # draw node as square
    g.attr("node", shape = "square")

    # for every sublist in converted list
    for connection in converted:

        # for every character in connection
        for character in connection:

            # if the initial character start with "t"
            if (character[0] == "t"):

                # set draw shape for the node as square
                g.node(character) #, label = "", xlabel = character)

    """set the shape for place as circle"""

    # draw node as circle
    g.attr("node", shape = "circle")

    # for every sublist in converted list
    for connection in converted:

        # for every character in connection
        for character in connection:

            # if the initial character start with "p"
            if (character[0] == "p"):

                # set draw shape for the node as box
                g.node(character) #, label = "", xlabel = character)

    """draw the graph"""

    # for every sublist in converted list
    for connection in converted:

        # draw the graph
        g.edge(connection[0], connection[1])

    # draw the graph, save it as png image, open the image and clean up the graphviz leftover file
    g.render(filename = "output", format = "png", view = True, cleanup = True)