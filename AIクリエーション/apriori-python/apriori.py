# Apriori Python Program
# Yasuhiro Hayashi

import csv
from apyori import apriori
import pandas as pd

def read_csv_file(filename):
    with open(filename, "r", encoding="UTF-8") as f:
        reader = csv.reader(f)
        lines = [row for row in reader]
        return lines

transactions = read_csv_file("data/test_apriori.csv")

#rules = apriori(transactions)
rules = apriori(transactions, min_support = 0.1, min_lift=0.5, min_confidence = 0.4)

results = list(rules)
data = []
for row in results:
    for r in row.ordered_statistics:
        buf = [
            ','.join(r.items_base),
            ','.join(r.items_add),
            row.support,
            r.confidence,
            r.lift,
        ]
        data.append(buf)

df = pd.DataFrame(data)
df.columns = ["from", "to", "support", "confidence", "lift"]

print(df.sort_values("support", ascending=False))
