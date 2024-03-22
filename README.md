# Repository Documentation

## Overview

This repository contains a Python script designed to increment the last numerical value found in a README file. Additionally, it includes scripts for automating the process of running the script, committing the changes, and pushing them to a Git repository on both Windows and Linux systems.

### Python Script: `addREADME.py`

The `addREADME.py` script automatically searches for the last number in the README.MD file, increments it by one, and saves the changes back to the file. This script is updated to start counting from 1 if no numbers are present in the README. This is useful for versioning or tracking incremental changes without manual updates.

#### Usage

```bash
python addREADME.py
```

### Windows Automation: `update_readme.bat`

For Windows users, a batch script automates the running of the `addREADME.py` script, adding the modified README.MD to git, committing the change, and pushing it to the repository.

#### Creating the Batch Script

1. Open Notepad or your preferred text editor.
2. Copy and paste the following commands:

```cmd
@echo off
python addREADME.py
git add README.md
git commit -m "Update README.MD"
git push
```

3. Save the file as `update_readme.bat` in the same directory as `addREADME.py`.

#### Running the Script

Double-click on `update_readme.bat` or execute it from the command line.

### Linux Automation: `update_readme.sh`

For Linux users, a Bash script is provided to perform the same actions as the Windows batch file.

#### Creating the Bash Script

1. Open a text editor.
2. Copy and paste the following script:

```bash
#!/bin/bash
python addREADME.py
git add README.md
git commit -m "Update README.MD"
git push
```

3. Save the file as `update_readme.sh` in the same directory as `addREADME.py`.
4. Make the script executable by running `chmod +x update_readme.sh` from the terminal.

#### Running the Script

Execute the script from the terminal with `./update_readme.sh`.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
