from FuzzyExpert.fuzzy import *

print('\nHello, please enter your credit score (300-850) and your total line of credit (1,000 - 10,000):')

credit_score = 300
amount = 1000

while True:
    try:
        credit_score = int(input("Credit Score: "))
    except ValueError:
        print("Please enter a valid whole number 300-850")
        continue
    if 300 <= credit_score <= 850:
        credit_score = int(credit_score)
        break
    else:
        print('Your Credit Score must be in the range of 300-850')

while True:
    try:
        amount = int(input("Credit Limit Amount: "))
    except ValueError:
        print("Please enter a valid whole number 1,000-10,000")
        continue
    if 1_000 <= amount <= 10_000:
        amount = int(amount)
        break
    else:
        print('You Credit Limit Amount must be in the range of $1,000-$10,000')

# Pseudo
# Rule 1: IF credit_score is low AND amount is high THEN risk is high
# Rule 2: IF credit_score is mid AND amount is high THEN risk is high
# Rule 3: IF credit_score is high AND amount is high THEN risk is mid

# Rule 4: IF credit_score is low AND amount is mid THEN risk is high
# Rule 5: IF credit_score is mid AND amount is mid THEN risk is mid
# Rule 6: IF credit_score is high AND amount is mid THEN risk is low

# Rule 7: IF credit_score is low AND amount is low THEN risk is mid
# Rule 8: IF credit_score is mid AND amount is low THEN risk is low
# Rule 9: IF credit_score is high AND amount is low THEN risk is low


func_LC = credit_low(credit_score)
func_MC = credit_mid(credit_score)
func_HC = credit_high(credit_score)

func_creditScore = [func_LC, func_MC, func_HC]
print(func_creditScore)

func_LA = amount_low(amount)
func_MA = amount_mid(amount)
func_HA = amount_high(amount)

func_amount = [func_HA, func_MA, func_LA]
print(func_amount)

rule_list = rules_list(func_creditScore, func_amount)

high_risk = [0.0, .15, .3, .5, .6, .7, .9, 1.0]
mid_risk = [0.0, .3, .6, 1.0, 1.0, .6, .3, 0.0]
low_risk = [1.0, .9, .7, .6, .5, .3, .15, 0.0]

# rule_list[0] is HIGH
rule_1 = rule_high(rule_list[0], high_risk)

# rule_list[1] is HIGH
rule_2 = rule_high(rule_list[1], high_risk)

# rule_list[2] is MID
rule_3 = rule_high(rule_list[2], mid_risk)

# rule_list[3] is HIGH
rule_4 = rule_high(rule_list[3], high_risk)

# rule_list[4] is MID
rule_5 = rule_high(rule_list[4], mid_risk)

# rule_list[5] is LOW
rule_6 = rule_high(rule_list[5], low_risk)

# rule_list[6] is MID
rule_7 = rule_high(rule_list[6], mid_risk)

# rule_list[7] is LOW
rule_8 = rule_high(rule_list[7], low_risk)

# rule_list[8] is LOW
rule_9 = rule_high(rule_list[8], low_risk)

all_rule_vectors = [
    rule_1,
    rule_2,
    rule_3,
    rule_4,
    rule_5,
    rule_6,
    rule_7,
    rule_8,
    rule_9
]

agg_list = agg_vector(all_rule_vectors)

result = round(defuzz(agg_list), 3)
# print()
print(f"\nRisk factor: {result} out of 100")
