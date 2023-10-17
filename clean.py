import re
import glob
import tqdm

file_list = glob.glob('solutions/*/question.txt')
for file in tqdm.tqdm(file_list):
    with open(file, 'r') as f:
        question_string = f.read()

    # This pattern assumes that the part you want to keep starts with a capital letter and has spaces or word characters
    pattern = re.compile(r"Can you solve this real interview question\? [^-]+ - (.+)", re.DOTALL)
    match = pattern.search(question_string)
    if match:  # If the pattern is found within the string
        # The first captured group (in parentheses) is the remaining string you're interested in.
        clean_string=match.group(1)
        with open(file + '_clean', 'w') as f:
            f.write(clean_string)