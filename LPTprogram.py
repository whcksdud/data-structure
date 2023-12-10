MAX=4 # 힙사이즈
machine = 3 # 기계 수

class element: # 작업 기계
    def __init__(self,id=None, avail=None):
        self.id = id
        self.avail = avail

class heap_cr: # 힙
    def __init__(self):
        self.heap = [None]*MAX
        self.heap_size = 0
    def circle(self): # 힙 초기화
        for i in range(MAX):
            self.heap[i] = element()

class LPT: # lpt 알고리즘
    def __init__(self):
        self.lpt = heap_cr()
        self.lpt.circle()
    def insert_min(self, item): # 삽입
        self.lpt.heap_size += 1
        self.i = self.lpt.heap_size
        # 부모 노드와 비교하여 트리를 내려간다.
        while (self.i!=1) and (item.avail < self.lpt.heap[self.i//2].avail):
            self.lpt.heap[self.i] = self.lpt.heap[self.i//2]
            self.i //= 2
        self.lpt.heap[self.i] = item
    def delete_min(self): # 삭제
        self.parent = 1
        self.child = 2
        self.item = self.lpt.heap[1]
        self.temp = self.lpt.heap[self.lpt.heap_size]
        self.lpt.heap_size -= 1
        # 더 작은 자식 노드를 찾는 과정
        while self.child <= self.lpt.heap_size:
            if (self.child < self.lpt.heap_size) and \
                    (self.lpt.heap[self.child].avail > self.lpt.heap[self.child+1].avail):
                self.child += 1
            if self.temp.avail < self.lpt.heap[self.child].avail:
                break
            self.lpt.heap[self.parent] = self.lpt.heap[self.child]
            self.parent = self.child
            self.child *= 2
        self.lpt.heap[self.parent] = self.temp
        return self.item

if __name__=="__main__":
    jobs = [8,7,6,5,3,2,1]
    h = LPT()

    for i in range(machine):
        m = element(i+1, 0)
        h.insert_min(m)

    for j in range(len(jobs)):
        m = h.delete_min()
        print("JOB {}을 시간={}부터 시간={}까지 기계 {}번에 할당한다."
              .format(j, m.avail, m.avail+jobs[j]-1, m.id))
        m.avail += jobs[j]
        h.insert_min(m)