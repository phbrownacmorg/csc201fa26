# Program to read a name from the keyboard and generate a Converse-style ID

import csv

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

def write_userids(records: dict[str, str], filename: str) -> None:
    with open(filename, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=records[0].keys())
        writer.writeheader()
        for rec in records:
            writer.writerow(rec)
        

def main(args: list[str]) -> int:
    infilename: str = 'names.csv'
    outfilename: str = 'userids.csv'
    namelist: list[dict[str, str]] = read_names(infilename)
    print(namelist[:20])
    for name in namelist:
        name['userid'] = make_id(name)
    print()
    print(namelist[:20])
    write_userids(namelist, outfilename)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
