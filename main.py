from dataclasses import dataclass
import json
import math
from typing import Dict, Tuple, List


@dataclass
class Score:
    src: str
    dst: str
    score: float
    rate: float

def score(rates: Dict[str, float], pair: Tuple[str, str]) -> Score:
    (src, dst) = pair
    a = rates[src]
    b = rates[dst]
    s = math.log10(b / a) % 1.0
    return Score(src, dst, s, b / a)


data = None
with open("./tempdata.json", "r") as f:
    data = json.loads("".join(f.readlines()))

rates: Dict[str, float] = data['conversion_rates']
print(f"Found {len(rates)} currencies")

pairs = [(i, j) for j in rates.keys() for i in rates.keys() if i != j]

scores: List[Score] = sorted([score(rates, i) for i in pairs], key=lambda a: a.score)
for s in scores[:100]:
    print(s)

