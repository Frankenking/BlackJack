@echo off

echo !WARNING! You Must Have Python Installed to build this program!
echo Continue?
pause

pip install pyinstaller
echo PyInstaller Successfully Installed
echo Building...
timeout(1)

pyinstaller BlackJack.py
echo Your Build if Finished! It can be found in the new dist folder under BlackJack.exe
pause