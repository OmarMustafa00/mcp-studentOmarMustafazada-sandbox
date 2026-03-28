def average_ratios(numbers):
    if not numbers:
        return 0
    total = 0
    valid_count = 0
    for num in numbers:
        if num == 0:
            print("Uyari: Sifira bolunme hatasi onlendi, bu deger atlandir.")
            continue
        total += 100 / num
        valid_count += 1
    
    return total / valid_count if valid_count > 0 else 0

print(average_ratios([10, 5, 0]))
