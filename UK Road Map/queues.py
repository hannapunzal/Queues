from collections import deque
from dataclasses import dataclass 
from heapq import heapify, heappop, heappush
from itertools import count
from typing import AnyStr

class IterableMixin:
    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

class Queue(IterableMixin):
    def __init__(self, *elements):
        self._elements = deque(elements)

    def enqueue(self, element):
        self._elements.append(element)
    
    def dequeue(self):
        return self._elements.popleft()