challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

a = challenge[2][1]
b = challenge[2][0]
c = challenge[3]
print(f"My {a}! The {b} do {c}!")

aa = trial[2]["goggles"]
bb = trial[2]["eyes"]
cc = trial[3]
print(f"My {aa}! The {bb} do {cc}!")

aaa = nightmare[0]["user"]["name"]["first"]
bbb = nightmare[0]["kumquat"]
ccc = nightmare[0]["d"]
print(f"My {aaa}! The {bbb} do {ccc}!")