import argparse
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("dir")

args = parser.parse_args()

target_dir = Path(args.dir)

if not target_dir.exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)
elif not target_dir.is_dir():
    print("Provided path is not a valid directory")
    raise SystemExit(1)

for entry in target_dir.iterdir():
    print(entry.name)

