from utils import read_input_file
import re

if __name__ == '__main__':
    print("Day 1:")
    input = read_input_file("d1-input.txt")
    list1 = []
    list2 = []
    for line in input:
        nums = line.split("   ")
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))
    
    list1.sort()
    list2.sort()
    assert len(list1) == len(list2), "[!] Lists have uneven length!"

    distance = sum((abs(list1[i] - list2[i]) for i in range(len(list1))))
    print(f"[>] Total distance between the two lists: {distance}")

    similarity = sum(num1 * sum((1 for num2 in list2 if num1==num2)) for num1 in list1)
    print(f"[>] Total similarity score between the two lists: {similarity}")

