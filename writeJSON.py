from group import group
import json


if __name__ == '__main__':
    with open('group.txt', 'w') as output:
        json.dump(group, output)
    with open('group.txt', 'r') as input:
        inputs = json.load(input)
        print(inputs)
