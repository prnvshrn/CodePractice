class Solution(object):
    def eval(self, op1, sign, op2):
        if sign == '+':
            return int(op1) + int(op2)
        if sign == '-':
            return int(op2) - int(op1)
        if sign == '*':
            return int(op1) * int(op2)
        if sign == '/':
            return int(op2) // int(op1)

    def calculate(self, input):
        priority = {'+':1, '-':1, '*':2, '/':2};
        nums, operands, i = [], [], 0
        while i < len(input):
            if input[i].isnumeric():
                nums.append(input[i])
            else:
                operands.append(input[i])
                nums.append(input[i+1])
                i += 1
                if priority[operands[-1]]==2:
                    nums.append(self.eval(nums.pop(), operands.pop(), nums.pop()))
            i += 1
        
        while operands:
            nums.append(self.eval(nums.pop(), operands.pop(), nums.pop()))
        print(nums[0])

if __name__ == "__main__":
    obj = Solution()
    input = "3*3/4+4/2"
    obj.calculate(input)