# 3. An e-commerce site tracks the purchases made each day. The product that is purchased
# the most one day is the featured product for the following day. If there is a tie for the product
# purchased most frequently, those product names are ordered alphabetically ascending and
# the last name in the list is chosen.[Amazon]


# ['yellowShirt', 'redHat', 'blackShirt', 'bluePants', 'redHat','pinkHat', 'blackShirt', 'yellowShirt',
# 'greenPants', 'greenPants', 'greenPants']
# 'yellowShirt' - 2
# 'redHat' - 2
# 'blackShirt' - 2
# 'bluePants' - 1
# 'greenPants' - 3
# 'pinkHat' - 1
# Output - greenPants

def featured_product(purchases):

    product_count = {}
    for product in purchases:
        if product in product_count:
            product_count[product] += 1
        else:
            product_count[product] = 1

    max_count = max(product_count.values())
    max_products = [product for product, count in product_count.items() if count == max_count]
    max_products.sort()
    return max_products[-1]


#driver code
purchases = ['yellowShirt', 'redHat', 'blackShirt', 'bluePants', 'redHat','pinkHat', 'blackShirt', 'yellowShirt','greenPants', 'greenPants', 'greenPants']
result =  featured_product(purchases)
print(result)
