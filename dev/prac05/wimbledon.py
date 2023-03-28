filename = "wimbledon.csv"
champion_to_count = {}
countries = set()
with open(filename, "r", encoding="utf-8-sig") as in_file:
    next(in_file)
    for line in in_file:
        text = line.split(',')
        champions = text[2].split("\n")
        for champion in champions:
            if champion in champion_to_count:
                champion_to_count[champion] += 1
            else:
                champion_to_count[champion] = 1
        countries.add(text[1])
print("Wimbledon Champions: ")
for champion, count in champion_to_count.items():
    print(f"{champion}  {count}")
print(f"These {len(countries)} countries have won Wimbledon:")
print(", ".join(countries))
