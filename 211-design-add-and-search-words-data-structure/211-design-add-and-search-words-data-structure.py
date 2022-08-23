class WordDictionary:

    def __init__(self):
        self.root = dict()

    def addWord(self, word: str) -> None:
        cur_node = self.root
        prev_node = None
        for ch in word:
            if ch not in cur_node:
                cur_node[ch] = (dict(), False)
            prev_node = cur_node
            cur_node, flag = cur_node[ch]
        prev_node[word[-1]] = (cur_node, True)

    def search(self, word: str) -> bool:
        queue = list()
        queue.append(self.root)
        i = 0
        slen = len(word)
        while queue:
            next_queue = list()
            for node in queue:
                if word[i] == ".":
                    for key in node.keys():
                        nd, flag = node[key]
                        next_queue.append(nd)
                        if i + 1 == slen and flag:
                            return True
                else:
                    if word[i] not in node:
                        continue
                    if i + 1 == slen:
                        nxt, flag = node[word[i]]
                        if flag:
                            return True
                        continue
                    nd, flag = node[word[i]]
                    next_queue.append(nd)
            i += 1
            if i == slen:
                break
            queue = next_queue
        return False
                    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)