class TreeNode:
    def __init__(self, val, left=None, right=None, height=1):
        self.val = val
        self.left = left
        self.right = right
        self.height = height  # 높이를 뜻하는 height 속성 추가 기본값=1


class AVLtree:
    def __init__(self, val):
        self.root = TreeNode(val)

    def insert(self, val):
        self.root = self._insert_node(self.root, val)

    def _insert_node(self, cur, val):
        if not cur:
            return TreeNode(val)
        elif val < cur.val:
            cur.left = self._insert_node(cur.left, val)
        elif val > cur.val:
            cur.right = self._insert_node(cur.right, val)

        cur.height = 1 + max(self._get_height(cur.left),
                             self._get_height(cur.right))

        balance = self._get_balance(cur)
        if balance > 1 and val > cur.left.val:  # Left-Right case
            cur.left = self._left_rotate(cur.left)
            cur = self._right_rotate(cur)

        elif balance > 1 and val < cur.left.val:  # Left-Left case
            cur = self._right_rotate(cur)

        elif balance < -1 and val > cur.right.val:  # Right-Right case
            cur = self._left_rotate(cur)

        elif balance < -1 and val < cur.right.val:  # Right-Left case
            cur.right = self._right_rotate(cur.right)
            cur = self._left_rotate(cur)
        return cur

    def _find_predecessor(self, cur):
        if cur.right:
            return self._find_predecessor(cur.right)
        else:
            return cur.val

    def _left_rotate(self, cur):
        v = cur
        w = cur.right
        t = w.left
        cur = w
        w.left = v
        v.right = t
        v.height = 1 + max(self._get_height(v.left), self._get_height(v.right))
        w.height = 1 + max(self._get_height(w.left), self._get_height(w.right))
        return cur

    def _right_rotate(self, cur):
        v = cur
        w = cur.left
        t2 = w.right
        cur = w
        w.right = v
        v.left = t2
        v.height = 1 + max(self._get_height(v.left), self._get_height(v.right))
        w.height = 1 + max(self._get_height(w.left), self._get_height(w.right))
        return cur

    def _get_height(self, cur):
        if not cur:
            return 0
        return cur.height

    def _get_balance(self, cur):
        if not cur:
            return 0
        return self._get_height(cur.left) - self._get_height(cur.right)

    def traverse(self):
        return self._print(self.root, [])

    def _print(self, cur, result):
        if cur:
            self._print(cur.left, result)
            result.append(cur.val)
            self._print(cur.right, result)
        return result


avl = AVLtree(3)
avl.insert(2)
avl.insert(5)
avl.insert(1)
avl.insert(4)
avl.insert(8)
avl.insert(7)
print(f'root balance: {avl._get_balance(avl.root)}, path: {avl.traverse()}')