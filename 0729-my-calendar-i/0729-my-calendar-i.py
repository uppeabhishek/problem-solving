class MyCalendar:

    def __init__(self):
        self.bookings = []
    
    def bsearch(self, l, r, booking):
        bookings = self.bookings
        
        while l <= r:
            m = l + (r - l) // 2   
            first = not (booking[1] <= bookings[m][0] or booking[0] >= bookings[m][1])
            if first:
                return False, -1
            elif booking[0] <= bookings[m][0]:
                r = m - 1
            else:
                l = m + 1
        
        return True, l
        
    
    def book(self, start: int, end: int) -> bool:
        bookings = self.bookings
                
        if not len(bookings):
            self.bookings.append([start, end])
            return True
        
        
        current_booking = [start, end]
        
        canBook, index = self.bsearch(0, len(bookings) - 1, current_booking)
        
        if not canBook:
            return False
        
        self.bookings.insert(index, current_booking)
        
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)