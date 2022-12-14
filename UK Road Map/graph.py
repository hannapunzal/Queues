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

    @classmethod
    def from_dict(cls, attrs):
        return cls(
            name = attrs ["xlabel"],
            country = attrs["country"],
            year = int(attrs["year"]) or None,
            latitude = float(attrs["latitude"])
            longitude = float(attrs["longitude"]),
        )
    
    def load_graph(filename, node_factory):