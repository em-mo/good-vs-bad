#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  alt_simulator.py
#  
#  Copyright 2012 Emil <emil@emil-luftbunt>
#  
from random import randint, random

class AltSimulator:
    
    def __init__(self, no_empty_peers, no_good_peers, no_bad_peers,
                 test_probability):
        self.test_probability = test_probability
        if test_probability == 1:
            self.always_test = True
        else:
            self.always_test = False
        
        self.empty_peers = no_empty_peers
        self.good_peers = no_good_peers
        self.bad_peers = no_bad_peers
        self.corrupt_peers = 0
        self.cleared_peers = 0
        self.working_peers = 0

        self.data_peers = self.good_peers + self.bad_peers
        
        self.time = 0
        self.stats = {self.time:{'good':no_good_peers, 
                                 'bad':no_bad_peers,
                                 'empty':no_empty_peers,
                                 'corrupt':0}}
        

        return
        
    def do_step(self):
        if self.empty_peers:
            self.time += 1
            
            self.cleared_peers = 0
            self.working_peers = 0
            no_good = self.good_peers
            no_bad = self.bad_peers
            no_corrupt = self.corrupt_peers

            while self.empty_peers and self.data_peers:
                peer = self.get_random_peer(no_good, no_bad, no_corrupt)

                if peer == 'good':
                    self.inc_good()
                    no_good -= 1
                elif peer == 'corrupt':
                    ## Detect corrupt data before upload
                    if self.data_test():
                        self.dec_corrupt()
                    else:
                        ## Detect corrupt download if applicable
                        if self.data_test() and not self.always_test:
                            self.failed_upload()
                        else:
                            self.inc_corrupt()
                    no_corrupt -= 1
                else:
                    self.inc_corrupt()
                    no_bad -= 1
                
            self.data_peers += self.working_peers
            self.empty_peers += self.cleared_peers
            
            self.stats.update({self.time: self.count_peer_types()})
            return True
            
        else:
            return False 
        
    def get_random_peer(self, good, bad, corrupt):
        peer_number = randint(1, good + bad + corrupt)

        if peer_number <= good:
            return 'good'
        elif peer_number <= good + corrupt:
            return 'corrupt'
        else:
            return 'bad'
            
    def data_test(self):
        if random() < self.test_probability:
            return True
        else:
            return False
            
    def inc_good(self):
        self.good_peers += 1
        self.working_peers += 2
        self.empty_peers -= 1
        self.data_peers -= 1
        return
        
    def inc_corrupt(self):
        self.corrupt_peers += 1
        self.working_peers += 2
        self.empty_peers -= 1
        self.data_peers -= 1
        
    def dec_corrupt(self):
        self.corrupt_peers -= 1
        self.cleared_peers += 1
        self.data_peers -= 1
        return 
    
    def failed_upload(self):
        self.working_peers += 1
        self.cleared_peers += 1
        self.empty_peers -= 1
        self.data_peers -= 1
        return 

    def count_peer_types(self):
        return dict(good=self.good_peers,
                    bad=self.bad_peers,
                    empty=self.empty_peers,
                    corrupt=self.corrupt_peers)
        
    def get_latest_stats(self):
        return self.stats[self.time]
    
    def get_stats_at(self, time):
        assert time <= self.time
        return self.stats[time]
