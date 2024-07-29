#! /usr/bin/bash
pyinstaller --onefile cpm.py 
cp ./dist/cpm /usr/bin/
rm -rf build dist *.spec
echo "[+] CPM was installed"
