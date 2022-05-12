import sys


class Solution:
    def minimizeResult(self, expression: str) -> str:
        addition = expression.find("+")
        min_result = sys.maxsize
        min_output = ""

        for i in range(addition):
            for j in range(addition + 1, len(expression)):
                first = int(expression[0:i]) if expression[0:i] else 0
                second = int(expression[i:addition]) if expression[i:addition] else 0
                third = int(expression[addition + 1:j]) if expression[addition + 1: j] else 0
                fourth = int(expression[j:len(expression)]) if expression[j:len(expression)] else 0

                if first == 0:
                    if third == 0:
                        current = second + fourth
                        if current < min_result:
                            min_result = current
                            min_output = "(" + str(second) + "+" + str(fourth) + ")"
                    else:
                        current = (second + third) * fourth
                        if current < min_result:
                            min_result = current
                            min_output = "(" + str(second) + "+" + str(third) + ")" + str(fourth)
                elif third == 0:
                    current = first * (second + fourth)
                    if current < min_result:
                        min_result = current
                        min_output = str(first) + "(" + str(second) + "+" + str(fourth) + ")"
                else:
                    current = first * (second + third) * fourth
                    if current < min_result:
                        min_result = current
                        min_output = str(first) + "(" + str(second) + "+" + str(third) + ")" + str(fourth)

        return min_output


s = Solution()
s.minimizeResult("999+999")
s.minimizeResult("247+38")
