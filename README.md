# AdminLifter - README

## 📌 Overview
**AdminLifter** is a Windows-based tool designed for **privilege escalation**. It leverages service functionalities and VBScript execution to demonstrate security techniques and explore potential vulnerabilities.

> **Note:** This project has reached its final stage of development and is no longer actively maintained.

---

## ⚠️ Compatibility
- **Windows 11**: The `runasinvoker` bypass no longer works reliably on Windows 11. It may only function for **specific executables** (e.g., those without a manifest enforcing admin privileges).
- **Older Windows Versions (Windows 7, 8, 10)**: The bypass typically works as expected.

---

## 🚧 Project Status
This project is **completed**. No further updates or new features are planned.  
- Tested successfully on older Windows versions.  
- Limited functionality on Windows 11 due to stricter UAC and manifest rules.

---

## 🛠️ How It Works

### 1. **Batch File (`bypass.bat`):**
- Allows running programs that request admin privileges **without** triggering a UAC prompt (on supported Windows versions).
- **Usage:** Drag and drop an executable onto `bypass.bat`.  
- **Important:** On Windows 11, this bypass only works for select executables that do not have an embedded `requireAdministrator` manifest.

```batch
:: Bypass script for older Windows versions (runasinvoker trick)
cmd /min /C "set __COMPAT_LAYER=runasinvoker && start "" "%1""
```

## 2. VBScript (`bhservice_task.vbs`)

Collects system information and appends it to `C:\Windows\TEMP\bhpoutput.txt`.

**Features:**
- Gathers OS, memory, hardware, and BIOS data via WMI.
- Intended for demonstration and testing of system info retrieval.

## 3. Python Service (`main.py` + `blackhatService.py`)

Implements a Windows service in Python using `pywin32`.

**Workflow:**
1. Copies `bhservice_task.vbs` to `C:\Windows\TEMP`.
2. Executes the script via `cscript.exe`.
3. Removes the script after execution to keep the system clean.

### Key Steps:
1. Copies `bhservice_task.vbs` to `C:\Windows\TEMP`.
2. Executes it with `cscript.exe`.
3. Deletes the script after execution.

----
## 📂 File Structure
```
├── bypass.bat                # Batch file for bypassing admin privileges on older Windows
├── main.py                   # Entry point for the Python service
├── modules/
│   ├── bhservice_task.vbs    # VBScript for system info gathering
│   └── blackhatService.py    # The actual Python service implementation
├── README.md                 # Documentation (this file)
├── requirements.txt          # Python dependencies (e.g., pywin32)
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

1. **Privilege Bypass (Older Windows)**  
   - Drag and drop an executable onto `bypass.bat`.  
   - If the executable does **not** have a strict admin manifest, it will open without the usual UAC prompt (on older systems).

2. **System Information Gathering**  
   - Use `main.py install` to register the Python service, then `main.py start` to launch it.  
   - The service will periodically collect system information via `bhservice_task.vbs`.

**Stopping & Removing the Service**
```bash
python main.py stop
python main.py remove
```

---

## ⚠️ Disclaimer
This tool is for educational and testing purposes only. Unauthorized or malicious use is strictly prohibited. The author and contributors bear no responsibility for the consequences of unauthorized use. Use responsibly and within the bounds of applicable law.