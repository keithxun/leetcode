class Fancy:
    MOD = 10**9 + 7

    def __init__(self):
        self.seq = []
        self.mul = 1
        self.add = 0

    def append(self, val: int) -> None:
        self.seq.append((val, self.mul, self.add))

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1

        val, old_mul, old_add = self.seq[idx]

        if old_mul == 0:
            return self.add

        ratio = self.mul * pow(old_mul, self.MOD - 2, self.MOD) % self.MOD
        return (ratio * (val + self.MOD - old_add) + self.add) % self.MOD