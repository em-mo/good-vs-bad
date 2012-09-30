#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2012 Emil <emil@emil-luftbunt>
#  
from simulator import Simulator
import argparse

def main():

    simulator = Simulator(20000, 4, 20, 0.1, False)
    
    print simulator.get_latest_stats()
    
    while simulator.do_step():
        print simulator.get_latest_stats()
    
    return 0

if __name__ == '__main__':
    main()

