from pathlib import Path

def search_file_for_string(file: Path, search_str: str) -> None:
    """Search the file FILE for the string SEARCH_STR, and print out any
        matches found.  Processes FILE line by line, so it may miss matches
        that span lines."""
    with open(file) as f:
        linenum = 0
        for line in f.readlines():
            linenum += 1 # Adds one to linenum and assigns the result to linenum
            if search_str in line:
                print(f'{file}:{linenum}: {line}', end='')

def search_files(pattern: str, search_str: str) -> None:
    """Search the files matching PATTERN for the string SEARCH_STR,
       and print out any matches found."""
    here: Path = Path('.')
    filelist: list[Path] = list(here.glob(pattern))
    #print(filelist)
    for file in filelist:
        search_file_for_string(file, search_str)

def main(args: list[str]) -> int:
    search_string: str = input('Please enter a string to search for: ')
    file_pattern: str = \
                input('Please enter a pattern telling which files to search: ')
    search_files(file_pattern, search_string)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
