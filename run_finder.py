# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from finder.core import DuplicateFinder

def main():
    parser = argparse.ArgumentParser(description="Find duplicate files based on content hash.")
    parser.add_argument("path", help="Directory to scan")
    parser.add_argument("--recursive", "-r", action="store_true", help="Scan recursively")
    parser.add_argument("--delete", action="store_true", help="Delete duplicates (Keep one copy). USE WITH CAUTION.")
    
    args = parser.parse_args()

    if not os.path.isdir(args.path):
        print(f"Error: Directory '{args.path}' not found.")
        sys.exit(1)

    print(f"Scanning '{args.path}' for duplicates...")
    finder = DuplicateFinder(args.path, recursive=args.recursive)
    duplicates = finder.find_duplicates()

    if not duplicates:
        print("No duplicates found.")
        sys.exit(0)

    print(f"Found {len(duplicates)} sets of duplicates:\n")
    
    total_freed = 0
    
    for file_hash, paths in duplicates.items():
        print(f"Hash: {file_hash}")
        for i, path in enumerate(paths):
            print(f"  [{i}] {path}")
        
        if args.delete:
            # Keep the first one (index 0), delete the rest
            # But wait, we should ask or just do it? The flag says "USE WITH CAUTION".
            # Let's delete strictly.
            keep = paths[0]
            print(f"  -> Keeping: {keep}")
            for path in paths[1:]:
                try:
                    size = os.path.getsize(path)
                    os.remove(path)
                    print(f"  -> Deleted: {path}")
                    total_freed += size
                except OSError as e:
                    print(f"  -> Error deleting {path}: {e}")
        print("-" * 40)

    if args.delete:
        print(f"\nTotal space freed: {total_freed / 1024 / 1024:.2f} MB")
    else:
        print("\nRun with --delete to remove duplicates (keeps the first file found in each set).")

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
