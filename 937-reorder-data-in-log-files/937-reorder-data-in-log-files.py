class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs, digitLogs = [], []
        
        for log in logs:
            current_log = log.split(" ")
            if current_log[1].isdigit():
                digitLogs.append(log)
            else:
                letterLogs.append(log)
                    
        letterLogs.sort(key = lambda k: (" ".join(k.split(" ")[1:]), k.split(" ")[0]))
        
        return letterLogs + digitLogs
        
        