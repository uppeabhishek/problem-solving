class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        gasRequired = 0
        
        for i in range(len(gas)):
            gasRequired += gas[i] - cost[i]
                
        if gasRequired < 0:
            return -1
        
        index = -1
        
        gasRequired = 0
                
        for i in range(len(gas)):
            
            gasRequired += gas[i] - cost[i]
            
            if gas[i] - cost[i] >= 0:
                if index == -1:
                    gasRequired = gas[i] - cost[i]
                    index = i
            else:
                if gasRequired < 0:
                    index = -1
            
        return index
            
        
            
            