# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 11:18:05 2021

@author: Oluwayelu Ifeoluwa
"""

class BasicHashTable:
    def __init__(self, max_size=4096):
        self.data_list = [None] * max_size
        
    def insert(self, key, value):
        self.data_list[self.get_index(key)] = (key, value)
        
    def find(self, key):
        kv = self.data_list[self.get_index(key)]
        
        if kv is None:
            return None
        else:
            key, value = kv
            return value
    
    def update(self, key, value):
        self.data_list[self.get_index(key)] = (key, value)
    
    def list_all(self):
        return [data for data in self.data_list if data is not None]
    
    def get_index(self, key):
        result = 0

        for char in key:
            a_number = ord(char)
            result += a_number

        index = result % len(self.data_list)
        return index
    

class ProbingHashTable:
    def __init__(self, max_size=4096):
        self.data_list = [None] * max_size
        
    def insert(self, key, value):
        idx = self.get_valid_index(self.data_list, key)
        
        self.data_list[idx] = (key, value)
        
    def find(self, key):
        idx = self.get_valid_index(self.data_list, key)
        
        kv = self.data_list[idx]
        
        return None if kv is None else kv[1]
    
    def update(self, key, value):
        idx = self.get_valid_index(self.data_list, key)
        
        self.data_list[idx] = (key, value)
        
    def list_all(self):
        return [kv for kv in self.data_list if kv is not None]
    
    def get_valid_index(self, key):
        idx = hash(key) % len(self.data_list)
        
        while True:
            kv = self.data_list[idx]
            
            if kv is None:
                return idx
            
            k, v = kv
            if key == k:
                return idx

            idx += 1
            
            if idx == len(self.data_list):
                idx = 0

class HashTable:
    def __init__(self, max_size=4096):
        self.data_list = [None] * max_size
        
    def __setitem__(self, key, value):
        idx = self.get_valid_index(key)
        
        self.data_list[idx] = (key, value)
            
    def __getitem__(self, key):
        idx = self.get_valid_index(key)
        
        kv = self.data_list[idx]
        
        return None if kv is None else kv[1]
    
    def __len__(self):
        return len([kv for kv in self])
    
    def __iter__(self):
        return (kv for kv in self.data_list if kv is not None)
    
    def __repr__(self):
        from textwrap import indent
        pairs = [indent("{} : {}".format(repr(kv[0]), repr(kv[1])), '  ') for kv in self.data_list if kv is not None]
        return "{\n" + "{}".format(',\n'.join(pairs)) + "\n}"
    
    def __str__(self): 
        return repr(self)
    
    def get_valid_index(self, key):
        idx = hash(key) % len(self.data_list)
        
        while True:
            kv = self.data_list[idx]
            
            if kv is None:
                return idx
            
            k, v = kv
            if key == k:
                return idx

            idx += 1
            
            if idx == len(self.data_list):
                idx = 0