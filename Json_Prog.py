import json


with open("scoring.json") as file:
    data = json.load(file)

res = 0

for test in data["scoring"]:
    for task in test["required_tests"]:
        answer = input()
        if answer == "ok":
            res += test["points"] / len(test["required_tests"])

print(int(res))