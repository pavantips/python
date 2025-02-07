product = "iphones and android phones"

lett_d = {}

for c in product:
    if c not in lett_d:
        lett_d[c] = 0
    lett_d[c] = lett_d[c] + 1
keys = list(lett_d.keys())

print (lett_d)
print (keys)

max_value = keys[0]
for key in keys:
    if lett_d[key] > lett_d[max_value]:
        max_value = key

print ("ok, so the letter that appeared the most is", max_value)

#####

placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

d = {}

for c in placement:
    if c not in d:
        d[c] = 0
    d[c] = d[c] + 1
keys = list(d.keys())

key_with_min_value = keys[0]
for key in keys:
    if d[key] < d[key_with_min_value]:
        key_with_min_value = key

print ("ok, so the letter that appeared the most is", key_with_min_value)
