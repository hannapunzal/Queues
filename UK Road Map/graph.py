import networkx as nx
from typing import NamedTuple
from queues import MutableMinHeap, Queue, Stack
from collection import deque
from math import inf as infinity

class City(NamedTuple):
    name: str
    country: str
    year: int | None
    latitude: float
    longitude: float
    