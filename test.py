class stack:
    def __init__(self,n,name):
        self.size=n
        self.top = -1
        self.s = []
        self.name = name
    def is_empty(self):
        if self.top==-1:
            return True
        else:
            return False
    def is_full(self):
        if self.top + 1 == self.size:
            return True
        else:
            return False
    def pop(self):
        if self.is_empty() == 0:
            t = self.s.pop()
            print("弹出栈{}栈顶元素为{}".format(self.name,t))
            self.top -= 1
            return t
        else:
            print("{}栈空不能弹出".format(self.name))
    def push(self,x):
        if self.is_full() == 0:
            self.s.append(x)
            print("{}元素入栈{}".format(x,self.name))
            self.top += 1
        else:
            print("栈{}满不能入栈".format(self.name))
    def show_stack(self):
        return self.s

def fun():
    y = input("输入表达式，以q结尾:")
    stack1 = stack(len(y),'stack1')
    stack2 = stack(len(y),'stack2')
    x = input("请依次刷入合法表达式字符以’q‘号结尾例如：3*(1+2)q:")
    dic = {'+':1,'-':1,'*':2,'/':2,'(':3,')':0,'q':-1}
    while True:
        if stack1.top == -1 and stack2.top == 0:
            stack1.push(x)
        else:
            if x in '1234567890':
                stack2.push(x)
            else:
                t = stack1.pop()
                if (x == '(' and t in '+_*/()') or (x in '+_*/()' and t == '('):
                    stack1.push(t)
                    stack1.push(x)
                elif (x == ')' and t in '+_*/()') or (x in '+_*/()' and t == ')'):
                    while True:
                        stack2.push(t)
                        t = stack1.pop()
                        if t == '(':
                            break
                elif dic[x] > dic[t]:
                    stack1.push(t)
                    stack1.push(x)
                elif dic[x]<=dic[t]:
                    stack2.push(t)
                    stack1.push(x)
        print(stack2.s,stack1.s)
        x = input("请依次刷入合法表达式字符以’q‘号结尾例如：3*(1+2)#")
        if x == 'q':
            for i in range(stack1.top+1):
                stack2.push(stack1.pop())
            stack2.push('q')
            break
    print("后缀表达式栈stack2为：{}".format(stack2.s))
    return stack2
def count():
    stack2= fun()
    stack3=stack(stack2.top+1,'stack3')
    stack4 = stack(stack2.top+1,'stack4')
    while stack2.top != -1:
        stack3.push(stack2.pop())
    print("后缀表达式计算栈stack3为：{}".format(stack3.s))
    t = stack3.pop()
    while t != 'q':
        if t in '1234567890':
            stack4.push(t)
        else:
            if t == '+':
                stack4.push(int(stack4.pop())+int(stack4.pop()))
            elif t == '-':
                stack4.push(int(stack4.pop())-int(stack4.pop()))
            elif t == '*':
                stack4.push(int(stack4.pop())*int(stack4.pop()))
            elif t == '/':
                stack4.push(int(stack4.pop())/int(stack4.pop()))
        t = stack3.pop()
    print(stack4.s)
    

if __name__ == '__main__':
    count()
                
        
    
