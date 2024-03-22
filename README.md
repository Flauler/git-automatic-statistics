# Repository Documentation

## Overview

This repository contains a Python script designed to increment the last numerical value found in a README file. Additionally, it includes a batch file for automating the process of running the script, committing the changes, and pushing them to a Git repository on Windows systems.

### Python Script: `addREADME.py`

The `addREADME.py` script automatically searches for the last number in the README.MD file, increments it by one, and saves the changes back to the file. This is particularly useful for versioning or tracking incremental changes without manual updates.

#### Usage

```bash
python addREADME.py
```

### Batch Script: `update_readme.bat` (for Windows)

The batch script automates the process of running the `addREADME.py` script, adding the modified README.MD to git, committing the change, and pushing it to the repository.

#### Usage

To run the batch script, simply double-click on it or execute it from the command line:

```cmd
update_readme.bat
```

## Linux Equivalent Script

For Linux systems, an equivalent script can be created to perform the same actions. This script uses Bash instead of batch scripting.

### Bash Script: `update_readme.sh`

```bash
#!/bin/bash
python addREADME.py
git add README.md
git commit -m "Update README.MD"
git push
```

#### Usage

1. Make the script executable:
```bash
chmod +x update_readme.sh
```

2. Run the script:
```bash
./update_readme.sh
```

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
