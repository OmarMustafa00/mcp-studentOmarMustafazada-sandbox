def calculate_values(data, multiplier=1.15):
    return [d * multiplier for d in data]

def print_totals(values):
    for val in values:
        print(f"Total: {val:.2f}")

def log_results(values, filename="log.txt"):
    with open(filename, "a") as f:
        f.write(str(values) + "\n")

def process_data(data):
    res = calculate_values(data)
    print_totals(res)
    log_results(res)
    return res
