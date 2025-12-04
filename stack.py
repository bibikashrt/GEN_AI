class Stack:
    def __init__(self,size):
       self.size=size
       self.stack=[None]*size
    
    def push(self,items):
        if self.top==self.size-1:
            print('stack overflow!')
        else:
            self.top+=1
            self.stack[self.top]=items
            print(f'{items} is pushed into the stack')

    def pop(self):
        if self.top==1:
            print('stack underflow!')
        else:
            removed=self.stack[self.top]
            self.stack[self.top]=None
            self.top-=1
            print(f'{removed} is popped from the stack')

    def peek(self):
        if self.top==-1:
            print('stack underflow!!')
        else:
            print(f'{self.stack[self.top]} is the topmost value present')

    def display(self):
        if self.top==-1:
            print('stack underflow!')
        else:
            print('The elements present in the stack are:')
            for i in range(self.top,-1,-1):
                print(self.stack[i])

def main():
        size=int(input('Enter the size of the stack'))
        s=Stack(size) 

        while True:
            print('Menu: Stack Operation\n')
            print('1. push\n 2. pop\n 3. peek\n 4.display\n 5.exit\n')

            choice=input('Enter the choice to perform..')

            if choice=='1':
                element=int(input('Enter the value push into the stack'))
                s.push(element)
            elif choice=='2':
                s.pop()
            elif choice=='3':
                s.peek()    
            elif choice=='4':
                s.display()
            elif choice=='5':
                break 
            else:
                print('Invalid choice>> please try again')

if __name__=="__main__":
    main()                                                              
    