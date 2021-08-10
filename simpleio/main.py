import argparse
import sys
import sio_parser
import gas
import masm
import nasm

parser = argparse.ArgumentParser("Convert SimpleIO code to assembly.")
parser.add_argument(
    "files", metavar="N", type=str, nargs="+", help="A simpleio file to convert"
)

args = parser.parse_args()

for file in args.files:
    try:
        with open(file) as f:
            text = f.read()
            instructions = sio_parser.parse(text)
            print(instructions)
    except FileNotFoundError:
        sys.stderr.write(f"SIO ERROR: FILE '{file}' CANNOT BE FOUND.\n")
    except sio_parser.ParseError as e:
        sys.stderr.write(e.value + "\n")
