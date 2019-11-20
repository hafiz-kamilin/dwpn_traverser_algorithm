#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# load package needed in this module
import copy

# function for converting the pnml file to list
def list(filepath):

    # initialize a converted list to store the connection
    converted = []
    # initialize a connection list to temporarily store the connection
    connection = [0] * 2

    # open the file
    with open(filepath) as fp:

        # read the first line
        line = fp.readline()

        # as long end of line is not reached
        while line:

            # if specified line that contains "<arc id=" text was found
            if (line.find("<arc id=") > 0):

                """find the source node"""
                
                # find the highest index for "source=" text
                line_location = line.find('source="') + 8
                # save the individual character into the connection
                connection[0] = line[line_location]
                # increase the line_location count
                line_location += 1

                # as long the scanned individual character is not '"'
                while (line[line_location] != '"'):

                    # append to the previously added character
                    connection[0] += line[line_location]
                    # increase the line_location count
                    line_location += 1

                """find the target node"""

                # find the highest index for "target=" text
                line_location = line.find('target="') + 8
                # save the individual character into the connection
                connection[1] = line[line_location]
                # increase the line_location count
                line_location += 1

                # as long the scanned individual character is not '"'
                while (line[line_location] != '"'):

                    # append to the previously added character
                    connection[1] += line[line_location]
                    # increase the line_location count
                    line_location += 1

                # append the data into the converted
                converted.append(copy.deepcopy(connection))

            # read the next line
            line = fp.readline()

    # return the converted
    return converted