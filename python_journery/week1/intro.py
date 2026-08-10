# intro.py — Day 1: temperature converter + bill splitter

# Part A — temperature
celsius = float(input("Temperature in °C: "))   # input() gives str → convert
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius}°C = {fahrenheit:.1f}°F")

# Part B — bill splitter
bill = float(input("Bill amount (₹): "))
tip_pct = float(input("Tip %: "))
friends = int(input("Split between how many people? "))

total = bill + bill * tip_pct / 100
share = total / friends            # exact share → float
whole = int(total) // friends      # whole rupees each → floor division
left = int(total) % friends        # rupees left over

print(f"Total with tip: ₹{total:.2f}")
print(f"Each pays: ₹{share:.2f}")
print(f"Whole-rupee split: ₹{whole} each, ₹{left} left over")
