import random
maxsize=5 # 큐 사이즈
class que:
    class customer: # 고객 정보
        def __init__(self, ids, arrival_time, service_time):
            self.id = ids
            self.arrival_time = arrival_time
            self.service_time = service_time
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.data=[None]*maxsize
    def isempty(self):
        return self.front == self.rear
    def isfull(self):
        return self.front == (self.rear+1)%maxsize
    def enque(self,ids, arrival_time, service_time):
        if not self.isfull():
            self.rear = (self.rear+1)%maxsize
            self.data[self.rear] = self.customer(ids, arrival_time, service_time)
    def deque(self):
        if not self.isempty():
            self.front = (self.front+1)%maxsize
            return self.data[self.front]
    def display(self):
        out = []
        if self.front < self.rear:
            out = self.data[self.front+1:self.rear+1]
        else:
            out = self.data[self.front+1:maxsize]\
            +self.data[0:self.rear+1]
        print(out)

if __name__=="__main__":
    bank = que()
    total_customers = 0 # 총 고객 수
    #service_customer 이용 고객
    service_time =0
    total_wait = 0 # 총 대기 시간
    minutes = 10 # 은행 업무 시간간
    for clock in range(minutes+1):
        print("현재 시간 {}".format(clock))
        n = random.randint(1, 10) # 3보다 작으면 고객 생성
        if n < 3:
            time = random.randint(1, 3) # 고객의 업무처리 시간
            bank.enque(total_customers, clock, n)
            print("고객 {}이 {}분에 들어옵니다. 업무처리 시간={}"
                  .format(total_customers, clock, n))
            total_customers += 1
        if service_time > 0:
            print("고객 {} 업무 처리중입니다.".format(service_customer))
            service_time -= 1
        else:
            if not bank.isempty():
                customer=bank.deque()
                service_customer = customer.id
                service_time = customer.service_time
                print("고객 {}이 {}분에 업무를 시작합니다. 대기시간은 {}분이었습니다."
                      .format(service_customer, clock, clock-customer.arrival_time))
                total_wait += clock - customer.arrival_time

    print("전체 대기 시간={}분".format(total_wait))