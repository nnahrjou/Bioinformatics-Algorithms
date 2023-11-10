import sys
import copy


class GreedySorting:
    def __init__(self):
        self.P = []
        self._input()
        dist, reversalList = self.greedySort(self.P)
        print(dist)
        self.printList(reversalList)

    def _input(self):
        with open("GreedySorting.txt", "r") as file:
            data = sys.stdin.read().strip().split()
            self.P = [int(data[0][1:])] + [int(e)
                                           for e in data[1:-1]] + [int(data[-1][:-1])]

    def greedySort(self, P):
        dist = 0
        reversalList = []
        for k in range(len(P)):
            if k + 1 != abs(P[k]):
                for i in range(k + 1, len(P)):
                    if k + 1 == abs(P[i]):
                        t = i
                        break
                P = P[:k] + [-e for e in reversed(P[k:t + 1])] + P[t + 1:]
                reversalList.append(copy.deepcopy(P))
                dist += 1
            if k + 1 == -P[k]:
                P[k] = -P[k]
                reversalList.append(copy.deepcopy(P))
                dist += 1
        return dist, reversalList

    def printList(self, reversalList):
        for p in reversalList:
            print(
                '(' + ' '.join(['+' + str(e) if e > 0 else str(e) for e in p]) + ')')


if __name__ == "__main__":
    GreedySorting()
