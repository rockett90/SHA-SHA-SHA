# SHA-SHA-SHA: A Summary
A Simple GUI for generating and/or comparing hexadecimal hashes using the SHA-1, 256, 384 or 512 algorithm(s) using Python hashlib and Tkinter.

# GUI Example
Use the interface to either generate a hexadecimal SHA from a file, or compare a file against a know hexadecimal SHA to check their contents match.

![example](https://github.com/rockett90/SHA-SHA-SHA/assets/149118299/fd5575a7-995f-4eb7-bd5a-0046f5e19bd5)

# Windows Executable
Steps to create an executable from the Python code:

1. Open Command Prompt

2. Install Pyinstaller
```bash
pip install pyinstaller
```

3. Change to the directory the .py and .png files are stored
```bash
cd C:\Users\YourName\WorkingDir
```

4. Build the executable
```bash
pyinstaller --onefile --noconsole --add-data ".\icon.png:." SHA_Gen-Compare_GUI.py
```

