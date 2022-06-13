my_list = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola", ]
}
for dict_key in my_list:
    print(f"Idę do {dict_key.capitalize()} i kupuje tam  {my_list[dict_key]}")

produkty = [len(my_list[dict_key])+len(my_list[dict_key])]
print(f"W sumie kupuje {produkty} produktów")

#Kod wydaje się nagle nie działać 