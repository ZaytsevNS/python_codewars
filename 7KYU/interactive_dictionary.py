# Solution for task: https://www.codewars.com/kata/57a93f93bb9944516d0000c1/

class Dictionary():
    def __init__(self):
        self.words_and_entries = dict()
        
    def newentry(self, word: str, definition: str):
        self.words_and_entries[word] = definition
        
    def look(self, key: str) -> str:
        return self.words_and_entries.get(key, f"Can't find entry for {key}")
