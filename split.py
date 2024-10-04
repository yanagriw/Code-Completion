#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--cursor_pos", default=(262, 41), type=tuple, help="Cursor position.")
parser.add_argument("--file_path", default="examples/task2.py", type=str, help="Name of file to split.")
parser.add_argument("--output_path", default="splitted_examples/50", type=str, help="Output file path.")

def split_code(file_path, position):
    x, y = position  # x: line number (1-based), y: column number (1-based)

    prefix = ""

    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Convert 1-based index to 0-based for internal processing
        line_index = x - 1
        column_index = y - 1

        if line_index >= len(lines):
            raise ValueError("Line number exceeds the total number of lines in the file.")

        for i, line in enumerate(lines):
            if i < line_index:  # Before the specified line
                prefix += line
            elif i == line_index:  # The specified line
                if column_index > len(line):
                    raise ValueError("Column number exceeds the length of the line.")

                prefix += line[:column_index]  # Code before the specified position
                middle = line[column_index:].split('\n')[0]  # Code after the position till the end of the line
                suffix = '\n'
            else:  # After the specified line
                suffix += line

    return prefix, middle, suffix

def main(args: argparse.Namespace):
    prefix, middle, suffix = split_code(args.file_path, args.cursor_pos)

    result = f"<fim_prefix>{prefix}<fim_suffix>{suffix}<fim_middle>"

    # Save the result to a text file
    with open(f"{args.output_path}.txt", 'w') as output_file:
        output_file.write(result)

    # Save the annotation to a text file
    with open(f"{args.output_path}_annot.txt", 'w') as output_file:
        output_file.write(middle)

if __name__ == "__main__":
    args = parser.parse_args([] if "__file__" not in globals() else None)
    main(args)