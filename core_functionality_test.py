cores_load = [10, 95, 45, 90, 88, 15, 99]
def load_limit(some_list, limit):
    at_thelimit_count = 0
    for i in some_list:
        if i >= limit:
            at_thelimit_count = at_thelimit_count +1
    return at_thelimit_count
cores_atlimit = load_limit(cores_load, 90)
print(cores_atlimit)