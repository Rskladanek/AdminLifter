# AdminLifter - README

## 📌 Overview
**AdminLifter** is a Windows-based tool designed for privilege escalation. It leverages service functionalities and VBScript execution to demonstrate security techniques and explore vulnerabilities.

---

## 🚧 Work in Progress
This project is under active development. Features and documentation will be updated as progress is made.

### Key Challenges:
- Bypassing service permission restrictions.
- Ensuring reliable execution of VBScript files.
- Navigating virtual machine constraints for realistic testing.

---

## 🛠️ How It Works
### 1. **Batch File (`bypass.bat`):**
- Allows running applications that require admin privileges without a UAC prompt.
- **Usage:** Drag and drop an executable onto `bypass.bat`. It will run with user-level privileges.

```batch
cmd /min /C "set __COMPAT_LAYER=runasinvoker && start "" "%1""
```

### 2. **VBScript (`bhservice_task.vbs`):**
- Gathers system information and logs it to `C:\windows\temp\bhpoutput.txt`.
- **Features:**
  - Extracts OS, memory, hardware, and BIOS details using WMI.

### 3. **Python Service (`main.py`):**
- Implements a Windows service using Python.
- Periodically executes the VBScript.

**Key Steps:**
1. Copies `bhservice_task.vbs` to `C:\Windows\TEMP`.
2. Executes it with `cscript.exe`.
3. Deletes the script after execution.

---

## 📂 File Structure
```
├── bypass.bat                # Batch file for bypassing admin privileges
├── main.py                   # Entry point for the Python service
├── modules/                  # Directory for additional scripts
│   ├── bhservice_task.vbs    # VBScript for system info gathering
│   └── blackhatService.py    # Python service implementation
├── README.md                 # Documentation (this file)
├── requirements.txt          # Python dependencies
```

---

## 📝 Requirements
- **Python 3.x**
- `pywin32` library (install with `pip install pywin32`)

### Additional Setup
- Place the VBScript in the `modules/` directory.
- Run the Python service with administrator privileges.

---

## 🚀 Usage
1. **Privilege Bypass:**
   - Drag and drop an executable onto `bypass.bat`.
2. **System Information Gathering:**
   - Use the Python service to periodically gather system details.

---

## ⚠️ Disclaimer
This tool is for educational purposes only. Unauthorized use is strictly prohibited. The author is not responsible for misuse of this tool.