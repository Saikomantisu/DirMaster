import urllib3

print("""
▒█▀▀▄ ░▀░ █▀▀█ ▒█▀▄▀█ █▀▀█ █▀▀ ▀▀█▀▀ █▀▀ █▀▀█
▒█░▒█ ▀█▀ █▄▄▀ ▒█▒█▒█ █▄▄█ ▀▀█ ░░█░░ █▀▀ █▄▄▀
▒█▄▄▀ ▀▀▀ ▀░▀▀ ▒█░░▒█ ▀░░▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀░▀▀
           </Devel𝕠oped By HeX_006>
""")

url = input("Enter The Website You Want To Scan: ")
http_or_https = input("Enter 1 For HTTP or Enter 2 For HTTPS: ")
path = input("Enter The Wordlist Path: ")
print()

file = open(path, 'r')
fileRead = file.read()
fileSplit = fileRead.splitlines()
dir = []

Http = urllib3.PoolManager()


def http():
    try:
        for contents in fileSplit:
            uri = f'http://www.{url}/{contents}'
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
    except:
        quit()


def https():
    try:
        for contents in fileSplit:
            uri = f'https://www.{url}/{contents}'
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
    except:
        quit()


if http_or_https == "1":
    http()
elif http_or_https == "2":
    https()

dirFile = open(f'{url}.txt', 'a')

for dirs in dir:
    dirFile.write(dirs)

dirFile.close()
print("==== Scan Complete ====")
