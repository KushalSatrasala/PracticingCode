# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res_str = ""
        queue = list()
        i = 0
        queue.append((root, 0))
        while queue:
            next_queue = list()
            val_flag = False
            for node, indx in queue:
                if node == None:
                    continue
                else:
                    res_str += str(node.val) + ":" + str(indx) + ";"
                    next_queue.append((node.left, 2 * indx + 1 ))
                    next_queue.append((node.right, 2 * indx + 2 ))
                    val_flag = True
            
            if val_flag == False:
                break
            queue = next_queue

        return res_str[:-1]
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "None" or "" or len(data) == 0:
            return None
        node_list = data.split(";")
        slen = len(node_list)
        node_dict = dict()
        for node in node_list:
            parts = node.split(":")
            node_dict[int(parts[1])] = parts[0]

        root = None
        stack = list()
        root = TreeNode(node_list[0].split(":")[0])
        stack.append((root, 0))     
        while stack:
            node, indx = stack.pop()
            if node is None:
                continue
            left = (int(indx) * 2) + 1
            right = (int(indx) * 2) + 2
            if node_dict.get(left, None):
                left = TreeNode(node_dict.get(left))
            else:
                left = None
            if node_dict.get(right, None):
                right = TreeNode(node_dict.get(right))
            else:
                right = None

            node.left = left
            node.right = right
            stack.append((node.right, (int(indx) * 2) + 2))
            stack.append((node.left, (int(indx) * 2) + 1))
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))