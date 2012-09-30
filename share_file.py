#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  share_file.py
#  
#  Copyright 2012 Emil <emil@emil-luftbunt>
#  

file_types = frozenset(['good', 'bad', 'empty'])

class ShareFile:
    
    def __init__(self, content):
        
        assert content in file_types
        
        self.content = content
        
        return
        
