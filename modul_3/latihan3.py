random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

# Filter untuk memisahkan nilai float, int, dan string
data_float = list(filter(lambda x: isinstance(x, float), random_list))
data_int = list(filter(lambda x: isinstance(x, int), random_list))
data_string = list(filter(lambda x: isinstance(x, str), random_list))

# Map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
def map_int_to_dict(number):
    ratusan = number // 100
    puluhan = (number % 100) // 10
    satuan = number % 10
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}

data_int_mapped = list(map(map_int_to_dict, data_int))

# Output
print("Data Float:", data_float)
print("Data int:")
for item in data_int_mapped:
    print(item)
print("Data String:", data_string)
