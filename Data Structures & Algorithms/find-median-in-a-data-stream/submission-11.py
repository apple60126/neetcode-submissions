class MedianFinder:

    def __init__(self):
        self.lst = []

    def addNum(self, num: int) -> None:
        self.lst.append(num)

    def findMedian(self) -> float:
        res = sorted(self.lst)
        print(res)
        if len(res) % 2 == 0:
            
            return (res[len(res)// 2 - (1)] + res[(len(res)// 2)]) / 2
        else:
            print(res[(len(res) // 2) ])
            return res[(len(res) // 2) ]
        










