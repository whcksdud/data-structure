table_size=13
class hash:
    # 해시 함수
    def fx(self, num):
        self.key = self.find_key(num)
        self.re_key = []
        for i in self.key:
            self.re_key.append(i % 12)
        return self.re_key
    # 이중 해싱 함수
    def fx2(self, key):
        self.re_key = key % 5
        return self.re_key
    #선형 조사법
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
    #이차 조사법
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
    #이중 해싱법
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
    # 키값 변환
    def find_key(self, a):
        self.key = []
        for i in a:
            self.b = list(i)
            self.k = 0
            for j in self.b:
                self.k += ord(j)
            self.key.append(self.k)
        return self.key


if __name__=="__main__":
    data1 = list(None for i in range(table_size))
    data2 = list(None for i in range(table_size))
    data3 = list(None for i in range(table_size))
    a = ["do", "for", "if", "case", "else", "return", "function"]
    hashtable = hash()
    print(hashtable.hash_lp_add(a, data1))
    print(hashtable.hash_qp_add(a, data2))
    print(hashtable.hash_dh_add(a, data3))

