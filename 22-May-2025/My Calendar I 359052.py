# Problem: My Calendar I - https://leetcode.com/problems/my-calendar-i/description/

class MyCalendar:
    def __init__(self):
        self.booked = []

    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.booked:
            # Check for overlap
            if start < endTime and startTime < end:
                return False
        self.booked.append((startTime, endTime))
        return True

# Example usage:
# myCalendar = MyCalendar()
# print(myCalendar.book(10, 20))  # Output: True
# print(myCalendar.book(15, 25))  # Output: False
# print(myCalendar.book(20, 30))  # Output: True