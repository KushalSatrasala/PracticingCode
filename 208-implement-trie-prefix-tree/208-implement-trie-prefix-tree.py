class Trie:

    def __init__(self):
        self.root = dict()
        

    def insert(self, word: str) -> None:
        cur_node = self.root
        prev_node = None
        for ch in word:
            if ch not in cur_node:
                cur_node[ch] = (dict(), False)
            prev_node = cur_node
            cur_node, flag = cur_node[ch]
        prev_node[word[-1]] = (cur_node, True)

    def search(self, word: str) -> bool:
        cur_node = self.root
        for ch in word:
            if ch not in cur_node:
                return False
            prev_node = cur_node
            cur_node, flag = cur_node[ch]
        
        node, flag = prev_node[word[-1]]
        return flag

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for ch in prefix:
            if ch not in cur_node:
                return False
            prev_node = cur_node
            cur_node, flag = cur_node[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)