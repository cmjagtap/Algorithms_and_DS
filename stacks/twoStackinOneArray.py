class red_blue_stack():
    def __init__(self, capasity):
        self.capasity = capasity
        self.data = [None] * capasity
        self.red_top = -1
        self.blue_top = self.capasity
    
    def red_push(self, element):
        if 	self.red_top < self.blue_top - 1:
                self.red_top = self.red_top + 1
                self.data[self.red_top] = element
        else:
            print("Stack Overflow ")
    
    def blue_push(self, element):
        if self.red_top< self.blue_top - 1:
                self.blue_top = self.blue_top - 1
                self.data[self.blue_top] = element
        else :
           print("Stack Overflow ")
    def red_pop(self):
        if self.red_top >= 0:
            x = self.data[self.red_top]
            self.red_top = self.red_top -1
            return x
        else:
            print("Stack Underflow ")

    def blue_pop(self):
        if self.blue_top < self.capasity:
            x = self.data[self.blue_top]
            self.blue_top = self.blue_top + 1
            return x
        else:
            print("Stack Underflow ")
stk=red_blue_stack(10)
stk.red_push(2)
stk.red_push(3)
stk.red_push(4)
print("Popped ele red stack is " + str(stk.red_pop()))
stk.blue_push(9)
stk.blue_push(8)
stk.blue_push(7)
stk.blue_push(6)
print("Popped ele blue stack is " + str(stk.blue_pop()))