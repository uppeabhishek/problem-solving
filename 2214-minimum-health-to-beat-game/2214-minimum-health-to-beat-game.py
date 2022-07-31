class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        damage.sort()
        result = 0
        for i in range(len(damage)):
            if damage[i] == armor:
                return sum(damage) - damage[i] + 1
            
            if damage[i] > armor:
                if i == 0:
                    return sum(damage) - armor + 1
                else:
                    damage[i] = damage[i] - armor
                    return sum(damage) + 1
        
        return max(0, sum(damage) - min(damage[-1], armor) + 1)
            
            
            
            
            