table_size=13
class hash:
    def fx(self, num):
        self.key = self.find_key(num)
        self.re_key = []
        for i in self.key:
            self.re_key.append(i % 12)
        return self.re_key

    def fx2(self, key):
        self.re_key = key % 5
        return self.re_key

    def hash_lp_add(self, a, data):
        self.key = self.fx(a)
        for i, j in zip(self.key, a):
            if data[i] != None:
                self.k = i
                while data[self.k] != None:
                    self.k = (self.k + 1) % table_size
                data[self.k] = j
            else:
                data[i] = j
        return data

    def hash_qp_add(self, a, data):
        self.key = self.fx(a)
        for i, j in zip(self.key, a):
            if data[i] != None:
                self.k = i
                self.w = 0
                while data[self.k] != None:
                    self.w += 1
                    self.k = (self.k + self.w * self.w) % table_size
                data[self.k] = j
            else:
                data[i] = j
        return data

    def hash_dh_add(self, a, data):
        self.key = self.fx(a)
        for i, j in zip(self.key, a):
            if data[i] != None:
                self.k = i
                self.w = 1
                self.kk = 11 - (self.k % 11)
                self.kkk = (self.k + self.kk * self.w) % table_size
                while data[self.kkk] != None:
                    self.w += 1
                    self.kkk = (self.k + self.kk * self.w) % table_size
                data[self.kkk] = j
            else:
                data[i] = j
        return data

    def find_hash(self, a):
        for i in range(len(a)):
            print("[{}]:".format(i), end="")
            if a[i] != None:
                print(" {}".format(a[i]), end="")
            print("")

    def find_key(self, a):
        self.key = []
        for i in a:
            self.b = list(i)
            self.k = 0
            for j in self.b:
                self.k += ord(j)
            self.key.append(self.k)
        return self.key