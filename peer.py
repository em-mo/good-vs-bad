#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  peer.py
#  
#  Copyright 2012 Emil <emil@emil-luftbunt>
#  
from random import seed, random

class Peer:
    
    def __init__(self, data, test_probability):
        self.data = data
        self.test_probability = test_probability
        
        if data.content == 'bad':
            self.malicious = True
        else:
            self.malicious = False
        
    def download(self, peer):
        self.data = peer.data
        return
            
    
    def clear_data(self):
        self.data = None
        return

    def test_data(self):
        if (random() < self.test_probability and 
           self.data.content == 'bad' and not self.malicious):
            return False
        else:
            return True
