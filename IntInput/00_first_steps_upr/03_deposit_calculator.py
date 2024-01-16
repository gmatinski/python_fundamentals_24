#сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

# От конзолата се четат 3 реда:
# 1.	Депозирана сума – реално число в интервала [100.00 … 10000.00]
# 2.	Срок на депозита (в месеци) – цяло число в интервала [1…12]
# 3.	Годишен лихвен процент – реално число в интервала [0.00 …100.00]

deposit_sum = float(input())
term_of_deposit = int(input())
annual_interest_rate = float(input()) / 100
sum_at_the_end = deposit_sum + term_of_deposit * ((deposit_sum * annual_interest_rate) / 12)
print(sum_at_the_end)