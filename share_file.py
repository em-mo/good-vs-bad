#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  share_file.py
#  
#  Copyright 2012 Emil <emil@emil-luftbunt>
#  

class ShareFile:
    file_types = frozenset('good', 'bad')
    
    def __init__(self, content):
        if content not in file_types: raise AssertionError
        
        self.content = content
        
