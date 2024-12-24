# AdminLifter - README

## Overview
**BlackHatService** is a Windows-based tool designed for privilege escalation by leveraging service functionalities and executing VBScript files at regular intervals. It serves as a framework to demonstrate privilege escalation techniques and explore potential security vulnerabilities.

### Work in Progress
This project is currently under development. Features and documentation will be updated as progress is made. Testing and debugging are particularly challenging, as the tool interacts with critical Windows services. 

### Challenges
Implementing and testing **BlackHatService** is inherently complex due to the nature of the privilege escalation process. Thorough testing requires an environment that simulates a secure system without risking a production machine. To address this, efforts are being made to work around security mechanisms on a virtual machine. This setup allows testing under controlled conditions, but it also reveals the sophisticated layers of security that must be bypassed.

Some of the hurdles include:
- Bypassing service permission restrictions.
- Ensuring reliable execution of VBScript files.
- Navigating virtual machine-specific constraints, which can impact realistic behavior.

---

## How It Works

The project consists of two main components: 

1. **The VBScript (`bhservice_task.vbs`):**
   - Gathers detailed information about the operating system, computer, and hardware.
   - Outputs the collected information to a file located in `C:\windows\temp\bhpoutput.txt`.

   **Key Features of `bhservice_task.vbs`:**
   - Uses WMI (Windows Management Instrumentation) to extract system details.
   - Writes information such as OS version, memory statistics, BIOS version, and processor details.

2. **The Python Service (`main.py`):**
   - A Windows service implemented using Python and the `pywin32` library.
   - Periodically copies the VBScript to a target directory and executes it using `cscript.exe`.
   - Deletes the VBScript after execution to reduce its footprint.

---

## File Structure
 ├── .venv # Virtual environment 
 ├── .gitignore # Git ignore file 
 ├── bhservice_task.vbs # VBScript executed by the service 
 ├── main.py # Python service code 
 ├── README.md # Documentation 
 ├── requirements.txt # Python dependencies

 ---

## Python Service Details (`main.py`)

- **Service Name:** BlackHatService
- **Service Description:** Runs a VBScript at regular intervals. 
- **Core Functionality:**
  1. Initializes a Windows service that uses `win32serviceutil`.
  2. Copies `bhservice_task.vbs` from the source directory to the target directory (`C:\Windows\TEMP`).
  3. Executes the VBScript using `cscript.exe`.
  4. Deletes the VBScript after execution to minimize its presence.

---

## VBScript Details (`bhservice_task.vbs`)

The script uses WMI to query system information and writes it to a log file (`C:\windows\temp\bhpoutput.txt`). Below are the categories of information retrieved:
- **Operating System:**
  - Name, version, service pack, manufacturer, Windows directory, locale.
- **Memory:**
  - Free physical memory, total virtual memory, available virtual memory, page file size.
- **Computer System:**
  - Name, manufacturer, model, time zone, total physical memory.
- **Processor:**
  - Architecture, description.
- **BIOS:**
  - Version.

---

## Requirements
- Python 3.x
- `pywin32` library (install via `pip install pywin32`)

### Additional Setup
- Ensure the VBScript is placed in the source directory (`C:\Users\tim\work`).
- Run the service with administrator privileges to access required system functions.

---

## Disclaimer
This tool is for educational purposes only. Unauthorized use is strictly prohibited. The author does not condone malicious activity and is not responsible for misuse of this tool.

---