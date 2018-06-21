import pandas as pd

df = pd.read_csv("clicks.csv")

is_purchase_list = []
for i in range (0, df.shape[0]):
    per = df.click_day[i]
    if per == per:
        is_purchase_list.append("Purchase")
    else:
        is_purchase_list.append("No Purchase")
df["is_purchase"] = is_purchase_list

purchase_counts = df.groupby([df["group"], df["is_purchase"]])["user_id"].count()

contingency = []
purchase_counts_list = purchase_counts.tolist()
for i in range(0, len(purchase_counts_list) / 2):
    contingency.append([purchase_counts_list[i * 2 + 1], purchase_counts_list[i * 2]])
	
from scipy.stats import chi2_contingency

print chi2_contingency(contingency)[1]

visitor_total = df.shape[0]
print visitor_total

pp_99 = (1000/.99) / visitor_total

pp_199 = (1000/1.99) / visitor_total

pp_499 = (1000/4.99) / visitor_total

from scipy.stats import binom_test

print binom_test(contingency[0][0], contingency[0][0] + contingency[0][1], pp_99)

print binom_test(contingency[1][0], contingency[1][0] + contingency[1][1], pp_199)

print binom_test(contingency[2][0], contingency[2][0] + contingency[2][1], pp_499)