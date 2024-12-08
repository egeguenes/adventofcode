import os

input = "input.txt"

def get_lines(path):
    with open(path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        return lines

def get_arrays():
    lines = get_lines(input)
    right = []
    left = []

    for line in lines:
        line = line.replace("   "," ")
        nums = line.split()
        right.append(int(nums[0]))
        left.append(int(nums[1]))

    return sorted(left), sorted(right)

def main():
    right, left = get_arrays()
    diff = 0

    for index in range(len(right)):
        diff += abs(left[index] - right[index])

    print(diff)

if __name__ == "__main__":
    main()
