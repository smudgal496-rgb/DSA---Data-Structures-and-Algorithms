class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value, priority):
        data = [priority, value]
        if not self.queue:
            self.queue.append(data)   
        else:
            add= False
            for i in range(len(self.queue)):
                if priority > self.queue[i][0]:
                    self.queue.insert(i, data)
                    add= True
                    break
        self.queue.sort(key=lambda x: x[1], reverse=True)
