"""
    Lab10_JackVDev-1.py
    Jack Verdin
    This program creates a menu to select from a few text files, and then counts the words in the one selected.
    7/4/2026
"""

from pathlib import Path

class WordAnalyzer:
    """
        Word Analyzer class UNFINISHED
    """

    def __init__(self, filepath):
        self.__filepath = Path(filepath)
        self.__wordfreq = {}
    
    def process_file(self):
        #Count how many times each word appears in specified file
        try:
            raw_text = self.__filepath.read_text(errors="replace")
        except FileNotFoundError:
            print("This file does not exist!") # figure out actual error prevention
            
        raise NotImplementedError # NOT FINISHED
    
    def print_report(self):
        # Print out results of process_file()
        raise NotImplementedError # NOT FINISHED