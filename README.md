# SF2PWN
First Step to pwn (FS2PWN) is script to automate some tasks.

 - Ping sweep.
 - Hostname discovery.
 - Port scanner for some interesting
   ports like HTTP, MSSQL, winRM and more.


# Donwload
You can donwload binary release file [FS2PWN.exe](https://github.com/0xAbdullah/SF2PWN/releases/download/0.1/FS2PWN.exe) v0.1

# Usage

```
PS C:\Temp> ./FS2PWN.exe -t 10.10.11.0/24
# FS2PWN | Coded by Abdullah AlZahrani https://github.com/0xAbdullah
[*] Let's GO.

[H] IP: 10.10.11.2 Hostname: DC.corp.example
[P] RDP 3389 open.
[P] winRM 5985 open.
[P] SMB 445 open.

[H] IP: 10.10.11.5 Hostname: SQL-Server
[P] RDP 3389 open.
[P] winRM 5985 open.
[P] SMB 445 open.
[P] MSSQL 1433 open.
...   ...   ...   ...

...   ...   ...   ...
[H] IP: 10.10.11.100 Hostname: Backup-Server
[P] RDP 3389 open.
[P] winRM 5985 open.
[P] SMB 445 open.
[I] I found 8 hosts up!
```

### ToDo (Coming soon)
```
Check SMB share folders
```
