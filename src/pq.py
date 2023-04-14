from heapq import heappop, heappush
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: float
    item: str|int=field(compare=False)

    def __init__(self, priority : float, item: int) -> None:
        self.priority = priority
        self.item = item
        pass
    

class IndexMinPrioityQueue:
    pq: list[PrioritizedItem]
    entry_finder = dict[int, PrioritizedItem]
    count: int

    def __init__(self) -> None:
        self.count = 0
        self.entry_finder = {}
        self.pq = []

    def push(self, key: int, priority: float) -> None:
        'Add a new item or update the priority of an existing item.'
        if key in self.entry_finder:
            entry: PrioritizedItem = self.entry_finder.pop(key)
            entry.item = '<removed-task>'
            self.count -= 1
        self.count += 1
        entry = PrioritizedItem(priority, key) 
        entry.priority = priority
        entry.item = key

        self.entry_finder[key] = entry
        heappush(self.pq, entry)
    
    def pop(self) -> int:
        'Remove and return the lowest priority item.'
        while self.pq:
            item = heappop(self.pq)
            if type(item.item) is int:
                self.count -= 1
                del self.entry_finder[item.item]
                return item.item
    
    def empty(self) -> bool:
        'Check whether the priority queue is empty.'
        return self.count <= 0    