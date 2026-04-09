class Solution:
    def calPoints(self, operations):
        record = []
        
        for op in operations:
            if op.lstrip('-').isdigit():
                record.append(int(op))
            elif op == "D":
                record.append(2 * record[-1])
            elif op == "C":
                record.pop()
            elif op == "+":
                record.append(record[-1] + record[-2])
        
        return sum(record)