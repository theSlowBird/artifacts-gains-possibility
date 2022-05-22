import decimal
from copy import deepcopy
from decimal import Decimal
import json

STAT_NAME = {
    "HP": 6,
    "ATK": 6,
    "DEF": 6,
    "HP%": 4,
    "ATK%": 4,
    "DEF%": 4,
    "EM": 4,
    "ER": 4,
    "CR": 3,
    "CD": 3,
}


def work(stat_name, filename):
    tot = {}

    def get(i: int, st: dict = stat_name, stat: list = [], p: Decimal = Decimal(1)):
        if i == 0:
            key = str(sorted((set(stat))))
            tot[key] = tot.get(key, 0) + p
            return
        s = sum(st.values())
        for k, v in st.items():
            st2 = deepcopy(st)
            st2.pop(k)
            get(i - 1, st2, stat + [k], p * v / s)

    get(4)
    print(type(tot))
    tot = {k: str(v) for k, v in tot.items()}
    with open(f'{filename}.json', 'w') as fout:
        json.dump(tot, fout, indent=4)


print(f'{decimal.getcontext().prec = }')
work(STAT_NAME, '0_Pyro')
st2 = deepcopy(STAT_NAME)
st2.pop('ATK')
work(st2, '6_ATK')
st2 = deepcopy(STAT_NAME)
st2.pop('ATK%')
work(st2, '4_ATK%')
st2 = deepcopy(STAT_NAME)
st2.pop('CR')
work(st2, '3_CR')
