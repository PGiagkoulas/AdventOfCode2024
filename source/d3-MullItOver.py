from utils import read_input_file
import re


def _get_operants(calculation: str) -> list[int]:
    calculation = calculation.replace("mul(", "").replace(")", "")
    return [int(op) for op in calculation.split(',')]


if __name__=="__main__":
    print("Day 3:")
    input = read_input_file("d3-input.txt")
    memory_contents = "".join(input)

    regex_search_results = re.findall(r"mul\(\d{1,3},\d{1,3}\)", memory_contents)

    mul_operants = [_get_operants(operation) for operation in regex_search_results]
    mul_results = [op[0]*op[1] for op in mul_operants]
    mul_sum = sum(mul_results)
    print(f"[>] Sum of multiplications: {mul_sum}")

    mul_cond_iterator = re.finditer(r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))", memory_contents)
    
    enabled = True
    enabled_mul_sum = 0
    for iter_result in mul_cond_iterator:
        operation = iter_result.group()
        if operation == "do()":
            enabled = True
        elif operation == "don't()":
            enabled = False
        elif "mul" in operation:
            if enabled:
                operants = _get_operants(operation)
                enabled_mul_sum += operants[0] * operants[1]
        else:
            print("OPERATION PARSING PROBLEM - RAISING ERROR")
            raise()
    print(f"[>] Sum of multiplications with enables: {enabled_mul_sum}")

