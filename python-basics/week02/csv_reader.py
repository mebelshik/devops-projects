import csv
from typing import List, Dict


def read_csv(path: str) -> List[Dict[str, str]]:
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]


if __name__ == '__main__':
    sample = 'sample.csv'
    rows = read_csv(sample)
    print(f"Прочитано {len(rows)} строк")
