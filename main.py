#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2012 Emil <emil@emil-luftbunt>
#  
from simulator import Simulator
from alt_simulator import AltSimulator
from plotter import peers_to_file, axels_to_file, pick_peers_column, plot_x_y
from itertools import izip_longest
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('n', nargs=3, type=int, 
                    help='Order: Total M, data N, bad n')
parser.add_argument('p', type=float, help='Test probability')
parser.add_argument('-p', '--plot', choices=['good', 'bad', 'empty'],
                    help='Choose if and what to plot')
parser.add_argument('-a', '--avg', type=int,
                    help='Take an average over this many runs, makes no sense without --plot')



def main():
    args = parser.parse_args()
    
    ## Total number of peers
    M = args.n[0]
    ## Total number of uploading peers
    N = args.n[1]
    ## Number of bad peers
    n = args.n[2]
    ## Probability for testing
    p = args.p
    
    assert N > n
    if p < 0.0:
        p = 0.0
    elif p > 1.0:
        p = 1.0
    
    simulator = AltSimulator(M - N, N - n, n, p)
    stats = None
    
    print simulator.get_latest_stats()

    if args.avg:
        # Hack if args.plot is not set
        if not args.plot:
            args.plot = 'good'

        for i in range(args.avg):
            ## (Empty, good, bad, probability)
            simulator.run()
            current_stats = pick_peers_column(simulator.stats, args.plot)
            
            # Sum up the peers
            if stats:
                stats = list(sum(s) for s in zip(stats, current_stats))
            else:
                stats = current_stats

            simulator = AltSimulator(M - N, N - n, n, p)

        # Divide each position in the list
        stats = map(lambda x: x/args.avg, stats)


    else:
        print simulator.get_latest_stats()
        while simulator.do_step():
            print simulator.get_latest_stats()
        stats = simulator.stats
    
    if args.plot:
        plot_x_y(range(len(stats)), stats,)

    return 0

if __name__ == '__main__':
    main()

