"""EPUB to TXT — Extract an EPUB to a clean UTF-8 text file with chapter breaks."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='epub_to_txt',
        description='Extract an EPUB to a clean UTF-8 text file with chapter breaks.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('EPUB to TXT')
    print('A book file you can grep.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
