#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  simulator.py
#  
#  Copyright 2012 Emil <emil@emil-luftbunt>
#  
from peer import Peer
from share_file import ShareFile
from random import seed, sample, randint

class Simulator:
    
    def __init__(self, no_empty_peers, no_good_peers, no_bad_peers,
                 test_probability):
        
        self.test_probability = test_probability
        if test_probability == 1:
            self.always_test = True
        else:
            self.always_test = False
        
        self.empty_peers = list()
        self.good_peers = no_good_peers
        self.bad_peers = no_bad_peers
        self.data_peers = list()
        self.uploading_peers = list()
        self.working_peers = list()
        self.corrupted_peers = list()
        
        self.time = 0
        self.stats = {self.time:{'good':no_good_peers, 'bad':no_bad_peers,
                            'empty':no_empty_peers}}
        self.output_file = open('./output/outputfile', 'w')
        
        for i in range(no_empty_peers):
            self.empty_peers.append(Peer(ShareFile('empty'), 
                                         test_probability))
        
        for i in range(no_good_peers):
            self.data_peers.append(Peer(ShareFile('good'),
                                        test_probability))
            
        for i in range(no_bad_peers):
            self.data_peers.append(Peer(ShareFile('bad'),
                                  test_probability))

        return
        
    #~ ## Returns True when there are peers left without a file
    #~ def do_step():
        #~ if self.empty_peers:
            #~ self.time = self.time + 1
            #~ no_empty = len(self.empty_peers)
            #~ 
            #~ if no_empty < len(data_peers):
                #~ uploaders = sample(self.data_peers, no_empty)
                #~ 
                #~ for peer in uploaders:
                    #~ start_download(peer)
                #~ 
            #~ else
                #~ for peer in self.data_peers:
                    #~ start_download(peer)
            #~ 
            #~ self.stats.update({self.time: count_peer_types()})
            #~ 
            #~ return True
        #~ return False
        
    ## Returns True when there are peers left without a file


    #~ def start_download(peer):
        #~ if test_data(peer):
            #~ downloader = self.empty_peer.pop()
            #~ downloader.download(peer)
            #~ self.working_peers.append(downloader)
        #~ 
            #~ if downloader.data.content == 'bad':
                #~ self.bad_peers.append(downloader)
            #~ else
                #~ self.good_peers.append(downloader)
            #~ return True
        #~ return False
        
    def do_step(self):
        if self.empty_peers:
            self.time += 1
            
            self.working_peers = list()
            self.corrupted_peers = list ()
            
            while self.empty_peers and self.data_peers:
                uploader = self.get_random_peer(self.data_peers)
                
                assert uploader.data.content
                
                if uploader.test_data():
                    self.start_download(uploader)
                    self.working_peers.append(uploader)
                else:
                    self.empty_peers.append(uploader)
                    self.bad_peers -= 1
                    
            self.data_peers.extend(self.working_peers)
            self.empty_peers.extend(self.corrupted_peers)

            self.stats.update({self.time: self.count_peer_types()})
            
            return True
        return False
        
        
    def start_download(self, uploader):
        downloader = self.empty_peers.pop()
        downloader.download(uploader)
        
        if downloader.test_data() or self.always_test:
            self.working_peers.append(downloader)
            if downloader.data.content == 'bad':
                self.bad_peers += 1
            else:
                self.good_peers += 1
        else:
            self.corrupted_peers.append(downloader)
        return
                
            
    def count_peer_types(self):
        return dict(good=self.good_peers,
                    bad=self.bad_peers,
                    empty=len(self.empty_peers))
                
    def get_random_peer(self, peers):
        return peers.pop(randint(0, len(self.data_peers) - 1))
        
    def get_latest_stats(self):
        return self.stats[self.time]
    
    def get_stats_at(self, time):
        assert time <= self.time
        return self.stats[time]
