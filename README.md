# Duplicate File Finder

A tool to scan directories for identical files by comparing their content hashes (MD5). It identifies duplicates even if they have different filenames.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **Content-Based**: Uses MD5 hashing to ensure files are actually identical, not just by name.
*   **Recursive Scan**: Digs into subfolders (optional).
*   **Cleanup Mode**: Can automatically delete duplicates, keeping one copy.

## Usage

```bash
python run_finder.py [path] [options]
```

### Options

*   `--recursive`, `-r`: Scan subdirectories.
*   `--delete`: **DANGER**. Automatically deletes all copies except the first one found for each duplicate set.

### Example

**1. Scan for Duplicates**
```bash
python run_finder.py ./my_photos -r
```

**Output:**
```
Found 2 sets of duplicates:

Hash: d41d8cd98f00b204e9800998ecf8427e
  [0] ./my_photos/IMG_001.jpg
  [1] ./my_photos/backup/IMG_001_copy.jpg
----------------------------------------
...
```

**2. Delete Duplicates**
```bash
python run_finder.py ./downloads --delete
```

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
