seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

# define a boolean variable
overstock_risk = 
#  overstock_risk = seasonal and current_stock > high_stock_threshold
#  seasonal = True
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

#   It looks like you’ve started defining overstock_risk but haven’t finished the expression yet. Think step-by-step:

overstock_risk should be True exactly when the item is seasonal and current_stock exceeds the threshold.
discount_eligible should be True when the item is not selling well and not already on sale.
make_discount is True if either of the above is True.
Finally print the result.
Try filling in the blanks:

python


1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
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
Run this in the editor’s Output Panel—does it print the expected True/False?


## Explain me my current code
