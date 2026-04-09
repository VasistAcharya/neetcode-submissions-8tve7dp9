class Solution:
    def calPoints(self, operations):
        record = []
        
        for op in operations:
            match op:
                case "D":
                    record.append(2 * record[-1])
                case "C":
                    record.pop()
                case "+":
                    record.append(record[-1] + record[-2])
                case _:
                    record.append(int(op))
        
        return sum(record)