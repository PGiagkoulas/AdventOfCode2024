INPUT_DIR = "./inputs"


def read_input_file(filename:str) -> str:
    try:
        with open(f"{INPUT_DIR}/{filename}", 'r') as in_file:
            return [line.strip() for line in in_file]
    except IOError:
        print(f"[!] Input file with name {filename} does not exist in input directory {INPUT_DIR}")