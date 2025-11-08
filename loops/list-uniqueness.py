items = ["apple", "mango", "banana", "apple", "litchi"]
unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate found", item)
        
    unique_item.add(item)