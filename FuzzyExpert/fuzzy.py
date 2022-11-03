def member_value(a, b, c, x):
    if x <= a:
        return round(float(0.0), 3)
    elif a <= x <= b:
        return round(float((x - a) / (b - a)), 3)
    elif b <= x <= c:
        return round(float((c - x) / (c - b)), 3)
    elif c <= x:
        return round(float(0.0), 3)


def credit_low(credit_input):
    a = 300
    b = 300
    c = 500
    x = credit_input

    return member_value(a, b, c, x)


def credit_mid(credit_input):
    a = 400
    b = 550
    c = 700
    x = credit_input

    return member_value(a, b, c, x)


def credit_high(credit_input):
    a = 600
    b = 850
    c = 850
    x = credit_input

    return member_value(a, b, c, x)


def amount_low(amount_input):
    a = 1_000
    b = 1_000
    c = 4_000
    x = amount_input

    return member_value(a, b, c, x)


def amount_mid(amount_input):
    a = 3_000
    b = 5_500
    c = 8_000
    x = amount_input

    return member_value(a, b, c, x)


def amount_high(amount_input):
    a = 7_000
    b = 10_000
    c = 10_000
    x = amount_input

    return member_value(a, b, c, x)


def rules_list(credit_list, amount_list):
    items = []
    for i in amount_list:
        for j in credit_list:
            if i <= j:
                items.append(i)
            else:
                items.append(j)

    return items


def rule_high(list_value, risk_list):
    temp_list = []
    for i in risk_list:
        if list_value <= i:
            temp_list.append(list_value)
        else:
            temp_list.append(i)

    return temp_list


def compare(list_item, vector_list, index):
    y = 0
    x = 0
    z = len(vector_list)
    value = 0
    list_values = []
    while y < z:
        if x < 9:
            a = vector_list[x][index]
            if a > list_item:
                list_values.append(a)
            else:
                list_values.append(list_item)
            x += 1
        y += 1
    value = max(list_values)
    return value


def agg_vector(vector_list):
    temp_list = []
    for i in vector_list[0]:
        temp_list.append(i)

    return_list = []
    for index, this_item in enumerate(temp_list):
        value = compare(this_item, vector_list, index)
        return_list.append(value)

    return return_list


def numerator(input1, input2):
    value = 0
    for index, i in enumerate(input1):
        value += input1[index] * input2[index]

    return value


def defuzz(output_list):
    risk_avg = [0.0, 7.5, 22.5, 37.5, 52.5, 67.5, 82.5, 95]
    denom = sum(output_list)
    numer = numerator(output_list, risk_avg)

    if denom != 0:
        return numer / denom
    else:
        return 0
