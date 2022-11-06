class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:

        def get_length(num):
            le = 0
            while num:
                num = num // 10
                le += 1

            return le

        def reverse(num):
            length = 0
            current = 0

            while num:
                rem = num % 10
                current = current * 10 + rem
                num = num // 10
                length += 1

            return current, length

        i, j = 0, num

        while i <= j:
            i1, i1_length = reverse(i)

            diff = get_length(j) - i1_length

            while diff:
                i1 = i1 * 10
                diff -= 1

            if i1 == j:
                return True

            i += 1
            j -= 1

        return False


