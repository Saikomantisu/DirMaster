import urllib3

print("""
┏━━━┓╋╋╋╋╋╋╋╋┏┓╋╋╋╋╋╋╋╋╋╋┏━━━┓
┗┓┏┓┃╋╋╋╋╋╋╋┏┛┗┓╋╋╋╋╋╋╋╋╋┃┏━┓┃
╋┃┃┃┣┳━┳━━┳━┻┓┏╋━━┳━┳┓╋┏┓┃┗━━┳━━┳━━┳━┓┏━┓┏━━┳━┓
╋┃┃┃┣┫┏┫┃━┫┏━┫┃┃┏┓┃┏┫┃╋┃┃┗━━┓┃┏━┫┏┓┃┏┓┫┏┓┫┃━┫┏┛
┏┛┗┛┃┃┃┃┃━┫┗━┫┗┫┗┛┃┃┃┗━┛┃┃┗━┛┃┗━┫┏┓┃┃┃┃┃┃┃┃━┫┃
┗━━━┻┻┛┗━━┻━━┻━┻━━┻┛┗━┓┏┛┗━━━┻━━┻┛┗┻┛┗┻┛┗┻━━┻┛
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏━┛┃
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗━━┛
            </Devel𝕠oped By HeX_006>
""")

url = input("Enter The Website You Want To Scan: ")
path = input("Enter The Wordlist Path: ")
print()

file = open(path, 'r')
fileRead = file.read()
fileSplit = fileRead.splitlines()
dir = []

Http = urllib3.PoolManager()

for contents in fileSplit:
    uri = f'https://{url}/{contents}'
    r = Http.request('GET', uri)
    res = r.status

    if res == 200:
        print("[+] 200 OK: " + uri)
        dir.append("[+] 200 OK: " + uri + "\r\n")
        print()
    elif repr == 403:
        print("[-] 403 Forbidden: " + uri)
        print()
    else:
        print("[-] 404 Not Found: " + uri)
        print()

dirFile = open('Found Directories.txt', 'a')

for dirs in dir:
    dirFile.write(dirs)

dirFile.close()
print("**Scan Complete**")
