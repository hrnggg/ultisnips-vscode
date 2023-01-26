from pathlib import Path
import json
from src import UltisnipParser, vim2vscode
import sys

def main():
    argv = sys.argv
    if len(argv) != 2:
        print("Please give a config file path.")
        sys.exit(1)
    config = read_config(argv[1])
    parser = UltisnipParser(
        Path(config["ultisnips-snippets"]).expanduser(),
        Path(config["vscode-snippets"]).expanduser(),
        vim2vscode
    )
    parser.parse_snippets(verbose=True)
    parser.write_snippets()

def read_config(config_file):
    """Reads the config file and returns a dictionary containing
    the ultisnips and vscode snippets directories
    """
    with open(config_file, 'r') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    main()
