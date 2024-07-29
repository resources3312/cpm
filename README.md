# C-Package-Manager
C-Package-Manager, or CPM is most badly package manager for C libraries, 
which was written on Python ironic isn`t?) Maybe my little project will useful
for people, which want understand how work package manager on simple example.
Course, pm how apt or pacman much more difficult than my dwarf, but the principle
is the same. You can run CPM server, and choose need cpm server via client. Also,
you can add you own library for one command, read man page.. In general, 
have fun :>>

# Installing Server
```bash
git clone https://github.com/resources3312/cpm.git

cd cpm/cpmserver

chmod +x cpm*.py install.sh

./cpm_server_test.py  

./install.sh
```

# Installing Client
```bash
git clone https://github.com/resources3312/cpm.git

cd cpm/cpmclient

chmod +x cpm*.py install.sh

./cpm_client_test.py  

./install.sh
```
