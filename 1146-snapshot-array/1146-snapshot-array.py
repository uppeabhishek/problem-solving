class SnapshotArray:

    def __init__(self, length: int):
        self.array = [[(-1, 0)] for _ in range(length)]
        self.snap_id = -1

    def set(self, index: int, val: int) -> None:
        
        snap_id = self.snap_id
        
        temp_snap_id, temp_val = self.array[index][-1]
        
        value = (snap_id, val)
        
        if temp_snap_id < snap_id:
            self.array[index].append(value)
        else:
            self.array[index][-1] = value
            
    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id

    def bsearch(self, left, right, index, snap_id):
        
        while left <= right:
            mid = (left + right) // 2
            
            mid_snap_val = self.array[index][mid][0]

            if mid_snap_val == snap_id:
                return self.array[index][mid]
            elif snap_id < mid_snap_val:
                right = mid - 1
            else:
                left = mid + 1
        
        return self.array[index][max(right, 0)]
                
        
    def get(self, index: int, snap_id: int) -> int:    
        return self.bsearch(-1, len(self.array[index]) - 1, index, snap_id - 1)[1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)