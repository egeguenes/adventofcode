input = "input.txt"

def get_lines(path):
    with open(path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        return lines

def part1():
    lines = get_lines(input)
    left = []
    right = []
    diff = 0

    for line in lines:
        line = line.replace("   "," ")
        nums = line.split()
        right.append(int(nums[0]))
        left.append(int(nums[1]))

    for index in range(len(right)):
        diff += abs(left[index] - right[index])

    print(diff)

def part2():
    lines = get_lines(input)
    left = []
    right = {}

    for line in lines:
        line = line.replace("   "," ")
        nums = line.split()
        left.append(int(nums[0]))
        occurance = int(nums[1])

        if occurance not in right:
            right[occurance] = 0

        right[occurance] += 1

    sum = 0
    for index in left:
        if index in right:
            sum += index * right[index]

    print(sum)

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
