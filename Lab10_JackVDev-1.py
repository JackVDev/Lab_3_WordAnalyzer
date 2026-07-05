"""
    Lab10_JackVDev-1.py
    Jack Verdin
    This program creates a menu to select from a few text files, and then counts the words in the one selected.
    7/4/2026
"""

from pathlib import Path
import string

textcleaner = str.maketrans("", "", string.punctuation)

class WordAnalyzer:
    """
        WordAnalzyer Class, holds a filepath and dictionary containing a list of words and their frequencies
        attributes: self.__filepath, self.__wordfreq={}
    """

    def __init__(self, filepath):
        self.__filepath = Path(filepath)
        self.__wordfreq = {}
    
    def process_file(self):
        """
            Attepts to process the file given in self.__filepath
            If the file does not exist (FileNotFoundError), returns False
            If the file does exist, it processes the words and adds them to self.__wordfreq, returns True
        """
        #Count how many times each word appears in specified file
        try:
            text_raw = self.__filepath.read_text(encoding='utf-8').rstrip()
        except FileNotFoundError:
            return False # Signals to program that there was a problem.
        else:
            text_lines = text_raw.translate(textcleaner)
            text_lines = text_lines.lower()
            text_lines = text_lines.split()
            self.__wordfreq = {} # Empties __wordfreq to ensure the count is accurate
            for word in text_lines:
                try:
                    self.__wordfreq[word]
                except KeyError:
                    self.__wordfreq[word] = 1
                else:
                    self.__wordfreq[word] += 1
        return True # Signals to program that process_file() is done without issues
    
    def print_report(self):
        """
            Sorts and prints self.__wordfreq
        """
        # Print out results of process_file()
        self.__wordfreq = dict(sorted(self.__wordfreq.items())) # Sorts __wordfreq alphabetically by key
        for word, freq in self.__wordfreq.items():
            print(f"{word:<15} :: {freq:>3}")

def main():
    # Do Stuff
    listoffiles = {"1": "princess_mars.txt", "2": "Tarzan.txt", "3": "treasure_island.txt", "4": "monte_cristo.txt"}
    validinputs = {"1": "Princess Mars", "2": "Tarzan", "3": "Treasure Island", "4": "Monte Cristo", "5": "Exit"}
    usercontinue = True
    while usercontinue:
        print("\n--- Word Analyzer ---")
        for k, v in validinputs.items():
            print(f"{k}. {v}")
        userchoice = input("\nPlease enter your choice (1-5): ")
        if userchoice in list(validinputs.keys()):
            if userchoice == "5":
                usercontinue = False
            else:
                print(f"Processing {listoffiles[userchoice]}...\n")
                analysis = WordAnalyzer(listoffiles[userchoice])
                if analysis.process_file():
                    analysis.print_report()
                else:
                    print(f"The file {listoffiles[userchoice]} does not exist in this folder.")
                input("\nPress Enter to return to the menu...")
        else:
            print("Invalid Input\nPlease input a number from 1-5.")
    print("\nGoodbye!")


if __name__ == "__main__":
    main()