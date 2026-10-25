class MinStack:

    def __init__(self):
        self.arr=[]
        self.min =[]

    def push(self, val: int) -> None:
        if self.min:
            if self.min[-1]>=val:
                self.min.append(val)
        else:
            self.min.append(val)
        return self.arr.append(val)

    def pop(self) -> None:
        if self.arr[-1]==self.min[-1]:
            self.min.pop()

        return self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min[-1]
