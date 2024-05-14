#!/usr/bin/python3
from os import path
import json
"""This module contains the FileStorage class definition"""


class FileStorage:
    """This is the class FileStorage"""
    def __init__(self):
        """Init: FileStorage instance constructor"""
        self.__file_path = 'file.json'
        self.__objects = {}
        
    def all(self):
        """All method:
        Returns the dictionary object of the class"""
        return self.__objects
        
    def new(self, obj):
        """new method: sets in __objects the obj"""
        self.__objects = obj
        
    def save(self):
        """save method:
        serializes __objects to the JSON file"""
        with open('file.json', 'w') as json_file:
            json.dump(self.__objects, json_file)
            
    def reload(self):
        """reload method:
        deserializes the JSON file to __objects"""
        if path.exists('file.json'):
            with open('file.json', 'r') as json_file:
                self.__objects = json.load(json_file)
        else:
            pass
