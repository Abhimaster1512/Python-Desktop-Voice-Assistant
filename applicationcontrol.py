import subprocess


def open_application(command):

    apps = {

        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "command prompt": "cmd.exe",
        "task manager": "taskmgr.exe",
        "file explorer": "explorer.exe",
        "control panel": "control.exe",

        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",

        "vs code": r"C:\Users\User\AppData\Local\Programs\Microsoft VS Code\Code.exe",

        "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",

        "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",

        "powerpoint": r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
    }


    for app_name, app_path in apps.items():

        if app_name in command:

            try:
                subprocess.Popen(app_path)

                return f"Opening {app_name}"

            except Exception as e:
                return f"Error opening {app_name}: {e}"


    return "Application not found"