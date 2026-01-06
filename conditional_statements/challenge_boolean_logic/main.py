seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

# 1. True if seasonal AND stock > threshold
overstock_risk = seasonal and (current_stock > high_stock_threshold)

# 2. True if NOT selling well AND NOT already on sale
discount_eligible = (not selling_well) and (not on_sale)

# 3. Discount if either condition holds
make_discount = overstock_risk or discount_eligible

# 4. Output
print("Should the item be discounted?", make_discount)