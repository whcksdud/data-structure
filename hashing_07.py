import hash
class hash_cp(hash.hash):
    def hash_qp_add(self, a, data):
        self.key = self.fx(a)
        for i, j in zip(self.key, a):
            if data[i] != None:
                self.k = i
                self.w = 0
                self.cnt = 0
                while data[self.k] != None:
                    self.cnt += 1
                    self.w += 1
                    self.k = (self.k + self.w * self.w) % hash.table_size
                data[self.k] = j
            else:
                data[i] = j
        return data, self.cnt

    def hash_qp_add2(self, a, data):
        self.key = self.fx(a)
        for i, j in zip(self.key, a):
            if data[i] != None:
                self.k = i
                self.w = 0
                self.cnt = 0
                while data[self.k] != None:
                    self.cnt += 1
                    self.w += 1
                    self.k = (self.k + 2 * self.w + 1) % hash.table_size
                data[self.k] = j
            else:
                data[i] = j
        return data, self.cnt

if __name__=="__main__":
    data1 = list(None for i in range(hash.table_size))
    data2 = list(None for i in range(hash.table_size))
    a=["do", "for", "if", "case", "else", "return", "function", "lsit", "while", "self", "sort"]
    hashtable2 = hash_cp()
    print(hashtable2.hash_qp_add(a, data1))
    print(hashtable2.hash_qp_add2(a, data2))