# coding: utf-8

import re
from collections import deque

class Stack(deque):
    push = deque.append
    
    def top(self):
        return self[-1]
    
    def dup(self):
        self.push(self[-1])
        
    def over(self):
        self.push(self[-2])
        
    def swap(self):
        self[-1], self[-2] = self[-2], self[-1]
        
    def drop(self):
        self.pop()

    def pick(self):
        self.push(self[-self.pop()])

    def roll(self):
        i = self.pop() + 1
        tmp = self[-i]
        del self[-i]
        self.push(tmp)

    def plus(self):
        self.push(self.pop() + self.pop())
    
    def minus(self):
        self.push(self.pop() - self.pop())
    
    def mul(self):
        self.push(self.pop() * self.pop())
    
    def div(self):
        self.push(self.pop() / self.pop())

    def mod(self):
        self.push(self.pop() % self.pop())

    def dot(self):
        print(self.pop())
        
    def dotstack(self):
        print(self)
        
    def __init__(self):
        self.dispatch_map = {
            '+': self.plus,
            '-': self.minus,
            '*': self.mul,
            '/': self.div,
            '%': self.mod,
            '.': self.dot,
            '.s': self.dotstack,
            '.S': self.dotstack,
            'drop': self.drop,
            'dup': self.dup,
            'over': self.over,
            'swap': self.swap,
            'pick': self.pick,
            'roll': self.roll,
        }
        self.symbol_table = {}

    def dispatch(self, key):
        if key in self.symbol_table:
            return self.execute(' '.join(self.symbol_table[key]))
        if key in self.dispatch_map:
            self.dispatch_map[key]()

    def execute(self, txt):
        state = 0
        name = None
        for i in re.findall(r'(\S+)', txt):
            if state == 0:
                if i == ':':
                    state = 1
                elif re.match(r'\d+', i):
                    stack.push(int(i))
                else:
                    stack.dispatch(i)
            elif state == 1:
                name = i
                state = 2
                self.symbol_table[name] = []
            elif state == 2:
                if i == ';':
                    state = 0
                else:
                    self.symbol_table[name].append(i)


stack = Stack()

stack.execute('1 2 + 3 4 * 5 6 / .s swap .s : a 1 2 3 swap ; a .s')
