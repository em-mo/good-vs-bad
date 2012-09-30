#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  simulator.py
#  
#  Copyright 2012 Emil <emil@emil-luftbunt>
#  
from peer import Peer
from random import seed, sample

class Simulator:
    
    def __init__(self, no_empty_peers, no_good_peers, no_bad_peers,
                 test_probablility):
        self.test_probablility = test_probablility
        self.empty_peers = []
        self.good_peers = []
        self.bad_peers = []
        self.data_peers = []
        self.downloading_peers = []
        self.time = 0
        
        for i in range(no_empty_peers):
            self.empty_peers.append(Peer(None))
        
        for i in range(no_good_peers):
            self.good_peers.append(Peer(share_file(self.file_size, 
                                                   'good')))
            
        for i in range(no_bad_peers):
            self.bad_peers.append(Peer(share_file(self.file_size, 
                                  'bad')))
        
        self.data_peers = self.good_peers + self.bad_peers
        
        
    def do_step():
        self.time = self.time + 1
        if self.empty_peers:
            no_empty = len(self.empty_peers)
            
            if no_empty < len(data_peers):
                uploaders = sample(self.data_peers, no_empty)
                
                for peer in uploaders:
                    start_download(peer)
                
            else
                for peer in self.data_peers:
                    start_download(peer)

                    
                    
                    
    def start_download(peer):
        if test_data(peer):
            downloader = self.empty_peer.pop()
            downloader.download(peer)
            self.data_peers.append(downloader)
        
            if downloader.data == 'bad':
                self.bad_peers.append(downloader)
            else
                self.good_peers.append(downloader)
            
    def count_peer_types():
        return {'good': len(self.good_peers), 
                'bad': len(self.bad_peers),
                'empty': len(self.empty_peers)}
                
    def test_data(peer):
        if random() < test_probability and peer.data = 'bad':
            return False
        else
            return True
