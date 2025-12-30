# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import os
import hashlib
from collections import defaultdict

class DuplicateFinder:
    def __init__(self, directory, recursive=False):
        self.directory = directory
        self.recursive = recursive

    def get_file_hash(self, filepath, chunk_size=8192):
        hasher = hashlib.md5() # MD5 is fast enough for dup checking, though collisions are theoretically possible, unlikely for files.
        try:
            with open(filepath, 'rb') as f:
                while chunk := f.read(chunk_size):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except OSError:
            return None

    def find_duplicates(self):
        hashes = defaultdict(list)
        
        # Walk logic
        if self.recursive:
            for root, _, files in os.walk(self.directory):
                for filename in files:
                    filepath = os.path.join(root, filename)
                    file_hash = self.get_file_hash(filepath)
                    if file_hash:
                        hashes[file_hash].append(filepath)
        else:
            # Non-recursive
            with os.scandir(self.directory) as entries:
                for entry in entries:
                    if entry.is_file():
                        file_hash = self.get_file_hash(entry.path)
                        if file_hash:
                            hashes[file_hash].append(entry.path)
                            
        # Filter for only hashes with > 1 file
        duplicates = {k: v for k, v in hashes.items() if len(v) > 1}
        return duplicates

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
