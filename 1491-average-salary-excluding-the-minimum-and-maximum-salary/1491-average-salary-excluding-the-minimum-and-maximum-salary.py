class Solution:
    def average(self, salary: List[int]) -> float:
        max_sal = salary[0]
        min_sal = salary[0]
        total = 0
        ppl = 0
        for sal in salary:
            if sal > max_sal:
                max_sal = sal
            if sal < min_sal:
                min_sal = sal
            total += sal
            ppl += 1
        
        return (total - max_sal - min_sal) / (ppl - 2)        