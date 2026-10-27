# Program to read a name from the keyboard and generate a Converse-style ID

import csv
import pathlib
import tkinter.filedialog

def make_id(name: dict[str, str]) -> str:
    lastname = name['lastname']

    # Remove any unwanted characters from the last name
    unwanted = " '"
    for c in unwanted:
        lastname = lastname.replace(c, '')

    # Now get the other names and extract the first two initials
    #   (or one, if there aren't two)
    othernames: list[str] = name['othernames'].split()
    initials = othernames[0][0] # First initial
    if len(othernames) > 1: # Person has a middle name
        initials = initials + othernames[1][0] # Use the first middle initial
    return (initials + lastname + '001').lower()

def read_names(filename: str) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            record = row.copy()
            # Get rid of comma in last name and anything after
            last = record['lastname']
            if ',' in last:
                last = last[:last.find(',')]
            record['lastname'] = last.strip()
            record['othernames'] = record['othernames'].strip()
            result.append(record)
    return result

def make_backup_if_needed(outfilename: str) -> None:
    """If file OUTFILENAME exists, make a backup of it, with the same name
        but a '.bak' file extension.  If the backup file already exists, it
        is simply overwritten."""
    outfile = pathlib.Path(outfilename)
    if outfile.exists():
        backupfile = outfile.with_suffix('.bak')
        outfile.move(backupfile)

def write_userids(records: dict[str, str], filename: str) -> None:
    with open(filename, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=records[0].keys())
        writer.writeheader()
        for rec in records:
            writer.writerow(rec)
        

def main(args: list[str]) -> int:
    infilename: str = \
            tkinter.filedialog.askopenfilename(filetypes=(
                                                   ('CSV files', '*.csv'),
                                                   ('All files', '*.*')
                                                   ),
                                               title='File of names')
    namelist: list[dict[str, str]] = []
    try:
        namelist = read_names(infilename)
    except FileNotFoundError:
        print('No file specified from which to read names, exiting.')
    else:
        #print(namelist[:20])
        for name in namelist:
            name['userid'] = make_id(name)
        #print()
        #print(namelist[:20])
        outfilename: str = \
                tkinter.filedialog.asksaveasfilename(filetypes=(
                                                       ('CSV files', '*.csv'),
                                                       ('All files', '*.*')
                                                       ),
                                                   title="File for user ID's")
        if len(outfilename) > 0: # Can't use FileNotFoundError
            make_backup_if_needed(outfilename)
            write_userids(namelist, outfilename)
        else:
            print("No file specified to write out the user ID's, exiting.")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
