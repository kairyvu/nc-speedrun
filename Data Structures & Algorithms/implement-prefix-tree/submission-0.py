class PrefixTree:

    def __init__(self):
        self.root = {}
        

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr["."] = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        return True if "." in curr else False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]
        return True

        