import ast
import json
from decimal import Decimal
from fractions import Fraction

import numpy as np


def get_poss(file, match, threshold) -> Decimal:
    """
计算至少包含指定数量个指定词条的已确实主词条的圣遗物概率
    :param file: 某类主词条的文件名
    :param match: 可匹配的副词条
    :param threshold: 至少匹配的副词条数
    :return: 满足匹配条件的概率
    """
    with open(file) as fin:
        data = json.load(fin)
    d1 = np.asarray(list(map(ast.literal_eval, data.keys())))
    d2 = np.asarray(list(map(Decimal, data.values())))
    condition = np.asarray(list(map(lambda x: sum([k in x for k in match]) >= threshold, d1)))
    return sum(np.extract(condition, d2))


print(f"{get_poss('0_Pyro.json', ['ATK%', 'CD', 'CR'], 1) = }")
print(f"{get_poss('0_Pyro.json', ['ATK%', 'CD', 'CR'], 2) = }")
print(f"{get_poss('0_Pyro.json', ['ATK%', 'CD', 'CR'], 3) = }")
print(f"{get_poss('3_CR.json', ['ATK%', 'CD'], 1) = }")
print(f"{get_poss('3_CR.json', ['ATK%', 'CD'], 2) = }")
print(f"{get_poss('4_ATK%.json', ['CD', 'CR'], 1) = }")
print(f"{get_poss('4_ATK%.json', ['CD', 'CR'], 2) = }")
print(f"{get_poss('6_ATK.json', ['ATK%', 'CD', 'CR'], 1) = }")
print(f"{get_poss('6_ATK.json', ['ATK%', 'CD', 'CR'], 2) = }")
print(f"{get_poss('6_ATK.json', ['ATK%', 'CD', 'CR'], 3) = }")

n = 2

print(f'>={n}:', 1 / (Decimal(0.9) * sum((get_poss('0_Pyro.json', ['ATK%', 'CD', 'CR'], n - 1) * Decimal(0.05),
                                          get_poss('3_CR.json', ['ATK%', 'CD'], n - 1) * Decimal(0.1),
                                          get_poss('4_ATK%.json', ['CD', 'CR'], n - 1) * Decimal(8 / 30),
                                          get_poss('6_ATK.json', ['ATK%', 'CD', 'CR'], n)),
                                         Decimal(0))))

print(f'>={n}:', 1 / (Decimal(0.9) * sum((get_poss('0_Pyro.json', ['ATK%', 'CD', 'CR'], n - 1) * Decimal(0.05),),
                                         Decimal(0))))

print(f'>={n}:', 1 / (Decimal(0.9) * sum((get_poss('3_CR.json', ['ATK%', 'CD'], n - 1) * Decimal(0.1),),
                                         Decimal(0))))

print(f'>={n}:', 1 / (Decimal(0.9) * sum((get_poss('4_ATK%.json', ['CD', 'CR'], n - 1) * Decimal(8 / 30),),
                                         Decimal(0))))

print(f'>={n}:', 1 / (Decimal(0.9) * sum((get_poss('6_ATK.json', ['ATK%', 'CD', 'CR'], n),),
                                         Decimal(0))))

print(Fraction(8 / 30))
print(float(Fraction(8 / 30)))
