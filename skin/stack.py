class stack:
    def __init__(self, dim=10):
        self.dimension = dim
        self.top = 0
        self.data = []
    def is_empty(self): return self.top == 0
    def is_full(self): return self.top == (self.dimension-1)
    def __str__(self):
        return "Stack top :- {0} Stack dim :- {1} Stack data :- {2}". \
               format(self.top, self.dimension, self.data)
