class Event:
    def __init__(self):
        self.time = 0
        self.x = 0
        self.y = 0
    def __init__(self, time, x, y):
        self.time = time
        self.x = x
        self.y = y

class EventArray:
    def __init__(self):
        self.events = []
    def __init__(self, events):
        self.events = events
    
