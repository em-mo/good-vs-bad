#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  plotter.py
#  
#  Copyright 2012 Emil <emil@emil-luftbunt>
#  

from os import system, remove

def plot_x_y(x, y):
	axels_to_file(x, y)

	with open('temp_plot.gp', 'w') as out_file:
		out_file.write("set term gif; set output 'peer_plot.gif'; plot 'temp_peers.dat' with lines;")
		out_file.write("set term x11; set output; plot 'temp_peers.dat' with lines;")


	system('gnuplot -persist temp_plot.gp')
	remove('temp_plot.gp')

	return

def peers_to_file(peers_dict):
    with open('temp_peers.dat', 'w') as out_file:
        out_file.write('#step' + 'empty'.rjust(10) + 'good'.rjust(10) + 'bad'.rjust(10) + '\n')
        
        for k, v in peers_dict.iteritems():
            s = str(k).rjust(5) + str(v['empty']).rjust(10) + str(v['good']).rjust(10) + str(v['bad']).rjust(10) + '\n'
            out_file.write(s)


    return

def pick_peers_column(peers_dict, column):
	l = list()
	for k, v in peers_dict.iteritems():
		l.append(v[column])

	return l


def axels_to_file(x, y):
	with open('temp_peers.dat', 'w') as out_file:
		out_file.write('#x y\n')

		for a, b in zip(x, y):
			out_file.write('{} {}\n'.format(str(a), str(b)))

	return