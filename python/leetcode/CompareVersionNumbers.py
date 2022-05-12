class Solution:

    def appendZeros(self, version, cnt):
        for i in range(cnt):
            version.append("0")

    def removeLeadingZeros(self, version):
        for i in range(len(version)):
            version[i] = int(version[i])

    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split("."), version2.split(".")
        if len(v1) < len(v2):
            self.appendZeros(v1, len(v2) - len(v1))
        elif len(v2) < len(v1):
            self.appendZeros(v2, len(v1) - len(v2))

        self.removeLeadingZeros(v1)
        self.removeLeadingZeros(v2)

        for i in range(len(v1)):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1
            return 0


if __name__ == "__main__":
    s = Solution()
    s.compareVersion("1.01", "1.001")
    s.compareVersion("0.1", "1.1")
    s.compareVersion("1.0", "1.0.0")
