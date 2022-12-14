import argparse
import threading
from random import randint, choice
from time import sleep
from itertools import zip_longest
from queue import LifoQueue, PriorityQueue, Queue
from dataclasses import dataclass, field
from enum import IntEnum

from rich.align import Align
from rich.columns import Columns
from rich.console import Group
from rich.live import Live
from rich.panel import Panel

QUEUE_TYPES = {
    "fifo": Queue,
    "lifo": LifoQueue,
    "heap": PriorityQueue
}

PRODUCTS = (
    ":balloon:",
    ":cookie:",
    ":crystal_ball:",
    ":diving_mask:",
    ":flashlight:",
    ":gem:",
    ":gift:",
    ":kite:",
    ":party_popper:",
    ":postal_horn:",
    ":ribbon:",
    ":rocket:",
    ":teddy_bear:",
    ":thread:",
    ":yo-yo:",
)