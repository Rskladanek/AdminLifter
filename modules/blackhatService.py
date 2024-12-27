import os
import shutil
import subprocess
import sys
import win32event
import win32service
import win32serviceutil
import servicemanager


SRC_DIR = 'C:\\Users\\tim\\work'
TGT_DIR = 'C:\\Windows\\TEMP'


class BlackHatService(win32serviceutil.ServiceFramework):
    """
    A Windows service that periodically runs a VBScript.
    """
    _svc_name_ = "BlackHatService"
    _svc_display_name_ = "Black Hat Service"
    _svc_description_ = (
        "Runs a VBScript at regular intervals. "
        "What could possibly go wrong?"
    )


    def __init__(self, args):
        super().__init__(args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.vbs_script_path = os.path.join(TGT_DIR, 'bhservice_task.vbs')
        self.timeout = 1000 * 60  # 1 minute timeout


    def SvcStop(self):
        """Called when the service is being stopped."""
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)


    def SvcDoRun(self):
        """Main loop of the service."""
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        self.run_service()


    def run_service(self):
        while True:
            # Wait for the stop signal or timeout
            ret_code = win32event.WaitForSingleObject(self.hWaitStop, self.timeout)
            if ret_code == win32event.WAIT_OBJECT_0:
                servicemanager.LogInfoMsg("The service is stopping")
                break

            # Copy and execute the VBScript
            src = os.path.join(SRC_DIR, 'bhservice_task.vbs')
            shutil.copy(src, self.vbs_script_path)
            subprocess.call(["cscript.exe", self.vbs_script_path], shell=False)

            # Remove the VBScript after execution
            os.unlink(self.vbs_script_path)


