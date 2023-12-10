class stack:
    def __init__(self):
        self.data= [] #스택 생성
        self.cnt =0
    def push(self,data): # 삽입 함수
        self.data.append(data)
        self.cnt += 1
    def isempty(self): # 공백 체크
        return len(self.data)==0
    def pop(self): # 삭제 함수
        if not self.isempty():
            self.cnt -= 1
            return self.data.pop()
    def size(self):
        return len(self.data)
    def postfix(self, a): # 후위표기식 변경
        self.temp = '' # 후위표기식 저장
        for i in a:
            if i.isdigit(): # 숫자면 저장
                self.temp+=i
            else: # 아니면 스택에 푸시
                if i == '(':
                    self.push(i)
                elif i == '*' or i == '/':
                    # self.data에 값이 있고
                    # 스택 top이 *,/ 이면 팝
                    while self.data and (self.data[-1] == '*' or self.data[-1] == '/'):
                        self.temp += self.pop()
                    self.push(i)
                elif i == '+' or i == '-':
                    # self.data에 값이 있고
                    # 스택 top이 (아니면 팝
                    while self.data and self.data[-1] != '(':
                        self.temp += self.pop()
                    self.push(i)
                elif i == ')':
                    # self.data에 값이 있고
                    # 스택 top이 (아니면 팝
                    while self.data and self.data[-1] != '(':
                        self.temp += self.pop()
                    self.pop()
        while self.data: # 남은 스택에 저장된값 팝
            self.temp+=self.pop()
        return self.temp
    def calculate(self,a): # 후위표기식 계산
        for j in a:
            if j == '+':
                self.push(self.pop() + self.pop())
            elif j == '-':
                self.push(-(self.pop() - self.pop()))
            elif j == '*':
                self.push(self.pop() * self.pop())
            elif j == '/':
                p = self.pop()
                self.push(self.pop() / p)
            else:
                self.push(int(j))
        return self.pop()
if __name__=="__main__":

    cal = stack()
    ev= "3+5*2/(7-2)"
    print(cal.postfix(ev))
    postev=cal.postfix(ev)
    print(cal.calculate(postev))
