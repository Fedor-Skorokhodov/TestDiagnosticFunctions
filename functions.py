def count_customers_groups(n_customers):
    groups = {}
    for customer_id in range(n_customers):
        group = 0
        while customer_id != 0:
            group += customer_id % 10
            customer_id = customer_id // 10
        count = groups.get(group, 0)  # 0 if key don't exists
        groups.update({group: count+1})
    return groups


def count_customers_groups_by_id(n_customers, n_first_id):
    groups = {}
    for customer_id in range(n_first_id, n_first_id+n_customers):
        group = 0
        while customer_id != 0:
            group += customer_id % 10
            customer_id = customer_id // 10
        count = groups.get(group, 0)  # 0 if key don't exists
        groups.update({group: count + 1})
    return groups
