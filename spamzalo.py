
import pyautogui
import time
import keyboard 
import pyperclip 
import random 
import requests
import os
import hashlib
import requests
from datetime import datetime
from colorama import Fore, init

def windowtitle(a):
    os.system(f"title {a}")
windowtitle("N̴̗̜̜̼̤̈́͂̑͋͋̈̌͆͋̓̉̑͝͝ģ̴̛̱̫͕͎̻̩͚̺͖̣̖̠̘̝̀̃͆̽̆̈́̈́̅̈͒̾̈́̇̐͒̈̚͝͝ͅơ̴͔̂͊̔̆͐͛̈́͂̌͗̂̇̊͋͠͠͠͝ͅc̸̢̫̓̉H̸̨̢͕̬̺͔͔̟̗̐̐̍̊̿͂̾̋̈́͂́̂̇̈̑͘̚͜͜͠ű̵̧̧̙̼͖̺͈̲̭͉͕̖̬̪̝͖̟̭͔̱̤̠̳̥̃̀̍͑͗͛̈̄̚͜ͅͅͅy̴̭̳̗͎̣̳̗͍̠̲̘̎̌͛̅́̊͝͠")

init(autoreset=True)

def hash_key(key: str) -> str:
    return hashlib.sha256(key.encode()).hexdigest()

def update_keys():
    try:
        response = requests.get("https://raw.githubusercontent.com/PremiumGreen/SISEMET/refs/heads/main/key.json")  # Thay đổi URL đến tệp JSON của bạn
        response.raise_for_status()
        keys_data = response.json()["keys"]

        for key, info in keys_data.items():
            if info["type"] == "trial":
                expiry = datetime.fromisoformat(info["expiry"])
                valid_keys[hash_key(key)] = {"type": "trial", "expiry": expiry, "used": info.get("used", False)}
            else:
                valid_keys[hash_key(key)] = {"type": "permanent", "used": False}
    except Exception as e:
       print(f"Lỗi khi cập nhật khóa: {e}")

valid_keys = {}
update_keys() 

def validate_key(user_key: str) -> bool:
    hashed_user_key = hash_key(user_key)
    key_info = valid_keys.get(hashed_user_key)

    if key_info:
        if key_info["type"] == "permanent":
            return True
        elif key_info["type"] == "trial":
            if datetime.now() < key_info["expiry"]:
                if not key_info["used"]: 
                    key_info["used"] = True 
                    return True
                else:
                    print(Fore.RED + "Khóa trải nghiệm đã được sử dụng.")
                    return False
            else:
                print(Fore.RED + "Khóa trải nghiệm đã hết hạn.")
                return False
    else:
        print(Fore.RED + "Khóa không hợp lệ.")
        return False


def main():
    os.system('cls')
    print(Fore.BLUE + "Chào Em Yêu")
    while True:
        os.system('cls')
        user_key = input(Fore.YELLOW + "Vui Lòng Nhập Key: ")
        
        if validate_key(user_key):
            print("Giỏi Quá, Key Đã Đúng.")
            break  
        else:
            print(Fore.GREEN + "Sai Mã Key, Vui Lòng Liên Hệ tele Nghdz0904 để lấy key mới")
            input(Fore.RED + "Key Sai, Vui Lòng Ấn Enter Để Nhập Lại Key ")

if __name__ == "__main__":
    main()




countdown_time = 10
print(f"Bạn có {countdown_time} giây để mở ứng dụng nhắn tin và chọn đoạn chat cần spam .")
for i in range(countdown_time, 0, -1):
    print(f"Thời gian còn lại: {i} giây", end='\r')
    time.sleep(1)

print("\nBắt đầu gửi tin nhắn!")

print("Nhấn 'q' để dừng gửi tin nhắn.")


messages = [
   "ơ ơ ơ rain 𝕋𝕒𝕙𝕟 𝕕𝕫 𝕜𝕙𝕠𝕟𝕘 𝕥𝕙𝕚𝕔𝕙 𝕦𝕒 ! rain rain     ๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊ܻܻܻܻܻܻܻܻܻܻ݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆ܻܻࣩࣩࣩࣩࣩࣩ࣯ࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩ֟֟֟֟֟֟֟֟֟֟֟֟֟֓֓֓֓֓֓֓֓֓֓֓֓֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֓֓֓֓֓֓֓֓֒֒֒֘֘֘֘֘֘֘֗֗֗֗֗֗֗֗֗֗֗֗֗֗֗ؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؕؕؕ",
   "sợ tao à con chó đần rain 𝕋𝕒𝕙𝕟 𝕕𝕫 𝕜𝕙𝕠𝕟𝕘 𝕥𝕙𝕚𝕔𝕙 𝕦𝕒 ! rain rain     ๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊ܻܻܻܻܻܻܻܻܻܻ݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆ܻܻࣩࣩࣩࣩࣩࣩ࣯ࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩ֟֟֟֟֟֟֟֟֟֟֟֟֟֓֓֓֓֓֓֓֓֓֓֓֓֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֓֓֓֓֓֓֓֓֒֒֒֘֘֘֘֘֘֘֗֗֗֗֗֗֗֗֗֗֗֗֗֗֗ؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؕؕؕ",
   "lại win à rain 𝕋𝕒𝕙𝕟 𝕕𝕫 𝕜𝕙𝕠𝕟𝕘 𝕥𝕙𝕚𝕔𝕙 𝕦𝕒 ! rain rain     ๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊ܻܻܻܻܻܻܻܻܻܻ݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆ܻܻࣩࣩࣩࣩࣩࣩ࣯ࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩ֟֟֟֟֟֟֟֟֟֟֟֟֟֓֓֓֓֓֓֓֓֓֓֓֓֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֓֓֓֓֓֓֓֓֒֒֒֘֘֘֘֘֘֘֗֗֗֗֗֗֗֗֗֗֗֗֗֗֗ؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؕؕؕ",
   "hăng tiếp đi rain 𝕋𝕒𝕙𝕟 𝕕𝕫 𝕜𝕙𝕠𝕟𝕘 𝕥𝕙𝕚𝕔𝕙 𝕦𝕒 ! rain rain     ๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊ܻܻܻܻܻܻܻܻܻܻ݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆ܻܻࣩࣩࣩࣩࣩࣩ࣯ࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩ֟֟֟֟֟֟֟֟֟֟֟֟֟֓֓֓֓֓֓֓֓֓֓֓֓֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֓֓֓֓֓֓֓֓֒֒֒֘֘֘֘֘֘֘֗֗֗֗֗֗֗֗֗֗֗֗֗֗֗ؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؕؕؕ",
   "m gà mà rain 𝕋𝕒𝕙𝕟 𝕕𝕫 𝕜𝕙𝕠𝕟𝕘 𝕥𝕙𝕚𝕔𝕙 𝕦𝕒 ! rain rain     ๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊ܻܻܻܻܻܻܻܻܻܻ݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆ܻܻࣩࣩࣩࣩࣩࣩ࣯ࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩ֟֟֟֟֟֟֟֟֟֟֟֟֟֓֓֓֓֓֓֓֓֓֓֓֓֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֓֓֓֓֓֓֓֓֒֒֒֘֘֘֘֘֘֘֗֗֗֗֗֗֗֗֗֗֗֗֗֗֗ؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؕؕؕ",
   "log acc thay phiên à rain 𝕋𝕒𝕙𝕟 𝕕𝕫 𝕜𝕙𝕠𝕟𝕘 𝕥𝕙𝕚𝕔𝕙 𝕦𝕒 ! rain rain     ๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊ܻܻܻܻܻܻܻܻܻܻ݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆ܻܻࣩࣩࣩࣩࣩࣩ࣯ࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩ֟֟֟֟֟֟֟֟֟֟֟֟֟֓֓֓֓֓֓֓֓֓֓֓֓֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֓֓֓֓֓֓֓֓֒֒֒֘֘֘֘֘֘֘֗֗֗֗֗֗֗֗֗֗֗֗֗֗֗ؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؕؕؕ",
   "chán v rain 𝕋𝕒𝕙𝕟 𝕕𝕫 𝕜𝕙𝕠𝕟𝕘 𝕥𝕙𝕚𝕔𝕙 𝕦𝕒 ! rain rain     ๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊ܻܻܻܻܻܻܻܻܻܻ݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆ܻܻࣩࣩࣩࣩࣩࣩ࣯ࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩ֟֟֟֟֟֟֟֟֟֟֟֟֟֓֓֓֓֓֓֓֓֓֓֓֓֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֓֓֓֓֓֓֓֓֒֒֒֘֘֘֘֘֘֘֗֗֗֗֗֗֗֗֗֗֗֗֗֗֗ؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؕؕؕ",
   "cay :))))) rain 𝕋𝕒𝕙𝕟 𝕕𝕫 𝕜𝕙𝕠𝕟𝕘 𝕥𝕙𝕚𝕔𝕙 𝕦𝕒 ! rain rain     ๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊ܻܻܻܻܻܻܻܻܻܻ݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆ܻܻࣩࣩࣩࣩࣩࣩ࣯ࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩ֟֟֟֟֟֟֟֟֟֟֟֟֟֓֓֓֓֓֓֓֓֓֓֓֓֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֓֓֓֓֓֓֓֓֒֒֒֘֘֘֘֘֘֘֗֗֗֗֗֗֗֗֗֗֗֗֗֗֗ؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؕؕؕ",
   "tao đang hành m mà rain 𝕋𝕒𝕙𝕟 𝕕𝕫 𝕜𝕙𝕠𝕟𝕘 𝕥𝕙𝕚𝕔𝕙 𝕦𝕒 ! rain rain     ๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊ܻܻܻܻܻܻܻܻܻܻ݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆ܻܻࣩࣩࣩࣩࣩࣩ࣯ࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩ֟֟֟֟֟֟֟֟֟֟֟֟֟֓֓֓֓֓֓֓֓֓֓֓֓֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֓֓֓֓֓֓֓֓֒֒֒֘֘֘֘֘֘֘֗֗֗֗֗֗֗֗֗֗֗֗֗֗֗ؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؕؕؕ",
   "mày nghĩ mày làm t cay đc à rain 𝕋𝕒𝕙𝕟 𝕕𝕫 𝕜𝕙𝕠𝕟𝕘 𝕥𝕙𝕚𝕔𝕙 𝕦𝕒 ! rain rain     ๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊๊ܻܻܻܻܻܻܻܻܻܻ݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆݆ܻܻࣩࣩࣩࣩࣩࣩ࣯ࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩ֟֟֟֟֟֟֟֟֟֟֟֟֟֓֓֓֓֓֓֓֓֓֓֓֓֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֒֓֓֓֓֓֓֓֓֒֒֒֘֘֘֘֘֘֘֗֗֗֗֗֗֗֗֗֗֗֗֗֗֗ؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؖؕؕؕ",
   "Ｈ̵̛̳͎̲͙̣͈͚Ｅ̸̰͔͍̦̟̝̹Ｌ̶̠̟̗͇̗͇̜Ｐ̶̯̰̣͕ ̷͙̜Ｍ̶̻Ｅ̷͓̠͈̝",
   "đ̵̢̡̢̟̼̮̻̖̜̩̦̮̭͙̞͎̩̮͎̭̞͖͙̭͔́̽̈͋̎̍̐̓̀̊̆̍͑͑̔́̈̒̒̂̈̈́̄̈̆̇̍̈͂̊̐͊͒̈̋͒̈́́̈̚͘͝͠͝ị̸̡̡̧̨̛̭̠͈̦̩͔̻̲̱͔̗͉̝̠̦̳̗̓̀̽́͆͑̓́̅̄́̍̒̉̃͆͛̒̈́̓̈́̈́̉̐̄̽͒͗̽̇́̉͆̈́̚̚̕͜͠ţ̴̨̡̧̧̡̢̛̛̯̦̤̼̥͍̪̻̬͔͍͕̠̺͙̙̗̟̰̦͔̼̜͍͋̍̇̂̽͒͐̉́̒̄̓̌͛̅̏̅̉̈́̐͆͆̓̅̐̽̌́͋͘̚͝ͅ ̵̨̨͎̗̬͈͈̳̺̗̩̲̲̥̞̞̃̃̃̉́̓͛͊̑̌̍̅̀̉͋̃̐͋̏̾̀̈̋̕͘͠c̶̫̳̩̯̲̄̈́̃̄̉̔̚ͅo̴̧̮̗̹̥̱͍͓̥͐̄̿̈́͛͆̃̓́́̎͑̆n̶̢͕͎̣̘̖̠͖͇̞̠͇̙͌̂͑̔̄̄̒͋̃͗͋̂̔͐͛̊͘͘͘̕͜͠ ̵̡̨̡͕̟̮͍͖͈̺͈̜̜̪͎͇̦̪̭̦̼̲͍̫͙̲̮͓͈̠̪̭̱͙͍̈͌͐͗̀͂͛̋̐̇̉̿̾̕̕͜͝ṁ̵̧̡̧̧͓̦̦̩͕̭̞̱͇̟̞̠̳̭̣͕̪̦̲͂͂͋̿̎̄͂̓̋̀̔͊̂̊́̓͝͝ͅẹ̶̝͕̼̑̂̄͊͐̋̍̇͑̀͋͑͆́͒̄̓́͝͠ ̸͉̖̗̥̠̝͖̭̤̬̝̯̯͋̓́̈́͗́͂̇̄͐͂̍̌̓͛͛̏͠ͅͅͅņ̵̛̣͇̬̹̼̲̅͐͌͗́̽͛͂̿̈́̅͐͂̈̔̐̂̓̈̎͗̐̉̏̌͝͠͝ḩ̴̢̧̨̤̘͔̩͇͈̭̝͔͍͈̟͈͍͇̦̪̩̫̗̬̯̻͕̯̮͓͙͈̻̺̪̫̆̽̿̐̊͝ͅà̶̡̹̻̤̳̪̣͆ ̷̢̡̢̧̡̧̪̙̜̺͇̥̻͇̙̣͎͚̞͇͉͚̫̣̠̖̮͕͉͔̹̈͌͗͋̔̆̃̈́͛̃̅̈́̅̈́̓͝͝ͅm̴̡̡̡̡̛̛̛͓̦͚͉̲̩͕̪̠̘̱̯͖̠̪̯̤͓̙̻̫̮͚̠̓̏͊͑̆̾̔̄̈́͒́̈́̉͆̄̓̔̅̌̌̓̓̎̍́̌̄̔̔̆͒́̂̑̆͗̃̚͘͜͠ͅà̸̢̢̨̡͓̳̮̼̦̱̘̝̤̞̘̼̘̮̤͔͕̰̙̜̥̼̯̮̳̰͔̞̬̟̗̅̓̐̇̀̍̇̾̃̑̔̈͂͌͋͑̌̾̏̎̆̐͘͘̕͘͝͠͠ͅͅẙ̵̛̩̪̼̰͇͚̹̻̥̖̥̣͍͎͔͇̝̘̥̠͈̤͇̻͔̺̫̳̺̠̠͍̮̫̹̞̊͗͆̇̅̓̾͛̑̽̎͆̾̽͛͒̓͛͆́̏̿̆͆͜͝͝͝ͅͅ",
   "ḏ̷̢̡͙͚͖̭̪͖̐̾̒̒͑͆́͋̋̎͘͜͜͝͝ͅç̷̢̺̭̯̭̺̱̱͎̜̹̻̱͎͍̳̗͉͈͉̱̖̼̩̖͚̥̙̱̱̣̘̬̖̪̘̯͉̗̬̠̻̯̙͕̈́͑̅͜ͅm̸̨̡̠̙͔͈͙̪̙̜̖̻̝̥͇͍̙͙͎̭̙̙̜̼͓̫̦̙͍͓͚̮̫̈́̋̾̋̎̍͒̔̈͜͜ͅ ̶̡̛̳̠͕̰̞̫̣̰̹͔̮̠̬̜͙̖̮̳͔͕̜̻̻̮̼̩͙̩̭͍̲̳̼̫̙̪̰̖̼͚̓̆͌̊̓̇͂͛̕͜͜͝ͅͅͅn̵̰͕̲̳̥̺͔̥̖͓͒͐̓̎̈̂̌̂̊͛̈́͠͠ͅg̵̢̧̡̡͍̹̩̗̝̼͇̙̥̭̜̞̮͉̈́̆͜ͅͅư̵̧̢͈̭̫̰̻͈͎͙̻͈͎̤̮̳̼̻̱͓̻̗͕͐͛͛́͘͜ ̵̡̛̪͖̖͓̂̃͋̈́͒̏̈́̄̓̂̑͂͂̄͒̑̃̊́̀̚͝͝͝c̸̢̧̢̡̪̰͉͉̘̘̬̟͉̖̤͉̲͇̬̣̫͈̯͉̦̻͇̖̦̦̰̬̖͛͑̈́̔́͗̈͋̒̀͐̑͒̽̒̇͊̂͂̈́̚̕͝h̸̡̢̡̧̡͓̠͚̝̯̻͕̜̣̪̪͔̯̺̼̺̮̥̥̖̠̺̩̰͉̰̫̙̞͕̅̈́̿͗̊͂͌̄͆̉͂̂̾͋͆̈̑͗͜͝͠ͅư̵̭̙̋̃͋̈́̍͗͛̀̑̃̄̅͊̀̂̂̋͑̽̍͛̒̃͋͘̕͝͝ą̵̡̡̱̮̗͚̭̫͚̙̥͚̙̟͚̠̠͓͎̥̳͈͍͚̲͓̗̪͓̖͇̪͙̥̝̻̙̺̙̜̏̆̃́͑̐̎̄̓̊̓̃͋͌͌̈́͂͂́̽͐͐͆̽̋̄̓̈́̓̓̿́̐́̃͑̎̉̎̈́̿̓̋͘͘̚͜͝͝ͅ ̷̖̫͉͊̾͆͐̄͆̓̔̽͛̓̆̉̓̓̀̈̀̎̃͂͘̚͝͝͝͝ç̵̡̢̛͍̻̩͈͓͉̳̱̬͚̯̰͙͉̬̦̟̗̣͖̼̟̮̰̤͔̣̲̺̯͇̳̞̫̬̰͙̀̈̎̋̕͜͜͠ͅͅo̷̡̼̘̪̲̦̗̳̣͍̍͒n̴̡̨̨̛̟̦̼̲̯̱̼̤̳̣̬̝̩͓͓̼̮̞͕͈͚̈́͋͊͒͗̌̉͊͗̿̋͊̒̈́́͗̈́̑̽̾̈͐̆͊̽̽̄̃͌̿͜͠ ̴̧̛̬̣͎̝͔̝̦̭͈͇̘̤̹̞͚͙́̂͂̀̐̇̍̃̇̂̅͆̔͐̈͋̐͑͗͋̐̔̂̑͆́͋́͝ͅͅc̶̛̛̯̯͓͙̟͇̖͔̞̫̼̺͈͚̗͎̻͙̤͙͉͔̠̹̭̗̤̀̀̅̂͒͒̿͆̊́̄͛̀̈́̿̅̉̔͂̐̄͋̂̔̑̊̕̚̕ḧ̵̨̡͕̲̩̭̭͎̗̦̖̘̳̭͕͇̣̭̭̻͍̭̟̮̗̼̼̥̭̩͔́͂̌͋̈́̆̊̄̾̄͑̊̊͊̒̈́́̆͐̈́̏̏̊͒͘͜͠͠ͅó̵̢̡̧̼͔̬̗̗͉̣̺̼͓̫͙̻̗͑̀͂͜͠ͅ",
   "d̷̨̨̖̝̘̝͎̗͉̞̗̞̩̦̱̉̿̐͛͋̈́̂͆͋̂̒͗͗͌̔̆̄̀͋̈́͗͊͊̒̀̍͌̇̎̍͆̃̐̉̾́̑̋͊͂̾͘͘̕͜͝͠͝͝͠c̵̬͕͇̩̱̦̲͖͍̝̝͔̏͌̒̄̌͜ͅm̶̠̺̈́̒̀͗̍̈̿̈́͂͐̆͝͝ ̵̢̢̡̧̹͚͔̳͇̤̫̬̭̹͔̗̱͚͙͓̲̱̩̟̣̫͖̟̻̜͚̖̪̹͎̯̥̦͔̗̪̤̳̝̪̄̌͋́̂̐͊̅́̋̏̿͗̆͊̀̒̀́̚̕͜͝n̸̢̧̢̛̰̞͇̖̙͔͔̳̭̜̜͈̘̠͓͇͇̝͖̱̠̫̝̥̋͒̌̈̐̅̏̓̐̿̓̆͐̿́͛̅̈́̾̽͒̌͛̾͂̀̕͜͜͜͝͠ͅͅg̷͔̪͈̱̗͔̲̙̬̜͈̮̰̝̦̺̀̓́̏̈́̍̃̎̕͜͝ư̷̫̪͔̻̬̳̟̭͖̝̠̪̗̠̥͓̯͈̣̞͎̭͓̳͎̹̲̹̼̠̰̙͍̥͈̺̳̩̌͌̊̈́́̐̀́́̒̎̄̀̔̍̆̆̐̀̉̂͗̂͑̿̏͒͗̊͋̋̔́̇̑̽̑̔̉̌͜͝͠͝͠͝ ̷̨̢̨̨̛̛̛̛͓͎͖͙̝̰͕̙̻̤͖͙͓̞̦̬͍̠̺̘͇̩̻̻̻̭̥̞̪̤̦̱̥̝̖̝̟̥̼̯͔̋̾̅̽͋̀̃̀́̌̀͂̃́̔͗̎͆͋̄͛̊͆͗̋͋́̿̅͋͘͝͠͝͠č̸̢̧̨̛̼̣̖͎̖͈̰͔̝̱̣̻̦̳̻̟̗͔̩͖͎̄̾͗̓̑͋́́̐̔́̔̓̒̑̀͛̅͗̋͗̀̂̓͋̉̆̐̂̈̋̓͛͑͐͘̕͝͝͝ͅh̴̨̧̧̩̠͎͙̺̝̩̲̭͓̻̻̤̣͖͍͇͎̟̮̻̘͎̰͗͗͋̌͗͌̃̏͜͜ͅͅͅư̸̢̡̨͙͔͔̦͈̜̖̜̯͇̣̗͚̦̭͎̫̮̟̙͎̱̗̣̟͙̹̝̲̩̘͔̞̤͇͖̺̭͛̅̇̈́̾͋͗͐̇̈́͗͆̔̾̔̅̄̑̌̆͂̉̎͗̓̓̎̂̄͘͘͘͜͝͠͠å̷̛͚̠̗̟̖͖̠͈̰͍̯͗̇̉̌́̓̓͑̓͋͐͒͑͆̓͂́̓͗̾͂̈̉̇̓́̊̀̇͌́́̒̾̀̀̽̅̄͂͘͜͝͠ ̸̡̢̪͉̖͕̗̖͓̹͙̖̞̰͉̘̯̙͇̥͍̤̦̭̯͓̫̬̜͖̿̒͌̐̈́̿̅̈́͂̍͂̓̽̿̇̈́͗̓̌͐͊͗̍̽̈́̌̊͜͜͝͝ͅc̸̡̦͗̈́̃͑̃̀̅̄́̈̄͗̂̄͐̉̇̅̈́̅̉̐͛̆̽̔̈́̉̒̊̃̄̈́͋̏̈́͆̂͆̚͘͘̕͝͝o̷̢̢̡̨̬͔̰̬̼̟͎̭͎͍̥͓̫͇̠̖͈̪͙͈̮̯̭͒̾͊͆̄́̒͐̄͑̍̅̐̀͊̏̋̋̀͌́͂̈́̅́̆̌̚͘̚͝n̵̢̢̛͓̬̠͎̫̣͚̟̮͎̳͛͗̿̄́͊͑͗̄͌̆͛̔̄̒́͠ ̶̨̡̧̥͓̣̩͉̰̙͕̥̝͉̈͂̆̓̒͐̈́̀͐̈́̈́̾̎͐̆̀̓̓̇̒͋̽̃̏͑̽̌͜͝͝͝ͅͅ",
   "h̶̢͖̼̦̲̝͚̜͓̳̫̬͉̣̙͇̲͖̠̥̭̭̼͇̪͉̜̫̳̻̏͒̄̃̊̋̑̉̿̽̌͆͛̒͘͠ą̵̨̢̨̯͍̜͙̯͙̱̬͎̤͕̲̯̮͚͎̹̞̮̗̺͙̖̭̼̙̤̥̖͙͔̪̱͉̺͈̘͍͂̈̔̎̂̊̾̽̀̑̂͊̔͝ͅͅͅh̴̨̧̡̨̛̛̜͚̯͚̪̯̘͔̞̘̬͚̺͚͇͖͓̲̃͆͊́̂͒̂̍̈́̍̽̄̀̄̀̈́̅̀̈̈́̋̆̑̆̆̃͌̃̾͊͗̐̂̉̌͒͊̋͌̾͐̃͘̚̕á̶̡̛̭̘͚͙̲̝̲̃̓̄͗̿͂̉́̑͐̂̿̇̉̐̓̌̒͒͐̏̎̚̕̕͝ ̷̛͓̯̠̝͎̲͎͎͙̜͈̘͍̗̣̖̹̜̮̺̥̘̩̞̝̞̟̞̄̑́͐̐́͒̾̋̓͌͑̑͋̊̂̾̎̊̄̊̈́̆̐͆̅̔͋̐͊̍́͐̓̉̐̏̚̚̚͘̚̕̚͠n̸̡̧̧̧̧̧̠̗̳̩̱͙̻͉̫̪̗̘̗͚̰̗͍̗̝̪̘̗̗̹̘͌͛͗̎̅̀̑͑̾͂̀͆̃̽̐͋͐̎́́̈́́̇́̉̈́͌̑̽͆̏̇̾̀̀̀̈́́̾̕̚͘̚̚̕͜͜ͅͅģ̴̡̨̬̲͕̝͔̻̦͈͕̤͓̖͈͑̈́̐̍̀̓̆ű̶͔̗̜͈̥̗̤͚̫̀̄̂͊̔͌̈́̓͑̚̚ ̸̢̫̝̠̹̯͕͓̳̟̖̬͉͚͖͚͔͈̩͕͚̹̹̞̎͐͋̽̂̂̓̄̇̊͑͗̑̿̓͐̒̆̋̃̋͗̍̔̕͜͝l̵̡̧̛̘͓͎̟̖̝̹̜̄̒̃̋̿̋̑̄̓̑́͗͑̃̀̌̌̈́̉͌̎͂͆̔̂͛̈́̀̃͒̋̕̚͜͝o̸̢̡̧̡̢̜̱̫̯̭̤̼̟͉̤̝̭̜̮̼̹̥̘̩̖͓̤̤̦͕͉̞͚̯̞̜͎͔̤̜̦̰͇̲̝̦͖͓͊́̾̆̅̀͜ͅn̸̛̛͇͖̪͕͙̤̺̳͓̺̗̖̭̱̤̣̞̘̱̗̥̼̖͍̱̈́̋͐̂͊̽͊͋̄͌̔̓̄͑̀́̽̓̈̒́̊̊̂͌́͂́̀̋͊̋̿̽̽̄̀͗̕͜͝͝͝͝",
   "c̸̨̢̞̣͈̹̺͓̹͙͚̖͍̙̻͉̦̓́̇̉̈́̈͗̉̐̋͊̿̾̏̇̆̈́̌͆̌͗͒͊̚̚̚͝h̴͕̘̘͎̟͖̞̬̼͕̱͌͌̐͜ͅḙ̸̛̖̳͎͔͍̈́̓̿̊͋̊̅͆̀̑̿̀́͛̐͆̈́̌̍̇͐͠͝t̶̢̢̡̢̬̯͖͚̫̠̗̮̟̲͚̯̹̣͎͖̱̜̪̙͎̦̬̺̱̮͇̟̫̞̻͚̘̘̼̄̀͆͋̓̂̃͌͒̊̍́̓̂̈́̐͗́̔̈́̄̐̒̎͘̚͘͜͜͝ͅ ̵̢̧̢͕̮̬̜̰̠̝̯͉͓̜̭̜̯͓͇̲͈͉̪͍̮̪̲̰͎̞̱̩̦̩͉̞̹͈͇̤̺̤͍̫̥̊̐̓̈́̉͋͗̐̈́͝ͅć̶̢̢̨̨̧̛̛͈͓̲̼̥̖̩̤̜͇̞͓͙̦͓͇̻͕̞̱̱̣̳̄̀͑͊̽̾́̈́͆͊̈́̽̀̽̈́̆͐̎͂́͆͗̅̏̎͗̌͛̚̚͜ơ̵̡̡͕͓̪͎̩͍̺̬͇̩͚̫̝̝͔̹̥͈̳̣̭̘̯̳̩͙̤̲̲̲̗̖̆̐͆̄̅̃̌͋̅̇̈́͂̀́̎̈̅͛̓͌̇̀̀͊̀̐̿̉͜͠ͅͅn̵̛͕͙̪͉̝̬̳͛͛̈́̈̑͋͛̇̉͌̾̂̋̄̀̂͗̀̐͌̑͛̒̌́̆̾̀̇̚̕͘͝͝͠ ̵̢̨̧̧̪̜̖͓̺̩̳̼͓͔͖̱͎̫̻̻͈̩̞͖̲͎̪͔̜̩͉̳̩̰̼̰̫̝̭͇̜̥̻̪̣͔̐̅̀͋͒̎͂̍̽̍̓͊́͆͆́̇͗͂̉̃̕͘͜͝͠͠͝m̵̢͍͓̰̲̳̟̫̮̳͔̗̘͉̪̼̝̾͐̆͋̏̓͐͐̚̕̕͠͝é̵̢̧̨̢̛̛̙̟̭̠̰̙̪͖͎͎͚̥̬̲͕̳̖̙̯̯̮̱̥̼̻̜̣̓̍́̄̐̈̈́̈́̇͒̃͂́́̇̿͛̈́́̇̾̈͋̋͊̅͘̚͘͠͝ ̸͓̪͌͆̂̾̈́̿͐̆͆̐̆͒͋͑̑̾͐̔̔̈́́̄̊̈́̅̈́̾̏̿͗̔́̿̔̓̈́̃͂͂̔̂͘͘̕̚͠͝͠͠ņ̶̨̧̨̡̟̫̗̗̻̥̼̯̺̘̩̝̝̫̥̗̩͖͓̠̦̥̘̫͚̞̖̦̗̞̳̏͋͐͂͊̊͆̎̓̏͐͘͠ḩ̵̢̨̧̨̯͕̦͎͎̦̣̰͚̯͖̞̼̰̰̖̯͕͖̮̱͈̳̥̺͕̙͎͔̯̰̠͕͕̉̇̀͆̀̈̾͆̆̒̃͑̑͐͒͐͗̅̓̈̿͊́͛͆̎̔͐̒̏̊̄̀̃̆̌̌̉͘̚͝͝ͅą̷̱͉̲̮̄̾̌̃̈́̊͋̒͂̐̋̂̓͘̚̚͝ ̸̢̨̧̲̗̬̭͉̤̤̳͕̻̗͚̼̹̤͖̮̘̮̼̖͚̼̰̜̹̮̩͈͔̮̭̘̦̙͔̞̮͙̓̎̿̊̑͋͑̂̍͜ͅṃ̸͈̳͚̘̘̝̬̼̟̣̭̩̭̙̹̅̀̓̑̆̃̾̆̔̂͑͒͐͐͌̿́̽̐̍̽́̈́͂̉͌̑̍̿̎͒̕͝͝͠͝a̴̢̨̛̛̻̫̯̠̬̬͎̣̮̞̞͎̪̯͖͙͉̱̳̞̞̗͉̼͎̤̻͙̳̲̋̃̀͐̄̎͛̊͋͆̎̓̓̌̈̈̀̈́̅̎̾͆̏̈́̈́̅̓̽͌̿͑̆̎͊̌̾͘͜͠ẙ̶̨̙̺̲̩̟̪̳̭̲̗̦̭̉̉̉̀̐̃̏̄̃͛̋̇̄̀́̅̎͑̈́̀͒̑́̎̾͘ ̸̛̛̗̯̊̿̅͑̈́̃͒̋̉̄̽̾̏̍̌̀̑́̓̿̎̂͐͠͝͝͠͝͠d̸̡̡̢̡̡̢̨̡̛̛̰̲̪̙̫̘̙̗̦̞̞̠͇̞̹̼͇̹̝̯̣̟͍͓͕̲̟̟̯̜͎̤̳͇͇̞̜̜̞͇̫̏̒̾̍̅̐͛̂̔͆͆͐̍͆͗́̒͊̀̈́̓͆́͂̾̅̈́̈͋̑̎͂̉̓͆̄̈̕͘̚̕͝͝͝͠ͅi̵̧̛̪̥̱͕̲͈͙̖̠̞͉̱̦̫̪̩̝̥̟͎͔͈̋̆͐̂͛͑̐̾͛͆͗̄̇͂̈́̒̄̓̎̈́͒̈́̌́͂̽̅̓̓͒́̋̌̀͆̒̈́͊͋̀̓́̚̚̕͝͝͝",
   "v̷̛̥͔͚͕̠̻̫̩u̷͈̖̞̯͎̳̼̗̞͉̣̠̼͗̓̌͊̃̈̎̀̇̎͂̊͛̎̑́̏̔̓͆̎̓͒͗͊̈́̀͋̌̀̚͘͠ͅi̶̡̡̡̛̛̛̦̬̹͙͎̬̝̲͙̜̪͈͔̙͍̲̝̖̖͎̭͕̬̪̰͎̝̤͎̻̜̟͕̫̬̮̖̪͚̪̞̗̝̟̥̔̑̑̉͛̆̀́̽̐͑͂̍͑̌̍̍͂͂̍̏͂̈́̍͌̉̓͌́̽̌̊̓̕̕̕͜ ̷̨̨̧̨̢̧͔̩̻̼͓̤̥̦̙̻̩̤̲̠̙̳̬̻͇̝̹̖̳̹̳͓̭͎̞͐͗̀̇̅̐̓͆̀̈́͐̾͛͂̀́̎̔͘͜͠͝v̸̨̧̨̨̢̡̡̨̢̫͎̟̯͍͔͔͉̣̟͍̞͇̘̪̱͉͍̼̗̱̫̟͕̯̹̘̻͕̗͖͉̅̓̒͋̿̀̈̅̇͛̿̾͋̾́̂̐̅͛̀̌̀̍̀͆̾͐͐́̿̅̋̾̑̂͂͊̉̃͊͛̈́͛͆̕̚͜͜͠͠͝͝ͅą̵̨̢̢̡̧̛̟̭̭̞̦̦͖͉̦͔͍͓͎͚̺͉̩͖͉̰͔͍̣͕̱̪̬͔̪̬̯̬̤̙̮̟̜̅͂́̀́̂́̐͗͘̚͘͜͠͠ͅì̶̡͉̻̺̾͆̌̒͗̽͆̇͒̐̈̉͗̽͗͋̿̀̄̓͆̂̔̿̂̇̈́̃̈̈͋͒̈́̀̇̇̐̏͛̚̚̕͝ ̸̨̢̨̨̧̢͙̹̠̠̙͖̠̼̹̭̯͕͉͈̰̟͙̤̯̫͍͕͇̟̪̤̲̲͕̮͍̣̮̦̬̗̩͇̮̒̄͜͜ͅͅḉ̶̧̧̢̛̮̘̙̠̼͖͎̜͖͕̘̖̖̖̮̯͎̱̟͇̺̘̲̹̟̖͎͎̠͚̱͎̥̗̤̯̩͔̟̰͈̜͋̈́̍̓͑̾͌̋̽̿̈́̍̾̃̎̎̃̃́̽̽̀͗͐͊̔̚̚̕̚͠ͅa̵̡̢̨͖̺͙͈̺̩̗̺̗͎̹̘̦͚͙̻̜̰̜͖̤͍̍͛̏͜ͅ ̴̻̟̒̊͗̌̀̅͊͐̓͋͛͝͠l̴̨̛̹͙͙̠̝̘̻̩̖̱̪̬̜̹̗̥͍͕̯͈̾̊̋̆̀̋̓̆͗̽̐̅̾̊͑̍̂̿͊̂͊̇̔͑̋̃́͐̽̅͋̉̊͒̔̀̆̈̚̚͜͝͝ò̸̧̧̨̢̡̧̨͇̲̳̜̼̣̞͎͇̹̲̣͚͙̳̖̙͎̱̺͍̳̤̫̜̦̯̘̈́̒͗̔̄̈͆̂̇̿̓͆̂͗͊͊̓̾̉̓̃͘͜͜͠n̷̢̧̘͔̼͇͈̰͎̖͍̮̳̏̑͊̇͗̌̈́̇̀̄̔̈́̕̕͝",
   "m̴̡̧̨̢̨̛̖̠̬̟̠̻̤͉͙͇̼̘͕͚̯̖̗͙̤̹͙͉̱̜̤̩͍͙̺͔̪̺̰̬͚̳͆̓͋̏̑͑̃̿̃͑̿̃͗́̍̎̓̊͐͐̒̿̀̊̋̈̈̌́̿̿̅̎̈̀̀̄̇͘̚͜͠͠͝͠ͅͅͅa̵͍̯̞͍͙̼̠̞̱̗͚̜̟͔̬͐͛̽͌̽́̇̈́̃̈͋͊͑́̐̃͛͐͆̅̏̊͑̾̅̋̂͐̈̄͊̎̊͌̕͘͘͘͘͜͝͝ȳ̶̨̢̧̡̢̢̛̟̹̳͔̞̝̙̟̤̙̩̖͍͙͓͇͙͔͖̱͎͚̘͉̣̮͍̮͎͚̤̞̇̄̔̍̌̐́̊͒͌̅͗̅͊̔̆̊̉͋̈́̉͆͑̇̓͒̊͆͂͛̇͐̿̾̄̐͂̈́́͒́̕̚͝͠͠͠ͅͅ ̴̢̛̺͚̺͍̙̘̮͈̱̖̟̬̙͕͕̦̗̠̬̭͉͙̳̫̙̞̘͖͔̰̞͚͖̩̟͉̥̬̟͙̳͔̮͈͚͇̒͛͊̏̀͑̈́̽͋̓͋̅́̈́̀̂̇̅͛̔̀̀̿̉̌͋͊̌͋͆̉̅́̚̕̚̕̕͜͝͝͝ͅn̶̡̡̡̨̨̛̼̭̟̠̭̬̬͚͓̗͇͙͔͙̜͎̼͎̱̳͎̪͚̲̝͖̪͈̱̫̲̔͌̄̉͑͌̈́͆̅̽͌̃́͒̎̓̆̉͐̈̅̈́̀͒͛̃̾͛͛͌̇̚͝ͅg̴̡̢̢̡̧̛̫̙͚͎̗̬̝̟̯͓̰̪͎̺͎̲̪͉̪̥̗͔̪͙͔̜̳̜̻̲̭̩͕̳̙̻̞̼̎͆̂̿̋̔͛̉̍̿̀͌̆̐́͂͒̽͌̿̂̿͑͋̾̅̋̀̐͌̈́̉́̍͂͂̈́̓̎͂̕̕͘͝͝͝ͅư̶̡̨̤̯͕̳̹̫̪͈̝̳͚̖̤͉̩͉̰̯̰̞̹̗̘̦̫͉̝̗̘̬̣͔̱͈̞̦͕͒̎́͆́̉̔̌́̉̔͛́͛́̀̆͂͗̈́̑̊̽̆̈́̀̕̚̚͜͝͝ͅ ̸̡̢̨̨̡̛̲͍͉̲̠̜͓̮͔̗͙͖͈͇͇͙̳͇̬̖̰͉̥̹͇̯̙̰̭̤̎̽͛͆͑̊̑̃̋̔̂̑̎͂̋͂̄͊̈́̇̆͗̑̇̆̀̔͛̂̿̂͗̊̈́̚̕̚͜͝͠͠ͅṛ̵̢̱̩̲̞͓̬̥̳͍͍̞̱̳̙͇̦̟͗̄͊͆̈̆͆͑̉͛̾͊͗͊́̀̋̈́͑̊̑͗̈́́̇̆̈̆̄͒̇̓̈́́͑̑͋̾͂͘͜͜͜͝͠͠͝͝ͅo̶̡̨̡̡̢͈͈̻̣̫̭̗̞͙̩̠̫̖̹̜̲͍̱̗̪̲͚̫̥͇̘̥͉̬͈̻̯͎͇̹͓̩͚͚̗̰̙̥̅̾͒̓̀̋͂͗͗͋̏̃̐́̈́͌͊̿̈́́̋̀̇͋̽͋͛̈̈́̏͘͘̚͘̕̕͜ͅȋ̶̧̧͓̩͍̲͉̭͖̟͚̤̘̯̫͉̫̭̩͎̳͖͇͙̗͔̘̤̳̥̝̝͇̬͉̬͚͕͓̹̻̫̘͍̜̜̆̇̀̀́̉͛͐̋̉͗̓͘͜͜͝͝͝ͅͅ ̵̧̧̢̢̨͎̭͚͉̱͚̲͍̰͓̹͈͇̟̟̦̞̯̲͍̠̺̳̤̹̘̙̯̜̺͕̼̪̓̀͛̓͗̀̈́̎͐̍͘̚͜͜͠͝ͅͅc̶̢̡̪̫̜̥̩̩͆͂̔̂̈́͛̉́̌̓̒̓͑̓͛̆̏̉̓̂̿̉͐́̈̇̊͛͠͠͝͝ö̶̧̘̪̪̩͉̳̹̺̖̺͕̠̲͙̣̪̝̞͒̇͌n̵̨̨̖͈͈͕͈̳͉̗̻͎̰̹̪̹͈̜̭͙̤̞̟̻̙͑̄̋ͅ",
   "b̴̘̼͙̦̘̠̹̙͙̳̝̣̻̮͋͊̎̔́͗͂̔̇̈́͋̊̎̈́̈̌͆͒̒̌͊̄̾̆͗̾̍̕̚͘̚͝͠͠j̷̛͔̭̲̗̱̖̬̥͉̯͙̼̠͇̺̱̠̼͖̰̼͇̟̗͎͈̬̣̺͈̼̬̯͓̳͇̝̪̪̥̓̏̀̃͊̏̔̈͊̍̒̊̇̒̑̓̋̇͌͐́̀͋̔̐̍̕̕̕͘͘͝͝͝ͅͅͅͅv̷̡̧̧̠̰̠̻͕̩̞̲̟͖͈̱̞͚̼̦̩͍͔͈̝̘̻̲͓͙͍͍̽̈̓̽̏̽̇͒̀̏̅̍̈́́͘͘͘̚͜ḓ̸̢̢̧̨̢̡̛̛̣̘͎͎͎͖̬͈̤͈͕̗̭̩̪̱̺̟̣̹͔̟̞͖͚͖́̿͋̓̾̈́̆̀̈́̔͐͗̓͊̋̒̂̎͗̃͆̄̈́͌͋͐̓͗͑͛͛̆̄̕͘ͅa̴̧̧̡̡̙̭̣̳̲̟̞͉̼̦̰̞̋͑̑̇́͑̈́͊̔̓͝͝ͅl̴̡̟͈̰̫̳̠̐̉̂͆̋̉̒͐̂̑̉́̊̈́͑̒̅̃̅̊̏̈́͋̈́̓̏̔̆́̈̈́̈́̅̋̀̕͝͠͝͝ņ̸̢̧̧̢̢̛̩̟̺̦̮̩̬͓̼̦͍̲͚̜̜̞̪̞̫̙̳̥̼̗̝̻̟̭̼͇̬̋̔̉̽̌͌͗̏̌̎͌̊̈́̃̏̈́̊́̏̄́̔́̊̒̔̊̈́́̋̀̀̾̔̒̉͜͜͠͝ͅv̶̡̹̰͙͉̺͎̙̈́̾̓̓͌̽͋̌̅̊̓̈́͆̉̽̽̎̎͒͆̆̋͗̔̐̀͂̄͆̃̂̀̊̊͑̊̃͘̚͘͘͘͠͠b̶̡̨̥̞̳͕͉͉̳̠̥̮͉͕̤̖͎̗̗͓͚̺̫̰̭̟̲̠̥̘̰͓͕̤͍̦̗̘̮̯̳̺́̔̈̂͒̎̈̃̋͗̒̅̕͜͝ͅͅḇ̷̺͇̱͙͒̈́̀̍͆̃͌̀̀͑̊̂͗͒̾̎̋͌̔͋̈́͊͠f̷̡̣̠͉̱̬͚̪̠͖̰͈̜̦͓̳̦͉̳̬̘̪̞̱̣̠̟̯̫̹͈̜̻̫̫͔̠̦̥̟̼̦̱͉̲̒̀̑̍͆͊́̄̈́̄̑̀͆͐͐́̀́͑͂̀̔͜͜s̷̡̡͔͍̹̯̺͉̳̘̭̩͍̩̘̈͊̔͗̽̂̌̔͐̋̓̓̓͐̋̃̾̎́̐͆̈́̓̌̉͊̂͠͠i̷̡̢̡̡̝͍̭̣̣̖̯̜̼͕̹̙̙͙͉̬͓͗͂́̒̆̿̒̔̒̅̓̇́͋̽͌̃͐̇̊́̎̄͌̒̉̂̈̅̅͒̽͘̚̚͜͝͝͝͝͝͝ͅͅo̶̧̰̦͇̜̰͉̎̎̅̌͌̊̂́̔̈̃͑̀̚͠͝͝j̵̨̢̛͓̘̩̟̪͈̗͙̲͎̟̱͚̠̹̤̖̙͈̗̣̥̜͚͇̲̜͎̙̭͚̲̩͈̤̜̜͖̠̝̙͉͓̟͖͚̯̔̃̍͐͒͛͛͌̿̆͂̀̍̓̈́̈́͆̃̀̑̑̾́͐͒͌̚̚͜͝h̶̡̡̧̧̧̟̖̯̰̝͈̦̲͉̺̥̙͔͖̝͈̪̳͓̪̲̦̣̹̟͇͇̹͙̰̬̗͓͕̥̻̞̞͔̆̏͛͑̎̀̆͜͜͝ͅơ̴̧̢͕̙̩̯̻̻̗̤̗̬̝̩̗̰̭͙̺͎̻͈͓̗̥̱̪͎͉̈́͗͒̏̾͑͛̾̐̽͊͂̏̽̚̕ͅb̷̡̧̢̨̨̨̨̧̜͓̳̲̱͔͚̥͉̰͚͔̘͎̪̭͉̪͙͉̖̘͔̝̩̮͈͇̯̫̹͇̤̹̹̻̠̻͍̞̖̈̇́̔̎͋̈́͌̃̆͛̕͜͝͠d̵̡̢̧̨̛̟̺̣͓͓͙̰̰̞̯̗͚̹̖̥͍̟̠̥̯̘̮̯̠̰̠̞̮̝̺̼͖̖̮̗̩̤̦̰̯̬͈͙͙͉̈̔̓̉̾̂͗̓̈́́͋̐̓̀̾̀̈͐̀͐̏̀̌̄̀͑͗̾͌͌̇͛͆̀̑̀̾͆̏̅̔̐͑͊̊͘̚͜͝͠ą̴̧̛̛̞͔̣̯͕̮̻̪̤̠͎̠͕̩̬̣̗̞̘̠̱͙̮̝̬͑̑̐͂͛͌̽̀̊̔̈́̏̆̏̇̇̈́͋̍͂̉͌̈́̀̓̂̅̑̓̀̐̏͑̋̍̚͝ͅ",
   "ḩ̷̧̨̨̨̛̛͎̩̘̩͍̤̙̼̗̜̳͔͈̱̥̹̣̦̟̮͍̭̦͇̺͚̗̭͈̘̘̩̬̳͇̺̯̙̟̫̗̊͊̈́̾͑͘͘͜͜͠ģ̶̟̲̘͕̩͖̗̞̗̫̒̅͝ư̵̢̧̙̥̙̭̲̠̞̙̜̙̘̪͙̭̱̘̮̦̜͖͍̺͔̗̺̺͇̰̫̲̟͚͉̺͎̗̘̣͈̍͋͗̉̌̌͌̅̒͌̏̅͑̇͛̈́̿͛͆̈́̾͂͊̎̚͜͝͝ͅͅơ̸̡̛̦̳̲̒̒̽̈̐͛̓̏́̋̓͗̑̀̓̇͛͐͑͂̅̔̏͆̀͘͝͝ş̵̢̧̠͈̼̟̠̹̬̗̬̙̗̯͙̱̍̀̓̆͆̇̊̏̀̂̇̾͜ͅd̵̢̨̢̧̛̖̦̟͉̟̺̝͖̤̳͓̝͇̻̤͎̱̠̞̝̦̖̯͙̣͇̼̦̫̭̲̹̗͉̹͓̺̩̰̩̍̈́̏͑̑̎̍͐̃̂͒͘̚͜ͅh̶̨̩͔̖̟̼̝̥͓̯̥͇̫́̃̂̄͐̆̄̈́̅̃͒̈́͐̈͝ͅf̷̛͍̪̥̞̣͉̤͉̐̇̾̔̎͂̾̃̉̊̒̃̆͛̇̾̇̇́͒̎̂̉̉͗̅́̃͋̅͐͌͊̇̂͊̅̽̚̚̕͘̕̚̚ṋ̶̢̧̪͔͔͎̻͉͙̝͔̣̬̪̲͙̲͔̱̞̳̜̻̯̗̤͍͈̺̼̱̦͈̯̘͎̳̘͙̍̏̍͗͆̌̌͐̀̆̆̃̈́̆͗̉̚b̴̧̢̛͚̻̯̭̘̫̠̪͑̇̽̒̀͂̓̑̃̐͒́͊̌́̐͆͛͊̔̄̊̊͛̆͋͊͛́̀̐̽̂̋͂͋̓̕̚͘̚͝͠͝͝j̷̡̢̡̨̺̭̣̥͚̳̙̘͓͖͍̜̜͚͕͔̘̼͚̞͖̺̤͙͕͖̝̞͉̤̠̉͋͌̐͊̆́͆̑̈́̈́͑͑̕̕͜͝ò̴̬̺̱̆̀̈̂̔̀͝s̴̛̰͖̪̯̲͍̼̱̫̲͓̱̻̥͓̟͍͍̜̦̲͙̹̲̙̄͂̋̽͌̿̆̎̌͗̽̂̿͒̀̑̉͛̿̐͗̌͒̂̔̚͝͠f̷̧̧̧̫͓͖̮̼̺̹̹̜̜͈͖͉̥͚͇̩̰̼̺̦͔̼͈̼͙̻̥͕̣͎͎̩̦̹̝͚͈̭͙̙͇̲͓̜̔͆̍͜͜͝n̶̨̞͔̖͍͍̳̳͓̜̱̳͖̻̮̠̰̙̤̭̩̣̘̱͍̻̟̲̝̖̹̤̜̄͒͑͆͐̂̌͗̏͑̐͘ͅo̴̧̡͕̟͓̣̯͚̺̦̝̜͖̜̰̟̲̰̿͗̐̓̔͂̔̊͊͒̅̂̈́̽͆̃̚̚̕͜i̸̧̢̨̛͈̹͚̤͕͈͎̻͔͉̫̭̜͓̟̘̳͙͍̭̼̭̘̦͖̘̭͚̳̳̬̯̗̣̦̬̖͊͐͆̆́͊͊̈́̇̄̓́̄̇͗͌͜ͅb̴̧̨̨̳͖̭̜̜̠̼̟̙͍̯̫̙͖̻̫͚̞̹̱͇̰̹̭̞̞̫͉̄̃̉̂̅͌̂̓̂̇͂̎̒͐̏̆̐̿̌͂̐̈͑̋͗̾̌̈̚̚͜͠͝",
   "h̶̤̗̰̉͊̂͛̉͠ȋ̵̧̧̧̨̘̪̭͈̗̩̝͉̥͖͙͖̫̮̦̪̥̖̟͖̼͔̤̠̫͖͓̰̬̤́̃̐̌̆͊͗̍̌̀͐̄͌̊̎͒̀͐̕͜ͅö̸̡̬̜̪̦͉͍̩̹̣̰̝̝͎̱̣̜̝͖̹͓̍̈́͐͒̕ḝ̵̛͕͇͔̬̱̙͓̺̟̺̜̙͚̰̀̾͊͂́̒͗̀̑͊̌̓̌͆͗̐̊̂͗̀̅̾v̵̪͍̲̾̽͋̉̆̔͆̏̋̃̈́́̅̈̑̎̑̑͊̓́̇̽͠͝͝ ̷̧̛͕̘̱̟͍̠͕̺̺̲̩͉͙̮̬̯͙̱͖͖̙̤̲̊̓̌͑̑͒̂͑̊̒͐͑̌̿̅́̚͜ḡ̵̰̘̥̹͍̳̜̮͉̬̺̪̗͇̭̲̻̙͊͛̓͊̐͑̕ͅ",
   "h̴̡̡̡̡̛̙͖̦̖͍̻̳̦͙̞̤̦͇̦̯̲̫̺̮͓̗̱͈̦͓͑͐͒͐̋̓̋̆͌̈́̉̒͒̽͗̀̒̑͆̀̓͊̋̓́͋̽͒̒̀̃͛͊͂̀̿͊̊͊͘͘̚̚͜͝͝͠ͅȋ̴̡̧̡̛̛͙͙̣̠̦͕̤͕̯̳͈̘͔͓̻̱̤̲͇͍̜̝̟̩͚̟̹̫͚͓͉͇̯̤͎̻͈̍̒̇̐̃́̎̀́̈́̋́͂̈̾̍̃̽̋̊̉̈́̇͒̇͒̓͆͂̆͆͒̅̂̍̅̆̆̚͜͝o̸̧͉͇̙͍̼̤͍͕̹̣̻̻̠̩̫̙͎͕̮̊̄̄͊͊̀̈́͌̽͆͒͑͑͒̌̈́͛̎͜ͅͅȩ̸̢̡̢̨͚̩̦̲͓̦͓̙͍̟̭͇͓̦̣̗̥͔̫̲̰̠̅̈́̔̋͌͆͌͗̓͛͂̎́̓̀͐͛͗̔͒̀͊͒́͊̈̇͒͌͛͛͂̅̒̈́͐̒̇̐́͝v̷̤̲̰̱̠̜͔́̾̐͆̋̃͊̂̿̎̆͐̕̚̚͜͠ ̸̢̡̟̮̮͎͉͇͕͔̞̦̏͝g̶̛̛͔̗̘̩̪̑͒̍͂̈̌̅͛͋̓͋͒̆̓͊̄͂͊̎̕",
   "b̵̛͓̲̲͍͕̖̻̼̘̱̮̜͙̻̱̀̋̈́̓̓͂̋̈̈́̍͑̋͑̈̌̑̂͑̂́͌̀͌͒̒̒͌͆̐̀̏̔͋̍̓̄͆̃̽̇͝͠͝į̷̡̨̗̜͕͙̼̲̺̙̝͚̰̲̺̮͓̱̟͔͙̼͒̃̎̐̽̅͌̀̅̒́̽̑͒͋͒̑̾́͋̓̌̅̿͌̌̍̀́̕̕̕͘͠͝͝͝͝ͅv̵̼̟̹̯͉̬̖̦̺̰̘͖̘̱͎̜͎̗̣̬̻̙͉̦̰̤̼̖͔͔̱̫̦̹͇͈̮̲̗̯͕̎̄̓͊̅́̔̅̀̓̎̍̿̾̓̃͌̊̈̊̎̓͆͘͜͝͝đ̶̡̛̭͎͕̗̞̩͉̣̭̳̫͉̝͉̹̪͓̳̫̦̟̱͖̥̖͙̰̰͙͇̤͎̲͉̲͗̓͋̉͋̓̇͗̆̔͐̿̇̏͌̓͛̃͂̀͂͂͂̕͘͘͜͝͠͝͠ͅơ̵̢̡̨̨̛͍̙͙̤̤͓̤̣̮̭͈̬͉̣͍̭͓͍̭͇̥̗̗̙͓̻͉̼̱͎̙̙͉̰͇̱̪̈́̀̐̑͆̀͐̏́̄̎̌͑́͂̍͐̇͂̈̀́͗̐̂̽͐̅̉͐̃̇̌͜͜͝͠͠͝͠v̵̡̡̳̮̲̺̮̜̼̬͚̠͔͍̗͍̟̙͙̳̉̈́̉̾͗̉̑̽̊̓̍͌̂̐̈́̐̿̃̊̃̆͐̐͊̈̓͌̽͌̊̂̔̾̊͆̅̏̑̈́̎̉̕͘̕̚͘͘͜͝ͅb̴̡̧̛̛̦̩̖̬̪͈̻̮̔͌̑̎̒́̓͌̎̇͊̀̄̏̉̾̚s̶̢̧̡̫̮͖̣͇̜̩̰͎̹̰̯̙̗̬̻͈̥̫͙̖̭͕̝̗̬͉̤̠̪͉̗̜͚̳̤̜̬̓͆͌̍̽̅̆́̌̾͘̕̕͜ͅb̵̢̧̢̠͔̮̯͚͓̣̙͎͓̱͓̻̳͔͙̼͉̖̊͊̇̄͂̃͒̆̋̂̏͗͘̕͜͜͝͠ỡ̷̡͓͍̰͉̣̟̠̗̯̳̤̤̖̂̑̾̀͌̿̐̄̋́͝b̴̡̡̨̛̗̦͈̬̭̲̠̰̼̣̜̞̱̣̖̟̭̩̘̪̬̙̮̹̝͎̹͍̗̫͎̮̲͚̫̣̠̙̳̹̂͐̾͑̽̐̔͐̋̑̚ͅv̵̨̛̛̛̰̫̭͙͎̬̜̞̱͉̻̼̜̱̟̺́̊͌̃͊̿͆̅̀̍̎̄͗̿̂̎̎͊͌̿̿̂̾͂̓̅̏̿̅̇̊̇͂̏̽͘̚͘̕͠͝ḩ̶̧̢̧͇͔̹͚̞͉̘͎͉̭͚͔̦̒̎͌̈́̃͐̊̂͊̓̀̋̒̓̆̄̽̈̈́̓̋̍̇́̋̀̇̀͊̎̔̄̓͜͠͠ͅġ̸̢̨̢̭̳̹̭̬̗̯̝̘̲̥̭̩̫̳̦͍̳͈̥̺̮̘͖̟͖̺̰̩̿͒̽̃͆̈́͛̍̓͐̉͗̇̈̀̋̓̊̉̅́̍́̌̃̿̕͝ͅͅͅͅì̸̡̨͕̥̜̹̠̲͕͔͈̥̟͍͈̲̟͓̯̩̗̭͖͖̣͓͓̟͍̪̈́̂̃̒̃̈́́́̓͑̄ͅͅw̷̨̨̧̡̛͖̗͇̻͉̹͇͚͎̘̩̥̳͉̪̮͎̩̪̪̜̠̯͂͆̀͌͐́̉̎̅͑̅̕͘͘͠p̷̨̧̛̬̻̤̹̰̼̠̭̭̳̠̫͓͙̞̖̦̥̰̫̮̪̱̤͎͔̠̯̙̮̹̥͇̫̘̫̬̠̮͔̪̟̘̥͎̏͋͆̃̔͑̌̐͂͒̂̽͛͗̃̉̑̉̃̍̉́͑̓͋̉̈́̑̾͆̚͘ṙ̴̡̢̡̧̨̛̛̼͔̪̰̟̖̹̪̞̖͚̫̟͔͔̫̝̙̘̦̬͉̺͈̹̣͕̬͕͍̫̤͍͍̯͇̬͖̠̀̍̊͛̈̈͛́̉͋̊̊̉̆̽̈́͂̊̃͗̎́̅͂͑̈́͗͗̄̽͒̕̚͜͝͠͝͠h̶̡̧̢̢̯͍̦̩̥̙̼̺̣͇͓̥̭͈̟̱̬̝̩͓̣͎̹̤̭̖͚̬͛̿͛̎͐̿̀̔̆͆͂̀̆̐̐̈̑̂͂́͑͋͛͒̈̂̚̚̚͘̕͜͝͝͝ͅͅģ̶̥̺̗͇͖̤̩̗̹͓͎̼̰̤͎͙̞͚̞̲̳͇̈̊̏͒͐̐̈́̽̇͌̅͐̂̿̇̉̓̇͂̈́̇͌̀͂̆͒̋̌͗͋͆́̈̑͌̚͘̚̚͜͝͠͝͝͝ͅi̸̢̧̨̢̨̝͈͕͎̣̩̻͔̤͍͉̳͉̳̦̝͎̮̲͓͉̦̖̔̊̉̽̆̄̾̃̅͆̉̿͋̂̌̇̓̏͌̔̓͗́͋̄͒̑̑͐̀͊̔̓̽̀̿̓̉̀̓̕̚͝ͅk̵͎̼̞̝̙̠̿d̴̛̘̳͉̹̥̜͎͍̹̲̘̭͕͗̐̌͆̃̀͒̉̾̽̄͛̽̌͘̕͜͝͝͝ͅḩ̸͙̗̙̲̞̰̣̰̞̖͔̬̜͖̝̳̠̪̯̯͔͈̱̫̦̟͔̦͖͓̈́͜ͅi̶̧͎̞̝͓͚̗̣̞̮̮̖̤̟̗͕̟̫̠͍͇̙̺͎͉̦̘̩̔́́̏̈́̒̎́͂̀̀̔̂̉̈́̓̄̿̍̕͜͝ͅp̸̨͇͚̼̮̮͕̗̭͉̣̟̗͎͓̦͍̺̓̔͂̓̒̒͛̌̎̓̈́̊̊͒̈́͆͌̇̃̐̚̚̚͜͝g̸̡̨̡̢̢̯̦͚̫͈̫̘̫̬̯͎̬̹̖̬͙͚̩͓̭̻̪̭̻̟̺̦̥͍̲͚͉̯̥̖̹̗̭̦̙̔́͜q̴̨̢̢̞̭̗̘͔̲͖̼̪͚̼̱͍̜̫͔̲̯̮̜͔͉̦̈́͋̈́́͛͂͂͑͒̈́͗͑̋̈͊̍̈́̓̽̄́̇͐̑͋͜͝ͅͅh̷̡̡̡̧̨̳̤̲̤̤̞̹͙͖͎̰̠̲̖̮̹̬͉̩̳̟̰͈͓̱͈̪̟͓͚̳̩͓͓͙͉̰͔̦̾̊̌̎̂̏͂̒̇͜͜͠ȩ̴̨̢̢̧̛̜̝͚̣͎̱̤̫̝͈̟̮̙̮̝͈͔̪̞̥͕̥͍̦̟͖̭̠̥̖͙̥̞̊̄́̾̓̎̆̆̃̽͐̇̿̒͛̂̃̿̎͑͌͜͜͜͝p̶̡̼̻͚̻͇̻̠̲̟̺̤̼͚̻͎̤̈́͠į̷̨̡̨̡̘͙͉̪̩̲̝̜̪̤̠̝̜̫̠͔̣͕̝̦̤̰̣̜̗͇̘̥͍̳̪͚̣͎̦̬͍͚̂̈́̀̈́͐̓͒̅̿͒̀̑̈̒͗͒̑͗͂̅̀̀̓̈́̑ͅg̶̢̧̯̘̠̞͍͉̣̻̰͚̬̼̣̼͍̼̬̦͌̎͒͑̆̈́̈́̓̆̈́̆̑̿̌̄̽̒͋̈́́̇͆͐̕͘̕͜͠ͅͅf̷̡̪̤̭̭̱̪̞̲̥͖̮̹͇͚̻̬̜͓͙̮́̄͜h̸̡̡̤͙͈͍̜̫͕͍̟̭̭͕̜̣͇̫̼̞͍̜̪͔̰͖̺̣͎̗̱̬̼͚̩̯̗̤̙̤̹͈̹̝̝͓͎̅̉̊̓̍̐̈̽̾͋̽̌͗̋́̎̉́͊̈́͊̈̂͠͝ͅj̸̧͚͕̝̩͓̙̣̪̺̬̗͍͎̰̿͗̐͆́̀̎̈́̈́̄͘͜ͅͅo̶̱̮̠̼͌͐̃̓̍̃̉̈́̾͊̂͊̈̍̇̀͆̉̍̾̉̾̈́̒̿͒͋̍́̇̐̇̀̉́̕[̶̧̡̡̛̘͚͖̗̪͓̱̫̩̱̰͖̫͓̝͓̺͉͙̻͍̈́̀̿͋͐͛͛̌̽͆̓͂̒͋͊̆̈̌̔͂̆͋͌͂̐̉͊͑̋͐̌̿̎̽̿̊̆̈̚̕͘͝͝͝͝͠q̷̧̧̨̧̛̖͇̥̰̰̳̬͈͇̱̤͕͎̟̘̹̹̲̦͖̲͕̞̞͕͈̣̭̜͈̫͔̤̘͔̖̠͖̲̹̒͂̇̃̐̄͋̒̃̇̑͒̋̄͂͗͑̓̈́̀̊͘͜͠͝͝ͅj̴̛͕̜̲̖̹͖̖̩̝̈́̍̔̎͆̌̊͒͑̒͋̌̀̎̋̉̋͗͗̈́͑͒͒̌̈́̎̂̄̒́͒͘̕͝͝͝͝q̷̨̧̨̝͚̥̭̞̪͚̠̣̦̦̹̖̩͎̱͓̮̞̗̿̇̔̏́̽ͅͅc̸̛͉͚̬͇̺̹͖̙̳͎̳̠͕̬̮̣̦̫̳͚̮͙̰̲̯̥̄̒̈̇̈́̽̆̾͐̈́̈́̈́̄̿́̾̋̔̈́͂̇̕͝͝ͅd̶̢̢̧̢̨̨̨͉͇̻̯̳̗͇̫͍̤̭̥̟̹͕̮̺̳͖̥̣̬̪͈̘̝̮̰̺͔̱̬͕̜̹̰̫͖̿̌̍̑̎̓͜͜͠͝ͅn̷̢̨̨͓̬͈͔͓̗̗̼̦͇͕̙̣̭̩̦̻̫̗̮̗͈̥̣̳̞̠̯̻̩̝͉͖̐͒̇̅̈́̈́͒͒̄̍͐̎͋̎̀̐͜͝͝ͅk̸̨̡̢̨̨̧̛̪̬̣͍͈̦̮̙͔̗̤̘͖͓͚̣̯̜̩̩̭͒̋̉̿͌́̓̈́̀͒̾͆͂̏͂̎͂͐̈́̏̀͋̇͊̓͐̀͛̈́͛̅̔̏̂͘̚͘͘̕͠͝͠v̸̨̨͓̗̗̱̣͖͇̙͕̮͚͐͒̀̀̔́̃̒̐̒̇̈́̅͊̅́̐̕͠͠n̵̡̨̛̛̙͇͔̭̝͉͈͙̦̙̮͓̹̘̞͇̫̗̭̣̣̜͓̯̝̭̻͚̥͎̗̞̫̘̺̳̔́̆̃̀̀̒̀͌́̅̈́͒͛͐̈̐̈̀̓̀͑̀́͑̌͒́̆̎̅̅̓́̑͋̔́̅͆̈́̕͝͝ͅų̷̨̡̛̥̻̺͖̜͉̗͕̟̭̖̝̲̬̰͚̖͇̬͍̩͈̦͔̗̤̬̣̯̯̘̬̹̖̫͓̻͙͔͕̮͌̅̐͗̾̔̂͊̈́̓̍̓̐̈́̇ͅs̸̨̢̢̩̞̣̜̙̪̫̘̰͙̤͇̩̳̖̦̺̼͚͕̅͒́̽͌͋͌̅̽͜͝ṙ̶͔͉̳͔̳͚̜̙̻̯̱͙̩̺̥͍̝̯̿b̴̧̛͍͔͈̫̠̣̬͖̦͓̣̆͆̎͗̈́̒͐̌͋̋̃̓̊̃̊̔̍̈̀̋̉̏̄̋̾͒͊͐̕͘̚̚͜g̸̨̡̢̡̧̛͖̣̪̰͔͕̳̩̫͕̮̟̦̼͕͇̻̩͍̳͈̼͚̱͉̠̫̹̗̗̖͍̍̎̄̿̿͌̾͛́̄̐̈́͌̊̔͌̈́̏́̈́͋̔̑̂̑̑̇̽́̾͌͆̅̉͑͌͛̎̒̅̿͋̊͘̕͘͘͜͠͝ͅu̸̧̡̨̡̨̧̙͍̖̞̯͍͖̭̪̟̬̺͙̹̱̺̗͔̫̖̗͔̻̙͖̞̹̜̰͎͉̣͓̣̹̹̟͓̥̗͆͜ͅį̷̛̜̮̱̠̰̯͆̏͌̾̌͑̅͋̊̈̄̽̍͑̒͂̑͒͊͒̉͗̇́͋̀̇̈̒͗̈́̿͋͗̋̅̕͘̚͘̚͘͘͝͝ṟ̴̢̧̡̱͚̲̦͙̗̠̱͍͔̮̘͙̰̮̹͎̼͉̞̥̼̗̮͉͎̗̯͇̫̩̖̳̺̺̦̆̎͂̄̏̔̌͐̃̈́͑̓̽̃͐̆̾͊͋̏̔̊͆̈́̑͂͘͝͠͝͝͝ͅợ̷̡̛͖̣̮̦̙̟̈̅́̑̋͑͌̇̽̈́̅̄̃͋̈̿͗̓͛̂̑͂̅̋̓̃̀̚͠͝ͅh̸̢̨̢̛̪̺̖͚͙̣̲̘̝́̅͌͛̽̄̇̈́́̔͆̀̾̊̐͜͜ȑ̶̢̡̢̧̧̙̤̰̖̗̬͉͙̥̟̘̟̬̗͔̗̞̙̭͔̲̻̩͙̤͖͚͈̬̙͉̼̭̞͓̳͙̦̦̙͕̥̙̉̀̓͑͒̈́͌́͗͜͜ė̸̢͚̣̯̫͓͙̣̥͍͖̭̫̝̦͉̻͇̦̪͓̜̺͚̞̞̆̆͌̆͝o̵̧̡̢̢͓̩̰͙̣̩͕̬̱̖̱̻̯͉͕̪̱̲̟̠̯͉̗̬͚͉͙͕͙̬͈̜͍̮͔̞̺̽̔h̶̨̛̛͎͓̬̭̣̻̗̠̮̹̞͖̭̪̟̯͔̬̪̤̗̗̗̝͔͗̿͗̇͌̆̔̒͌̽̂̊̃͐̔̀̎͋͌̽̾̾̾͒͊͑̇͒͑͆̄̿̐̑̈͆̿̾͒͌̑̽͜͝͠g̸̟̗̥̑̽̾̊̐̎̕͘̚͝͠͝i̵̛̛̛̲̬̝̟̖͚͎̫͍͍̖̞͚͇̱̗̙͚͇̫̠͉̗̭͔͈̻̊̅͂̽̍̌̈́̾͗̉͂̽̈́̊͌̒̉͑͒̅̂̀͒̓̋̋̉̓̄̒̕͘͠͝͝ṵ̶̧̧̠̱̩̮̥͕̻̗̣͙̫̠̝̯͉̳͙̹̙̠̗͔̆̋͆͑̀͋́̍͘ͅj̶͉̬̰̳̻͖̠̯̼̙̬̦̝͚̞̦͔̦͚̙̖̟͖͕͉̼̞̘̤͖̺̣̹̿͛́̿̈́̃͆̆̈̓͂̔͒͋͗̒̌̿͑͗̉̾͂͘͝͝͝͠f̷̢̢̧̡̨̙͖̠͚͎͉̝̞͙̣͎̙̮̥̼̤̰̜̥̹̤̭̪̰̐̍̃͑̓̀͋͗̐̆̽̍̓͐̉̌̿́͂͐̍̍͛͊̈̊̎̾̾̃͐͆̈́̊͋̍͌̂̂̾̀̉͜͝͝͝͝͠ͅͅͅp̸̧̡̧̦͚̤͓͔̻͇̹̫̬̘͇̩̣̰̝̙̾̊͌̔̆̓͘͘͝v̷̨̧̧̹̠̪̙̼̼̙̹͉̬͍̱̮̳̗̖̲͇̘͔̩̟̬̩̳̟͇̙̖̥̼̙͇͖̝̯͙̋̍̍̾̆̈̇̂̆̒̃͌͐͑̈͒̊͘̚̕͠͝h̶̹̩̦̦̞͌̒̍̈́̿͌͆̔́̊͌̂̓̊̾̌̍̐̏̈́̎̐̽͋̈́͂̈͌͆̊͆͑͛͒͋̍̋̃̂̿́̕̚͘̚̕͝͝ư̴̢̧̨̛̜̼̻̫͈̞͙̞̦̝̗͇̦͉̖̜̘̱̣͉̖̟̻̖͎̬̥͚͇̹̪͙̺͂̎̎̎̓̄̉̉̄̇̈́̎̒̈́̊̇̅̋̇̕͘͠͝ḃ̷̨̢̡̨̛̛̩̳̼͔̯̗̜͖͎͈̘̬̞̲̼̳͙̙̤͈̭̩̘̗̜͈͎̱͕̝͇̦̋͋̽̀͑̓̔̓͗̾͐́̅̓̾̍͗͊̃̏͘̚͜͜͠h̴̢̢̡͍͚̫͈̮̠̪̬͖͙̲̘͎̲̯̠̫͔̲͖̜̹̳̮̰̦͍̗̗̙͈̺̣̝͚͈̼͓̗̪̖͖͛͋́̅̇͌̈̃͐̔̑͆͛̋͆͂̂͑̉̊̍̀̀̀́̑̂̑͂̄̔́̈́͛̅̋̓̄͋͋͌͆͊̆́̓̚͘͜ģ̶̛̯͕̩̯̙̼͖͔̤͔̦̜̩͎̜̘͎̺̰̫͔̠͚̮͚̜͎̮̰̞̙̝͕͌̀͒͐͊͒̆̓̇̌̀̓́̈́̎̽͑͐̑̿̒̏̅̋̽͆̄͗̽̔͑͑̽͌́̅͗͌̐́̚͘̚͠͝i̵̧̧̛͖̹̙̗̗͎͙͓͇̫̻͈̝̠̘̥̰͚̹̱͋́̋̈̆̈͆̇̎̀͐̑͑̑̎̈́̈́́̒̆́̉̎͐͋̑͂̔̍́͆̌̈́̚̕̚͘̚̚͝͝͝ų̷̨̢̢̹̭͓͖̖͕̤͍͙̮͓͓̺̱͇̼̦̠̪̦̙̳͕͚̹̪͈̗̱̟̭͖̳̙̳͚͉̯̘͎͇̺͇̲͐̌̓̿͌́̈́̔̌̑̓͆̅͊̅̂͌̓̓̐̈́̓̀̃̏̕̚̕̚̚͝͠ͅͅp̸̧̨̧̹͕͔̥̹͓̤͈̠̮̮͙͓͈͇̯̰̰̗̪̻̞̮̤̞̭̰̰̳͎̗͉̝̜̭̳̥̍͜h̵̢̞̟̼̳͖́̅̊͛̀́̃̂̌̂̅͋̍̔͋́̾͛̿̕̕͝͝͝ͅg̷̢̨̧̢̧̡̧̛̪̻̹͙̱̪̠̙̫͍̰̗̪̳͇̝͇͓̦̣̹̱͇͓̗̲̭̥̉̈̈́͐̒́͊̊̍́̈́͗̈̽̃́̈́̉̒͑̊̂̅͂̆̂̀͆̉̐̀̍̀̓̅̃̌̊̚͘͜͝͝͠ͅį̷̨̧̨̯͚̞̦̥̣͇̻̪̥̗̫̠̲̝̥̠͓͍̼͓̺̯͈̠̙̗̳̱̝̮̻̫̠̹̻̣̟͇͙̬͇̝̀̾̍̿͌͐͐̀̀͆̂̄́̓͗̆͒̈̈́͗̐͜͠͠͝͝ͅù̸̡̡̞͍̤̮̮̜̩̞̩̼̼̥͇̰̲̹̹̻̺̲̙͍̤̭̝͛͜͜͜ͅṛ̴̡̢̡̢̯͍͚̠̹̬͔̱̩͍͙̦͎̫̫̥̫̼̟̜͍̦̻̹̣͍̦̻͚̠̳̪̥̘̣̪̬͌͗̎̎̾̑̈́͋́̇̓͗̓̏̀͋͋̈̀́̔̕̕̕͜͜ẽ̵̢̡̥̣̳̣͈̰̞͙̥͍̠̣̩͍̖͉̼̓̍͑͐̂̉́͐̂̅̃̀̒̑̀̀̏̔̈́͛̈́́̐̈́͆̾̋̒̃̐͂̌͐̕͘͘̕͜͝͝͠h̸̨̛̛̩̞͕̺̜̜͖͖͈̪̜̺̬̭̪̜͇̀̏̀̔̅̓́́̾̐̔͆́̐͒́̍̊͊͐̏̋͌̎̐̏̈͋̀͋͊̽̃̆̏̆́̄̾̌̊̕͝v̴̧̨̱͔͇͚̼͉͚̫̹̫̮̟̯̜͖̲̰̝̤͖͕̭͎̦͖̮̲̯̳̝͍̋͐̒͂́̆̏̆ͅj̴̡̡̨̡̛͔͙̻̖̦̟̬̝͍̺͎̠͙̯̙͓̜͉̪̙̱̲̳̆̂̄̆͋̀͜͜n̵̛̲̝̏̒̈́̌̂̒̈́̍̉̍̌̄̂̇̔̍̇̈́́̾̀̓̆̀̓̀̈́̀̓̔̐͐͘͝͠͝f̷̡̧̢̧̢̛̣̜̥̺̪̦̞̳̠͖̬̻̫̹̳̪̰͙̠̯̩̘͈̙̫̩̫̻̗̣̫̦̖̖̥̙̪̘̘̣̑̿̓̋͌̀͂́̎̈́̆̉̊̋͂̐͂̋̉̊̂̏͑̌͐̈̓̆͒͐͌̈́̿̈́̽̑́̌̆͒̀̆͌̆͘͘͘̚̕ͅͅr̶̢̞̣̞͚͎̗̜̠̲͕͕̖̝͎͉͙̘̖͙̰̣̲̲̟͎͓͓̜̝̜̲̔́͛̋̏̏̐͋̑͑̋̀̔̔̾̈́̅͊̄̈́͑̈́͌̌̈́́̌̐̓̈́̽̒̔̋̐͐͊̆̒͋̔̍̕͘͠͠͝͝͝ͅŗ̶̹͙͇̼͕̮̣̙̜̘͂̍̐̊̃̄͝͝q̸̛̛̛̳̹͇̻̺̗̻͚̳̼̖̯͊̂̃͐̓̂̿̊̔̄̓̎͒̏̿̿͋͐̓̔̊̓̾̑̽̽͗̾͗̂̅̍̇̽͑͋́̿̌̇̕̕̕͜͝͝i̵̢̢̨̡̡̛̛͓̺̱͙̹͇̲̳̫͔̞̥̩̖͔̰͙̭̠͇̯̬̗̭̳͙̙͇͚̩̫̯̍̋̌͊̓͊̓̓̈́̓͑́̎̈́̂͐̑̉̓͗̔̔͂̈̂̑̒̀̈͒͛͋͘͘͘̕̕̕͝͝ͅj̸̨̧̡̨̢̢͕͚̪͓̞̞̪̰͍͓̠͙̞͙̱͉̮̥̣͙͕͍̫̗̩͉͉̼̜̱̤̭̥̰͎͎̽̀̈́̀̇̇̍̀̏͗̀̌̈͛̿̈́́̅̊̏̍̚͘͜͜ͅͅͅử̴̢̧̡̛͎̝͈̮̥͇̭̯̣͎͇͚̣͉̟̟̤̱̠͕̪̱͖̮̰̼̘͕̜̫̖͚͖̮͔̭̮̖̦̭͙̱͍̉̃́͒͊͒͑̓͑̈́̀̐̍̂͋̀͌͆̒̐͑̄͒͂̈́̉͐̀̾͒̽͑͂̄̈̂̕͘̕͜͠͝͠͝͝͝ͅͅͅb̶͉͍̳͈̹̹̩̜̼͉̥̘̫̥̟̤͊͆͑̎͋̇̚̚͝͠ğ̵̡̨̧̗͈̝̲̞̮̰̤͙̬̹͈̝͖̹̖̬̼̹̥̹̺͙͇̭̝͔̥̝͉͈͜ͅe̸̡̧̨̘̬͉̬̜̙͓͖̟̼͚͉̲͖̹̞̺̳̦͔̙͇̲͙̥̲̜̖̦̳̟̭͎̭̟͛̈͌̈̿̏͗͐̏̾͊̾̈́̑͐̏̓̐̓͑̕̚͜͠͝͝͝ẖ̶̡̧̢̛̛̻̤̠̼͙̞̺̩̼͕̭̰̙̼̳͎̹̯̜͓͖̠̤͉̯̭̱̪̗̳͙̣͉͈̤͖̙̗̝͆̓̓͐̈́̃̅̇̓̇̈̎̒̄̉̀̔̏̎̐͐̋̀͆͋͗̐̕̕͝͝ͅŗ̷̡̛̥͕̳͓͙̯̟̳̤̩̝̗̗͇͙̻̗͖̥̳̩̮̫̻̳̳͔͕̠͚̼͈̯̠̫͓̜̤͒̓́̆̑͑͐̀̈̆̈́͐͗̒̄̃͒͐͗̅͘͘͘̕͝͠g̵̡̛̛͉̳͇͖̮̤̞̖̹̫̼̿͋͆̈́͛͒̅̈̓͆̈́͗͋͗̆̌͗̽͗͐͋̂̓͘͘̕͝į̷̨̧̡̧̨̡̛̲̠̮̥͉̰̫͚̮̮͈̬͎̳̘̤̗̘̳̖̹̫̺̼͔̭̣̳͚̠̤̲̱͔͕̝̲̣̱̻̑̆͐̿̔̍̄̏͆́͌̉̌͛̏͛́͐͊̅͌̃̓͗͆̾̈́͗̆̋͊͊̎́̀͌̄̋̌̎̚̚͝͝͠͠ͅư̸̡̧̡̛͔͈̰͖͉̬͓̯̠̹̺͚̥̭̳̪̤̯̪̱̟̫̭̝̯͋̐̈́͐̽̀͐̾͑́̀̀̑͆̂͐̈́͗̇͐͊̏͑͋̂͒̓̔̆̇̄̅̚̚͘̕̚͠w̸̧̢̡̲͍̰͙̺͙̟͖̪͎̪̩̯̳̼̟͎̞͔̬͙͖̰͈̮̤͖̤͔͓̳̾͒̀̌̈̓͆̊̎̚͜͜͝ͅj̷̢̡̛̝͎̦̠̥͚͓͇͙͈͇̼͔͈̍̔̈̋͑̈̈̓̿̒̔̾̉̍̕͠͝͝͠͠͝ḑ̷̨̢͉̭̥͈͓̪̗̼̯̠̳̳̮͔̠̭̻̮͈̥̩̜̗̣͎͇̫̲̤̩͈̺̳͖̳̔̓͆͛̈́͠͝͝͝ͅs̶̡̡̯̼̺̼͖̳̯̲͍̦͓̞͉̯͗̍b̴̢̡̢̨̛̛͎̳̩͇͔̰̞̹̩̖͖̹̞̼̻̣͓̤͇̝̩̙̻͇̳̠̣̦͚͇̼̬̖͔͍͓͇̖͎̯̘͗̿̊̿̊͋́̅̍͛̋͆̈́̿͌̎̑͗̊̍̇͆̔̀̋͆͛͑̈͊͑̿́̓̌̾̅̚̕̕͜͜͝͝͠͝͝ͅv̶̡̧̛̩̤͍͉͙̜͎̻̰͓̰̹͖͇̟̞̺̰̠̔̒̋̔̍̀̓̋̈́̇̄͋̋̄̽͐͜͜͜j̴̘̟̤̙̮͙̿̄̆̓͋͒͋͂̂̐̈́͐̕͘͝͝i̶̢̢̧̧̡͈̼̘̱̠̫̳̯͉̪̳̙͉̖͙̯̱̤͇̺̺͇̬͔̝̬̹̖͇͋͋̅̃͜͜͜b̷̡̨̡̨̨̨̧̡̛͎̳͚̱̥͕͎̩̭̥͍̺͇͖̫̲̪̩͈͈̞͍̗̲̜͓̫̣̗͖̼̺̼͊̍͋́̄̓͛̆̉͂̀͂̏̎̉͌͑͂̽͐̑̌̓̈̀͛̈́̽̍̄̇̈̅̃̆͊̈́̈́̀̋͊͘͘͘̚͜͝͝͠b̷̡̨̨̡̧̭̫̖̤̖̬̮̟̺̪̪̱̘͔̭̟͉̳̠̣̯̹̦̳͇͊̊̋͗̄́̔͂̐̈́̀̀̇͊͌̈́̌͗̎̽͑̆͐̕͘͝͝h̵̨̛̺͖̱͖͖̣̳͆̉̋͒́̍́͐̂̍̾͑͆̉̋̉̅͆̆̿̋̽̔̓̈́̍̇̉̄͂̓̍̽͋͂̐̓͗̍͑͘͝͝ẇ̵̡̧͇̖̜͓̜̝̬͚̱̱̤͂̍̃́͐̊̈́́̏̔̓̒̋͑̉̉͌̊̑̔̋͑̈́̂͌̽̾̈́̏̔̋͂̊͛̂̀̉̈́͜ͅỳ̵̖̯͚̺̫͕̗̝̰̲̟̝̭̲̺̙̜͔͕͙͋̈̇́͐̆̍͗͊͒̿̑̔̆̓̐̌̅̎͌̌̊̀͌̾̓̂͋͛͜͠͝ͅͅw̴̮͙͚͇̦̍r̶̡̨͔̞̲̱͇̘̮̙̜͔̤̻͙͖̝̘̥̙̜̭̣̤̘̜̯̭̦͉̜̥̘̮̣͉͍̖̩̔̾̈́̈́̈́̀͗́̚̕̚̕͠͝ͅͅg̷̡̡̧̨̖̻͇͕̼͔̜̜̙̠̳̥̥̬̙̖̪͎͙̜̬̎͗̍̈́̊̈́͜͝ͅͅy̵̢̡̧͍͖͓̻̥̖̩͉͖͖͕̦̫̮̙̘̼̖̦̖̞͚̦̤͓̿̌̾̈̋̐̎͛̄̍͌͂͗̏͝͝b̸̢̧̨̪̞̤̲̟̻̬̜̹̲͓̼̻͍̗̪̠͆̊́̒͂̎̀͛̍͋͒̏̃̄͐́͒̉͒͗́̀̍͂͊́̏̈̈̽̂͝ę̸̡̢̡̮̘͚͙͍̹̲̭̥̯̘̼͎̫̳̠͙̥͓̞͓̫͈̻́̇͛̒̆̈̉̌̄̉̂͋͒̈̌͊̾̐͆̆̆͌͂̄̄̿̈́͂̅͌͌͛͐̂̀̔̏̕̚̚̚͜͝͝ͅh̷̡̢̬̫̺̪̖̳̱͙͔̩͕̻͖͉̻̝̙̤̼̞͓̠̥̩̰̖̪̲̝̙̖͑̀̓̆̋̇̇̆̌̄͂̊̽̓̕̚͝͝j̸̡̨̧̨̢̺̦̻̫̳͓̻̦̮̰̳͎͔͍͙̘̄̓̐̌̈́͗̐͊͐̐̕͘̕͠͝v̴̡̧̡̢̛̛̫͓̤̲͚̭̱̗̖̠̳͖͓̣͈͕͖̝̯̯͙͖͍̙̣͇̲͕͚͔̞̠̐́͑̅̏͋̽̒͛̀͑͐̃̑̓̈͑͋̓̾̈́͑̈́̇̅̂̔͋̅̊̑͊̕͘͜͝͝͝͠ͅb̸̢̨̨̨̦͚̰͖̪̪̲͙̞̳̙̯̖͙̰͇͚̦̥̣̰̻͎̞̤̩̖̫̼͇̞̭̖̜̝́̈̆͌̋̈́̃̂͑̏̈́̍̌͗̆̈́̆̀̑̆̄̕̕͝ͅf̵̨̡̡̞̩̠̥̩͇̥̭͙͔̣̹͖̳̞̥͚͓͈̰̣̘̰͈̭͔̞͙̍͊̊̐̈̾̑͆̈́̑̀͛̓̇͊͛̅̈́̉͝͝͝͠͠s̶̡̧̧̰͕͚̬̠̣̰̯̮͚̱̟̣̪̝͔̺̱̬̼̩̓͐̍̓̉̀̒͛̊͑͒̽͋̌̇͛̓̌̂̇͠͝͝͠ͅk̵̢̨̡̨̨̛̛̰̞̭͚̫̭̞̱̩̱͖̮̩͎̯̺͇̰͉̟̮̣̝̼̟̖̮̜̫̖͍̟̫͖̼̩̐̔̅͑̓̑̔͊̉͋̏̄̈́̊̾̈͆̐͐͛̔̊̈̂͜͜͠͝ͅj̵̨̧̺̫̪̘̩͎̩̩̞͕̦̺̜͇̠͙̠̪̯̰̟̣̠̼̳͖̝͐͒̌̆̌́͂̅̒͒́̉͌͗͑̅̂̑́̂̐̽́̈́̃̆͗̀̋͑̀̂̿͛͘̕͘̚̚̕͜͝͝ͅh̴̢̡̡̨̨̧̛̛̻͔̺̣͙̼̤̦͖̬̠̪̼͎̤̩͎̻̘̩̙̹̹̥͖͚͓̱͎̳̪̱̻̥̳̰͙̫͗̌̊̃̏̆̅̔̏̃͗̽̿̈͊̈́͌̀̽̄̆̿́̃͂̾̊̃͒̓͘͜͝͝͝͠r̴̡̨̨̛̛͍̪̹͔͓̥̦͇͇̝̟͉̠̱͊͆͊̓͛̐̇̏̌͒̿̍̇́̋̍͐͐̆͛̾̒͒̈́͗̋̍̅̒̐̽́̉͋̓̎̀̋͗͋̽̌͊̕̚͠į̴̧̨̛̯͉̠͉̪͉̻̗̮̫̲̠̩͖̫̺̩̤͈̟̫̺̳̳͍̩̘̲̈͐́͊̋̈̏̀̒́̌͒̎̅̚͝ǫ̸̡̗̬̬̼̩̻̤͔͚̰͚̮̙̩͖͈͌͋̓͗͆͠w̴̧̛̫̠̦̪̼̗̣͎̹̩̩̺̳̱̺̺͓̰̹̣̯͉̹͍̻̥͚͚̺̰̹͕͉̠͑̂̿̃̏̾̏̓͋̽̐̇̀̀̋̾̋̏́͛̊̀̿͛̉̅̌̔̑̑́̈͊̆̌̂͗̉͛͆̆̚̚͠ͅḥ̶̢̡̡̱̺̯͍̳̦̯̗̻̘͚̻̤͈̺̖͓͈̘̦̖̦̗̙̓͊̔̄b̶̨̛͖̬̝̲̦̥̝͚̟͉͓̣͙̹̳͇̱̗͎̻̥͈͖͔̗̄̄́̽̓̏̎̒͐͆̾̄̔̈́̓͐͆̊̓̄̔͒̊̑̐̇̈̌͒̒́́̀̆͑̀̿̐͗̆̚̚͝ͅͅk̶̨̨͍̲̤̙͖͎͕̭̇̄̌͒̃͌͑̋̂̐̀̓͋̆̑̎̐͐͑̀̒̉̊͗̔̀̓̅́͌͘̚͠͝s̵̢̗͎̣̟̖̞̤͎̜̆͋̇͆̋̀͐͗̀̊̈́͐̀̿̓̆͌͐̅̆̃͆͌́̿̈́̈́̈́̓́́̀̑̄̓̕̕̕͘̚̕͝͠͝͠͝f̴͍͕̲̱̣̣͕͙̱̞̜̮͈̤̤̩̪͖̠͔͔͙͔͖͍̮̣͕̲̩̲̝̹̦̲͎̭͈̊̄̃͛̾̈́̈̉͐͋͊̂̎͐̈̈͑͂͌͋̓͂̓͊͒͋͌͐̓͒̾͑̓̊̒̿̒͘̕͠ļ̸͙̭̲͔̲̺̝̟̭͇̹͎̭̼̤̰͌̏̓͛͋̾̒̋̈̆̊̌̆̈́̂̀̏̋̈̓̓̆̅͆̉̐͆̈͋̐̒̚͜b̴̧̡̡̡̗͓͚̬̩̬̖̥̦͈͔̗̜͔͚̱̠̦̙̬̹̮̞̙̰̹̗̮̺̤͕̳̙̫̀͌̈́̾̾̐͛̑̍̎́͋̎̂̏͑̇̔͆͜͜͜͝͝͝ͅv̵̢̪̮͎̲̗̞̬͂̍̐̈̂̊̍̾͗͐̎͆͗͑̈́̾̊̓͌̓̀̂̆̐͋̇̈́͒͊͆̕͜͝͠͝k̴̢̢̡̨̢̢̛̠͎͚͔̝̲̣͖͉͍̙͍͈̝̼̯͕̠͕̩̙̻͚̥͓͖̗̻̖̝̘̫̥̊̅̎̀̀̓̂̽͂͑̽́̑́̓̈́̇͐̏̽̈́̑͊̓̚̚͠͝͝ͅͅj̸̛͇͙̮͗̓͑̏̈́̽̓̅͐̋͛͋̐̆̕͜a̵̧̨̧̢̢̨̪̱͖̜͙̺͎̻͉̗̝̩̲̤̲̞̻̖̭̱̤͉̜̦̦͇͖̬̼͙̹͎͕̩͔̯̞̼̠̮̻͇̪͊͒͒̒͒͋̍́̚͘ͅd̸̨̨̡̢̢̢̗͉̘̥̹͔̜͖͔̲͓̟̟̗͎̼̘̗͓̮͇̠̘͚̜̹̗̰̱̙̺̼͓̙̜̗̤̭̝̋́͐͑b̵̺̯̙͓̗͚̗͙͉͕̩̗̹̥̼̖̰̳͔̬̭̿̓̃̐̇̓̓̿͌̅̐̌͒̈́͐́̈̑͑͒̉͂͆̈̒̂̂͐̆̔̈́̕͠͠ͅͅj̶̧̨̧̳̥͓̭̳̝̙̹͙͍̺̙̜̭̪̠̤̗̭̙̮͔̠͙̖̰̙̗͚͙̟̰̮̩̥̠̭̒̽͌͛̈́͊̌͒̀̈́̊͊̍͒̂̀͒͋̎͊͊̈̏͒̑̒̈́́͋̆͐̀͐̔̊̂͐̄͒̔͑̽͘̚̚͜͜͜͝͝͠ͅͅͅv̸̨̡͈̫̞̗̭̮̩̪̥̟̼̘͇͍̟̹͎̘̭̣̎͊̀̅̾́̄̐̃̿͆͌̀̆͊̉͊̊͗̋̔̐̆̚͘͘̚͜͝ͅa̴̖͍̙͈̝̾̓j̸̰̣͙͉̪͓̫̬͎̫̀̏̊͗̓̒́̍͊͌͐̏̋̐͒͐́̊̀́͌̍̋̊̆͋͐̈́̔͒͑̇̊͋̾̚͝͝͝ḍ̷́̈́̎͋͂̀͂̀͂̿͐̽̏̓̌̒̈́̓̎̿̊̂̇̾͌̕̕̚̚͝͠ḅ̵̛̻̟̠̭̜̐͌̃͂́͛̏̈́͆̾̚͜͠͝͝͝ļ̴̛̥̞̰̲̠̯̩̺̺̟̗̗̪̖̝̱͔̗͚̟͖͉͓̥̙̪͉̳̖̱̺̖̮̤̺̙͉̇͊̃̃̊̑͂͊̈̊̿̌̀̅̄͐̓̈́̍̃́͋̃͂̃̒̐̾̌̐̃͗̎́͘͜ͅf̴̨̢̛̭̥͔̯̥̥̖̰͌́̍̆͛̈́͑͆̄́̃̏̑̎̆͆͐̉̓̿̍̋̌͋̂̈̎͌̏͂̀̑́̃͐̋̄̀̉̕͘͠͝͠͝͠ḧ̴̡̧̧̨̧̛̠͔͚̳̻͖͔͎͕̝̘̟͎͚̺̬͙̙̭͓̦̹̝̳̠̝̫̜̤̘̹̑̾̓͑̄̑̔̈͑̍͑͗̔͗̓̔̄̌̓͂̽̃̑̈͊̒͐́̈́̌̏͋̿̀͂͗̔̕̕̚̕̕͘͘̕͘͜͝͝ȩ̴̨̢̡̢̛̝̘̬̼̲̹̗̲͉̲̹̙̣̺̞̺̣̺̭̗̼̗̝̭̭̗̱̥̫̩̯̬̯̳̩̬͍̺͕̓̂̅̈́̈́͋̋́̉͂͗̂̕͜͜͜͝͠ͅư̵̹̖̞͖͉̓̏̅͊̒̅̈́̀́̂̈̓͒͊̒́̅̿͌͐̀̽͌̋̈́̚̚̕͝h̷̢̢̨̨̢͈̱̳̱̭̻̪͎͉̳͎̭̘̖͉̳̳̯̞͓̰̻̫̣͚̬͔͇͍͖̲̔͛̈́̂̈́̇͗̐̀̊́͐̔́̏̎̒̈͂̾̓͗́̆̒̐̓̔̅͜͜͝g̵̨̨̛̛̛̛̠̲̙̪̥̲͙̥̀̔͆̇̄̃̍̔̍͂̒́͊̆͌͂̉̈͑͗͋̃͊̓̑̚͘̕͠͠͝o̸̧̨̯̙̟͚͓̲̗͉̘̘̭̮͎͍̙̻̦͚̦̦̰͇̱̞̖̜͂̅̓̂̈́̐̀̚͜͜ŭ̴̧̺̬͕̻̦̰̪̻̞̝̥̟̓͘f̷̢̧̨͕̦̠̜͓͇͉̫͕̹̺̠̙̻͓̘͚̮̗̥̟̗̫̹̼͍̮̭̪̬͔̞͖̮͕̺̠͍̲͕͐̽͌͑ͅr̸̡̛̛̛̼͛̅͛̇͌̈́̃̀̈́͗̾̃̋͊̈́̇̈͊̀̃̇͐̉̕͝ḧ̸̢̡͇̱͇̠̺̻͖͓̝̬͇̻̖̳̣͓̝̞̖̙̠̤͍͇̹̪͎̰͕̫͚͚͔̠̞̭͆͊̅͆̋̊̾̑͋̽͊̅͒̈́̐́̉̾̎̓̄͛̐̐́̿̅́͐͐̑̕̚͘͘̚͜͜͜͝͝͠g̴̢̨̰̤͇͖̜͓͙̼̖͕̫̫̪͕̠̺͇̙̫̠̻͉̠͖̪̪̟͈͈̘̪̙̖̼̪͚͖̭̳̩͆̔̉́̎̄̎͗͝͝͠",
   "ş̵̢̧̨̺̥̰̘̼̮̯͎̣̥̺͉̭̹̭̣̩͖͓̯͙̭̭̤͕̹͔͈̖̣̠̪͔̻̮̺̭͌̈́͆̀̿̄͑̅̀̿͛͋̍͂͘͝͝͝ͅợ̶̡̡̡̛̹̜̥͈̮͚͖͕̰̝̹̺͖͓̾̾̓͌̎̿̏̈́̇͊͑͊͗͗̎̅̏̈́͊̆͛̈͌͂͑̓͊̐͊̓̔̏͆̔͆͒̆̐̃̌̐̚̕̕͜͜͝ ̷̡̨̨̛̦̭͓͍̘̘̘͎͉̤̖̖͔̋̍̽̐̅̌̎̈̋͊͊̆͌́̓̈͐̉͜ͅţ̶̨̢̢̡̺͖̠͉̬̱͖̲̫̬̝̮̮̹͉̭̾̅̔͆́̋̐͌̈́̓̇ͅa̵̧̛̛̛̬̫̰̹͕̝͉͎̜̜̠͈̼̠͉͙͙̩̥̥͆̑̔́̋͛̍̍̿͋̀̎̈́̎́̊̀̑̈́̂͌̓̂̓̈́̃̈̓́̎̕̕͜͝͝ͅͅŏ̷̧̡̧̢̨̨̖̫̘̻͉̲̦̝̞̺̙̺͍͇̯̞̙̦͙̟̤̮̳͚̤̦̼͓͔̻͇͚̯̰͈̦͔̝̃̆̎͊͆͐̀͊̀̾͗̅̂̉͌͗̈́̈͑̔̀̊̉͆͒̾͆͗̿̈̾̚͜͜͝͠͠ͅͅ ̴̧̛̬͔́̊̇͛̓́̀̍̂́̾̓͊̑̏à̵͎͔̘͇͚̮̠̜̀͐̒̽́́̈́̐͠ ̴̨̛͎̳͉͍̰̣̙̰̝͓̯͓̺̪͙̻͕͈̘̟̇͗͑͆͋̎̅͂͌̀͋́̍̉͑͂̂̐̋̾͐̈́̕͘̕͠ç̸̧̢̮̣̬̘̗̘̣͓͑̌̈́̾̏̈́̍̎̓̌͋͊̍̂̋̇̽̔̉̒͋̍̾̍̌͑̚͘͘͝͠͝͝ͅǫ̸̧̧̛̛̝͙̞̲̩̹̼͓͕͉̳̟̖̜͖̫̯̜̳̬͓̙̬̯̯͗̈́̎̒́̎̈̎͛͒͆̆̂͗̅̍̊̏̎͛͒̾͂̉̇̿̌̓̍̅̚̚̚̚͘͝͝͝ͅn̶̠͚͎̥̦̳̭̦̲͉̰̪̻͎̺͓͉̝̝̯͐̇͋̈̒̔̇͐̽̑̀̄̀̔̀̈́͜͜ ̸̧͇͚̰̺̯̲̤̫̫͙̣̹̖͙̰͈̈̒͊̃͌̃̒̉̿͊͛̓̏̏̔̓̋͘͝c̴̠͒͆͌̂̇͆̋̓̋̿̓̌̐̀͛̒̋̿̔̅̆̆̓̈́̿̈̌̊̂̾̓̍̅̄̈́̈̑̕̕̚͘͠͝͝͝ͅḩ̷̨̢̡̧̜̦̙̺̺̺͇̻̟͔̮̮̝͖̭͙̻̲̙̣̟̖͈͚͎̦̳̲̘͎̥̱̬͉̗̲̖͋́̓͂̓̿̈́̈̐̔́̋̄̽̃̆̌̍̌̆͂͊̍̂͑̌͐̀͌̾̓̋̅͑̌͋̾͒̿͂̾̉̾͜ǫ̴̛̗̦̙͈̬̤̱̲̫̤͙̯́͐̃̐͌̐̀̑̑͆̿̇̒̀͂̽̑̂̑͘ ̵̰̑̍̐̇đ̵̨̡̡̢̛͈̬͓͎͍̪̖͉̯̙̠̫̗̝̰̟̼͓̮̜͙̠̀̽̆́͗̓͋͊̇̓̓̓̈́͗̽̑̈̿̑̉̀̈́̆͛̍͂̅̌̔̈̔̈́̿̈́̀̽̕͜͠͝͝͝ầ̷̢̛͉͔̟̳̟̦̙͔͖̫̪̺̩̱̃̈̀̏̊̈̊͊͛̋̒̄̉́̏̅̋͂͐̅͛̾̓͂̌̿͒͗̀͑̚̚̚̚͘͜͝͝n̸̡̨͖̙̩̙̙̙̩͚̫̱̪͕̞͓͈̟̘̜̘̰̥̙̮̯̬͈̘̤̥͇͉̝͚̬̊̓̎̒́́̌̚͜ ̵̨̧̛̩̗̯̳̲̣͎̤̙̲̺̱̺͕̝͚͎̜͙̦͍̯̥̣̝̺͍̓̓̍̋͋̿̒̈̆̃̇̾̿͋̓̌̇͑͑͆͌̎̕̚͘̕͜͜͝͝͝ͅr̷̟̹͕̬̯̳̘̀̇̄̐́̈́͂̉̈̀͂̀̈́͑͂͛͐̿̅͌͆̚͠a̸̡̧̢̨̩̠͇̘̹͎͕̫͚͎̰̻̺͙̣̼̰̺̲͔͍̣͓͉̤̲̯̯̩̣͍̫͙̫̼͇̖͓̹͓͇̥̠͌̾̔̈́̑͂́̎̓̅̈̆́̓̓͂͐͐̇̋̐͑̚͘̚̕͘͜͜͠͠i̴̮͓̤̲̟͕̲̖̰̪̬͎͓̺̠͚̠͗͌͐̔͌n̴̨̜͓̩͍̗̰̬̖̘͈̝̬̝͖̆̇̾͛̀͂̈́̈́̏̿̔̉̏͛̔̓͆̋́͆̑̔̌̕̕̚͘͜͠͝ ̸̢̧̧̡̛̰̲̼̦̦̹̞̰̥̮̤̘̼̘̤͕̬̱̼̳̬̯̫̱̦͉̈͊̽͑̈́̈͂̈́͛̌̅̔͂͌̑̓͑́̆̑̃͐͋́̋͊̌́͠͠͝ͅͅͅͅ�̶̢̨̰͙̣̠̭̠̐́͆̀̎̅̅̑͊̌͛̍̿͛̏̇̐͒͂͑̐̉̓̎̔̆͆̈́̈́̃̈́̍̐͆͌̔̂͆͊̀͘̚͜͝͝͝͝͝�̸̢̢̢̢̛̱̺̞͔̻͎̰̤̱̮̯̝̙̹̮͚̩͔̝͖̣̲͓̹͈̤̭͍̈̓͒̍̈̽͐̎͗͂̄̒͜͜͝�̷̨̻͚̠͖̪͙͎̬͍̖̻̹͎͇̪̱͎̼̫̭̳̦̭͙̱̟̜̘̫͈̪̯̦̮͈͓̀͛̊̾̈́̇̀̉̓̽̍̾͗̆̄̃͊̋̓̍͛̒͜͠͠͝͝�̴̧̢̛̛̛̛̝͍͕̗̪̲̥̳̤̤͖̤̣̝̦̘͉̮̟̝͕͍̱̠̯͐̇͒̀̓͌̑̀͌̅̉͊́͗̈́̍̉̄̈̑̐̒͒̋̒͌͒̈́̈́̽̏̈́̅̓̀͂̌̚̚͝�̶̧̧̨̫̤̼̮̼̫̜̹̖͔̪̰̣͕͓̇͆̾̓͌͂̍̊̾̆̓́̋͐͜͜͜͠ͅ�̷̢̧̢̠̯̯̥̯͙̳̰̲͚̣̘͓̰͕͚̠̦̪͓̖̥̭̘͔̰̮̫̩̪̞̣̺̙̘̗̥͔̪̺̯̼̲̻͙̟̈́̋̈̃̈́̈́͋́̈́͊̒̌̚͘̚͜�̵̡̨̥̥̘̖̱̺̗͉̩̮̞̳͍̜͕̘̻̻̦͍̭̃̅̈́̅̿̓̈́̈́̃̌̋̾̓̋̿̐̒͆͆̐͜͠͠͝�̸̛̛̟̖͕̠̮̱̹̖̦̱̦͎̊̌͂̈̎̄̔̐͜͠ ̷̢̛͎̤͙̻̭̼̟̗̳͚͍̝̼̻̩͇̯͙̣̥̺̣̼̯̦̯͚̻͔̻̤̩̱̻̹͖̘̳̫̹̩̟̊̂̎̐̓̈̆̄̓̐͑́̍̇̔̓͐͑͗͊͂̊̿͆̇͂̾͛̈̉̿͛̀̇̅̈͆͘͘̚͘̚̕͜͝͝͝ͅͅͅͅ�̴̨̢̧̛͚̱̩͔̮͖̞̺̬̖̳̻͖̜̥̭̼̙̬̼̖͇̄̏̊͌̉͌̇͋͂̈́̔̀͆͒͐̽͐͂̍̉̐̓̔̀͗̿̐̊̈́̊͝͝�̴̧̧̡̨̧̟̱̘͚̬̬̬͙̘̤͇̣̗̥̫̣̬͙̻̻̱̟̟̳̜̞͖̩̱͇̺̯̗͙͇̤̼̯̦͙͊̊̈̿͐̇̑̆́͌̕̚͜͜͠�̵̱̩̼͉͍̙̤͔̤̟̤̺͇̖͉̱̆̐̀̿̏̿͛̾̽̒́̊̌́͒̂̇͌̑͐͐͋̓̾̋̄̀̈͋̐̃̕̕͜͠�̶̡̨̢̧̨̧̧̨̡̛̻͚̮̻̟̜͔̘̳̳̦̗͓̣̳̗͙̼̜̠͈̲̹̘̤͍͔͂͂̌̄̾́̈́͗͑̀͒̌̒̍̈́̍̄͋̈́̊͛̃̓͒̂́̾͌̎̊͐̍̕͘͘͜ ̸̢̛̛̲͕͈͖̙̱̦̝̘̫̘̊̐͑̔̓̅̃̾́̀͊̾̈́̓͋͐͘̕̕ͅ�̶̨̡̧̛̛̝͕̘͓͕̮̗̯͖̻̥̗̻̣̣͉͙̼̞͔͔̠̹̭͉̙͗͊̐́͑͋̅́̆́͂̍͗̆̏̂̊̌̍̑̐̃̏̅̏͌͑̈́̐͋́͋̀̀̔̈́̀̌͘͘̕͜͠͠͝͝ͅ�̴̨̡̡̨͙̪͕͍̹̬̩̰͈̙̖͕͇̼̳̮̬̠̮̣͖̳̖̈͐͊̏́̑̆͜�̷̢̢̡̛͉͉̩͎͎̘̩̝̪͙̪̖̖̻̠͓̯̫̩̜͚̝͉̰̬̥̲͎̺͈̩̲̭͚͙̩̮̺̘̦̰̹̖͚̍̈́̌̂̔̾͌͆̓̑͌͒̂̎̋̀̍̅̍̇͜͝͝�̷̨̧͖̦̘̘̹̞̳͚̰̯̪̓̉̾̂̑̀̀̂̕͜ͅ�̷̡̢͙͎̫̖͕͉̺͍̪̩̦̬̞͓͚̥̬̗̭̣̟͓̖̞͔͎̠͇͎̜͎̱͔͉̱͓͈̳͚̤̘̝̬̱̠̬͙̗̅̈͋̊̋͑̋̽̉̔̎̏̀̈́́̉͗̊̚̚͝�̴̨̡̧̧̧̛̛̗͚̘̟͍̞̪̖̖̘̳̳͍̠̲̬̺̖̺͎̜̳͔̬̱̰̱̭̭̃͊́̿̋̇̀͐͒̓̃̿̉̅̀͗̿̃̉͑̊̾̈́͂́͂̈̇̌̀̍̉̅͘̕̕͜͜͝͠�̵̡̡̡̨̧̨̳͉͈̮̮͓̤͔̞̺̠͔̲͚̩̟̖͈͈͎̮̘̖̰̺̠̼͓̥͙̘̺̥̠̯̮͈͚̫̳͈͂̽̆̂̈́͐̄̈́́͋͒̓̈́̃͊͗̕͜͠ͅͅ�̷̡̡͎̠̞̪͉̠̝̻̞͈͎͍̣͔̦̤̺̩̟̳̠̌̈́̆̐͌̊̀͊͂̍̃̃̈́̍͗̓̃̿͌̀̔̾͑͛́̆͘͝�̵̧͇̲̟͔͔̾͋̓͑̕̚̕̚͝�̷̧̢̢̨̢̙̺̟͚̣̘̻̙̩̤̺̳̫̻͉̙͈̪̩̤̤̬̘̖̦̠̞͔̺̜̱̞͕̣̤̩̤̭̻̺̣̮͌̋͗̈́̂̀̅̆͂͂̃͗̐̐̒͋̒̆́̊̂̄͐̓̈́̏̉͒̉̔̕͜ͅ ̶̧̨̢̡̡̨̛̥̜̼͈̮̰̜̝̪̪̹̖̫̗̘͔̮͇͔͕͗̀̒̇̄̍͆͒̈́͆̂̍̄̒̕�̵̧̧̛̫̝̻̭̳͙͇̺̯̖̻͔̱̮͈̪͈͖͖̦̮̤̜̑̿̈̽͂̂̏̌̌̒̓͒̔̕͠ͅ�̵̛̛̛̛̤̃̑̓̔̍̍̈̐̔͛́̑̏̓̄̉̀͂̈́̉̽̏̆̎̄̇̿̐͂̇̈̀́͊͐͑̚̕͘̕͘͠͝�̷̢̡̳͔̭͈̖͉̭̝͉̭͈̪͍̘̹̳̱͔̾̓̌̇͗̈́̂̋̄̐̿̀̎̑͒̈̌̽͊̌͆̎́͗͘̚͘̕�̸̢̛̛͖͖͇͉̯̰́̌͗̈́̀͒͌̽̈́͛̀͂͊͋̐̐̃̊̀͛͆̓̈́́͗͆͊͐̆̈̓̊͒͘͘�̷̣̬̠̹̥̮̳̟̗͎͎̥̣̯̦̝̩̝̰͎͈͖̭͍̼̯̞͎͍̩͙̦̹̺̟͇̗͍̥̿͌̋͒̆̈́̊͂̄̆̕͝ͅ�̵̡̜̖̺͓̣͔͉͙̖̗̺͔̙͓͖̱̤̱͓̜̲̭̫͎̮͖͎̥̻̝̘̯̦͕̟̣̫̟͖̹̊̓͛̃̈́̆̔̑̇̎̆̄̀̀̃͘͜ͅͅ�̷̨̣̒̂̒̓͛̉̊̓̿̽͗̓͆̈͑̑̈́̓̓̑̔͑̿̈́̐̈́̎̒̇̂͌̋̎̓́̽̅̕̕͠͠�̷̛̦̥̆̉́͒̕͠�̶̨̨̢͎͓̣̺̗̘̳͎̳͎̘͎̹̥͙̪̦̟̰̼̩̹̳̍͂̂͌͗͗̋̕͜ͅ�̸̢̡̢̧̛̺̳͕̲͎̼̮͓͙̙͈̩̠̪̫̟̠͇̺̲̪͇̠͖̩̣̩̘̱̻̬̮͖̳͍̟̖͍̜̥͕̆̓̈́̌̄̃̀̋̐͗̂͛̈́̔̆͋̊̍͆͘͘̚͝ ̵̨̢̧̟̩͉̯̪̮̟̝̺̘̯͍̹̯̫̼̳̗̖͖̼̤̜̙̉͑́͐͒̏͗̍̊͆̐̐̉̈̉̿̑͛͋̒̓͊̆̊̚͜͠ͅ�̷̹̭̰͇̼̹̖̹̮͕̳̠͙̤̠̣̖̤̜̳̬͓̣̥̟̲̩̰̩̘͚̪̩̆͆͒͆̈́͛͌̄̓̅̂̽̑̊̽͗̆̓̑͊͂̃͆́͘̕͜͠͝ͅͅ�̷̼̻͈͖͖͕̘̝͔͓͈̩̝͖̽̀́̉̃̓̍͒͂͆͊̃̽̌̽̚͘͝͝ͅ�̸̡̨̧̡̡̯̩̥͙̪̮̥̮̞̝͎̜͓͍̩̘͈̘̻͔̘̞̥͚̮̳̜̊̀̈̌̇̉̂̎̔̑͑̑̀̋̔̈́́̑͋̄̑͆̓̾̽̐̉͆̍̒͒͂̀͘̚̕͘͘̚͠͝͝͠ͅ�̷̨̢̠͎̯̜̙̣̝̜͎̦̖͖͖̾̿͋͛̿̓͑́̿͒̿͑͂̎̈̈̾̔́̆͝͝ ̶͙̖̘̼̮̳̘͍̳̗͉̟͙͎͓͙̦̮̮̹̓͂̒̐̄̄̓͐͆̔̽̓̏͂̍̿̔̏̄͋͋̚͘̕͠͠͝!",
   "c̴͚̣͙̺̻̤̬̠͙͚̫̫͊̓̇h̵̢͈̦̭̝̯̀̇̆̅̍͑̄͘ú̷̢̱̪̖̗̦̺̯̱͈͉͗̅͘͘͜͜n̷̝̤̠͇̩̦̞̊͋́̇̆̋͗́̀̎̈͜͝͠ģ̸̞̙̙͔̹̹͇̙͖̜͇̱͜͠ ̷̨̡̡̜͍͍̣̟͚͍̲͈̐͗̓̅̿́͋͜͠m̷͎̼̙̹͍̻̯̓͛̅̓̾̆̈̈ä̴̧̧̞̳̖͉̭́̌̿͘͠y̵̧̡̡̼̫͔͓̝̪̩̙̭̐ ̵̧̢̢̝̠̞̼̘̝͕̬̩̇̑̔͛̏t̸͇̼̞͚͉̩̦͚̖̣̗͔̙̋͜ů̵̠̤ơ̵̡̝̺͉̠͉̬̣͈̍̑̓͌̾̾͗́̿́͝ͅi̵̧͍̺̲̻͚͖͈̥̜̫̗̫̭̊͒ ̷̛͚̦̻͚͑̋̑͑̀̔̐̚͘͝l̸̛͇̣̤̽͋̇̿́̌͝͝ȏ̸̡̧̢̫̬̭͖̜̰͖̱̦̠͛͋͐̔̈́̊́͆͘͜n̴̳̤͚̤̬͋̊̀̃",
   "m̴̛͖̼̏̌͂̈̽͛́̉͌̒̊̆̕̚a̸̢̡̱͈̞̠̬̞͉̞̮̅ỷ̶̮͈̥͍̳͇̫̹͎̠͋̆͗̍̿̎͋̃͗̾́̒͝͝ͅ ̷̢̜̰͙͎͚̯͐͐̎n̸̢̡̛̬̩̪̗̠̱̮̦͜ͅģ̴̮͓̖̇̋̾̀h̸̗̝̘͎̤͙̻̒̏́̑̒̍̍̔̈͆̕̕͠i̵̲̣̠̩̭̖̙͎̣̖͉̝̾̌̈́̔͑̃̑͘͠ ̶̞̞̞̣̝͉̬̟̲̬̙͋͠m̵̛̬̲̫̝͚̈́͒͑͆̏͛͊͌̊͑͘͝â̸̭̠͓͇̻̖̼̙̖̌̂ͅŷ̸̛̛̤̮̩͊̀̎́̂̉͛̇̆̊̿̕ ̶̳̜͚̹͈̘͈̬͑̀͒͛̈́̽̍̚͝͝g̵̤̟̮̮̹̭̗̠͌i̶̧̞͕̦̝͍̤̻̤̦̫̙̯͓͐̽͋͜͠͝o̸̭̭͊͘̕͜i̸̥͓̠̝͐͛͂͆̏͂̄͆̇̏͐̕ ̵̡͙͚̱̠̿̄͝ą̷̬̝̭̖̣͕̰̠͓̩̎̈́͒̀̎̎̑̕͝͝͝",
   "t̶̛̛̝̘͈͔̜̜̺̃́̀̑̏͆̾̈́̃̌́̈́̕a̶̢̡̛̜͇̬͇͎̭̖̰̼͓̜̖̓͂̏͂͂̈́̄̐͝͠͠o̴̲̓͑̈́̇ ̸̛͈̪̱̀̊̏̔͐͆͆͐͐̇̈̒͋̚d̴̲͚̪̰̥̳̖̳̠̠̭̺̪̓̽̾a̴̗͍̫͒͂͐͂̉̓̓͐̍̽̊̇̀͘̕n̴̨̧̛̗͔̮͍͙̫̠̗̬̑͗̌̂̊̊͐͐̊̊̄͌͘͜͝g̵̢̗̪̬͕͇̑͆̀͌̓ ̵̰̞̖̺̼̝̹̃̔̊̊̑̿̔̈́̔͗͝͝͝c̷̨͇̘͓͕̿͗́̅̓͘ͅã̴̧̧̡͉̖͈̗͈͔͚͙̦͌̃̒̐͒̕p̶̼͔̼͕̪̿͆͋̓̾͑̍̌̅̇́ ̴̡̧̡͓̤̮̥͍̱̱͔̥̦̈͜h̶̛̥̄̒̆̇͗̓̆̕͝͝o̷̡̒͛̿n̶̡̹̻͉͍̙͖͈̠̳͚̎̓̇̈́̌́͝ ̶̱͔̠̜̘̀̿̈́̾̈́́̊̑̆̚͘m̷̢̰̲̥̮̤̖̼̲̖̺̘̺͋̅͋̈́̓̾͊̏͌̒̿a̷̡̭̥̹̥̦̠̱͈̮͚̫̲̺̲͒̽ỹ̸̧̲͈̦̙͓̥̅̓̆̈̒̏ͅ",
   "ḿ̷̘͔̗̙̝̺̮̯̣́͑͑͜á̵̧̧͎͚̰̺̱͎̙̠͇͈͈̠͍͋̇̐̆̇̔̕ẙ̶̧̰̣̰͖̲̩̘̩͈̼̇ ̵̨̡͉̗̤̪̜̙̣́̃̈́͛̓̍̉̂̎͘͜n̵̨̹̱̣͇͉̪͇̼͕̞̗͚̂̽́n̷̡̬̳̱̗͈͖̬̉̿̀̋͗̓̓̊g̷̡̡̩͈̥̬̼̲̞̱͖͚̝͉̓̆̏̊̈́̋͂̉̕u̷͇̞͚͕̐͑͘ ̸͋̈͋̎̆͊́̂͘̕͝ͅṉ̷͚̝̥̬̹̙̦̜͚͇͔̥̹̣̀͂͒̒̉̓̽̓̚͘̕͘͝h̴͔̤̓͝͠ư̷̤̺͇̻̓̓͌ ̷̧͈̗̯̤͔̗̰͇̳̩̮̲̓͑̍̒̌̽͒̇͋̚̕1̸̮͈̺̞͕̙͉͖̚ͅ ̴̡̢͎̯̳̤̖̟̬͙̻̎̊̆̒̌c̶͉̪̰̯̼̺͙͍̦̐͂ö̸̘̱̝̮̈̄͌̓͘͝n̵̢̜̜̱͖̩̬̹͖̼̥͈͉̱̍̎͑͐̏̉̔̓̅̑͝͝ ̸̠͕̖̂̓̃̎̌͝ͅc̷̥̱̘̮̪̜̯̫̱͓̟̪̜̈́̾̚ͅḩ̸̡̘̗̝̻͚̭͉͛̑̊̀͋̈͌͗̇͠o̶͍̯͉͕̪̙͖̪̗̖̮͇̭͈̅̏̑̈́̾͐̽̕͜",
   "g̴̺̼͕̭̤̲̖̞̺̤͌̒̃̑̈́̓͗̌̎i̷͚̘̮͚̹̞͗̋͒͊͜ọ̵̥̟̬̬͙̟̦͖̻̫̙̏̓̒́͒͊͘͘i̸̧̟̻̭̙̩̞̺͌̇̈́̆̋͗̔ͅ ̷̮͉̤̻̓͐̽̀͂͋̈̚͜͜t̷̡̖͇̝̳̪͎͍̻̞͆h̵̨̪̪͈̦͚͖̜̮̬̮̹̫̟̹͐̾̀̍̌̀̚͝i̴̧̺̞̲̠̤͈͕͓͖̙̙̼͈̊́̅̒͊͑ͅ ̴̹͚̈̈́̿̀̆̊̔̆͠͠ͅä̷̛̤̱̲́̓̓̂̾͐̀̓͝n̶̞̥͍̞̗͕̫̂͌̑̍̏͋͐͒̆͛͋̃͊̕͝ ̵̖͈͍͇̍̽̆͆̎̂̅͊̒̉ẗ̵̛̥̫̯͍͎̲̩͓͉̤̲͈͚̮͛̀̊̔͋́̚͜a̴̧̨̻̯͇̖̐̈͐̔̃̃̎͆̽̉̉͘̕͠ò̶̧͈̭̫̘̰̺̯̝̞͚̘͉͎̇͛̿̚͠͝ ̷̛̺̬̥͇̱̈́̏̅̓͗̌́͑̄̚̚̚d̶̛̦͕̊i̸̫̓̊̏̕",
   "m̷̨͓̱͖̗̗͕͎̲̹̎̑͂͘ͅą̶͖̻̺̘̣̱̝̮̗̜͕̤̲̩̀͗͂͊͊͝͝y̷̡̛̺͉͕̠͙̤̮͗̄͛̋̑͑̈̄̒̉̿ͅ ̸̝̩͊̽ͅŝ̸͇̲͙̥͉͍̣̼̺͙̪͇̬̰͌̈́́͝ò̴̰͇̳͔̲͔̝̽͋͑̈́͋͘ͅ ̵̭̤̜͑̌͋͗͑͘͝t̶̢̘̬̼̫̝̼̜̩͓̙͗̈́̈̈́͊͋̿̚̚͜͝å̸̠̜͚̲̣̃̈́̽̈́̓͛͝ǫ̴͎̣͓̲̟̗̼̲̾̈́͜͠ ̶̜͚͓̠̖̭̅̈̂̎̑ͅa̷̢̋̀̀͘",
   "chung may tuoi lon",
   "me may tuyet voi lam",
   "may gioi thi nuot tao di",
   "tao chap ca ho nha may",
   "cay khong con",
   "chui tao di",
   "may cay a",
   "dit me may luon",
   "an thang bo may di",
   "du con me may",
   "t̸̢̡̧͙͖͎̗̱̳̘͉͍̱̠̠̝͖̰̲̠̦̤͖̘̦̬̞̟̟͙͇̻̓̈̎̿̿̇̍̇͌̐̈̂̋ḩ̴̢̦͙͚̫͈̩͍̜̱̗̘̫̩̪̩̩͈̣̩̺̼̰̲͕̈̃̾̔̿͋͋͑̔͋̄̏͌̃́͛͐̐͆͆͛̎̋́͂̾̾̆̋̽́̓͛̀̈̐̌͗̋͛̿͂͘͘ą̶̨̨̪̹̬̰̣̝̙̠̘̞͕̥̱̬̠̺͒͋̏ͅn̸̛̰̬̩̖̺̬͕̞̥̔̈̄͑̈́͒͑͋̄̿̍̈́́̒̒͗͝͝ġ̶̤̩̥̳̭͎͓̙̳͉̱̼́̇͑̅͋̎̽̇̂̒̓̔̎͂͛̄̏͌̀ ̵̡̡̧̢̺̻͈̱̼̯̖͈̙͈͙͎̪̮͍̻̦̣͎̗̲͎̺͙̼̱̲̮̫̘̜̜̞̰̈́̿͒̿́̓͂̋͜͝͝͝͠b̶̡̢̛̫͈̤̰̬͚̻͎̰̯͇͉̥͈̘̟̟̤̠̪̮̤͎̙̤̞͈̖̱̤̳̆̽̀͌̿̌̀́͊̔͊̈̒̉̃̓͗͒̄̍͋̉̃͌̂̉̃͑͘̕͘͠͝͝ö̵̧̡̯̼̻͙̜͇̹̝̠̠̰̜̣͔̝̙͔͓̺̥͙̟̝̝͖̹̻̮̰͖̥̤́́̉͛̒͛̊̎͗͆̆̏̆̈́̓̿̾͗̐͊̈́̋͗̚͜͠ͅͅ ̵̡̨̧͕̖͇̻̤̰̺̘̜͓̣͍̗̦͔̮̪̼͚͔̰̪͔͍̠̼̠̻̳͔̳͖͇̝͔̹̭̮͕̱̮̩̦́̃̈́͆̽͆̏̿̌̍̇̏̀̎͑̌̇̋͒͒̀̍͘͘m̴̡̢̡̛̰̥̱̭̺̤͓̠͎̥͎̣͖̼̞̬̳͈̙̺͍̘̪͙̈́̇̃̈́̏̓̐̾̀̑̽̇̾̿́̊̀̿́͌̿͊̍͘̕͜͝͝ͅͅá̸̡̧̨̢̨͙̬̻̰̘̤̟̲̖̘̞͚͓̮͇͈̠̮͖̞̺̹̖̬̣̐͐͋̈́́̉͛̕̕ͅȳ̶̢̨̬͓̫̝̣̗̦̫̘͙̳͓̺͎̣͙̻̤̝̻̲͙͎̱͈͕̟̤̣̲̝̳̊̓͛̽͆͜ͅ ̴̢̧̡̢̢̭̣̳̪͍͔̙̤̜̭̯̞̮̹͖͕̠̗̲͚̼̬̳̦̠̗͙̫͖̞̬̟͇̝͉̑̍̐̄̕͜͝n̴̢̛̛͚̘̼̖̘̪̬͎̺̭̺͈͉̳̫͙̭̥̙̙͓̹͍͕͚̜̻͙̩̹̲̋͊̏͊̀̔̅̒ȩ̶͍̯̣̼̞̮̘̫̻͍̤̹͎̥͎̮̣̞̺̭̟͙̹̳̩̥͋̊͐̑͛͊͂̓̓̀̓̾̾̅̿̒̿́̏̂̽̉̆͋͗͘͘͠͝͠",
   "d̴̢̡̧̢̧̛̪̟̘̟̗͓̙̻͔̝͍̰̺̼̘͚͕̭͕͕̖̦͇͚̟̗̮̫͍͓̗̹̻͇͓̼̫͙̓́̄̽̋͋̈́̾̐̀̃͋́̽̎͐̃̇͊̅̎̽͒͝͝͠i̷̢̢̡̢̛̦̜͎͈͕̬̟̳͍̝̻̤̭̙̳̘̱͕̼͓͚̻͍̲̺̬̥̪̞̺̥̼̲̘̹̞͇̺͍̘̲̘͎̖͚̦̠͎̺͈̜͈̺͔̲̱̜̘͔͖̒̅̀̎͑̊̋͒̽̎̀̐̐̀̀̌̂͐̓̒̏̈̀́̃̎̓̈̾̒̏̎́̄̐̕͘̕̕͜͠͠͝͠t̵̢̨̡̨̨̨̨̛̛̛̩̝̞̮̝̣̦̘͍̟̳̥̰͍̱͎̘̜̥̜̭̦̖̭̣̰͍̗͕̟͇̞̳͙̮͔̗̠͙̠̘͙̗̩̱͇̲̻͇̟̤͓̩̲̻̬̣̓͐̌̈́̅͌̉̐̀̏̈͛̉́̀͒̄͊̏͐̃̎͊̈̾̅̅̃͐̋̀̏̊̏̈́̑́̿̃̈́͊̅͆̂͊́͊̈́͆̾̇̇̔̆̀͊̾́̋̒̈́͗̊͂͂͂̒̑̍͗̃́͗͒͑͂͊͐͗͆́̃̃̃̾͊͋̈̇̕̚̕̕̚͘̚͘̚͜͜͜͜͠͠͝͝͠ͅ ̷̢̢̢̢̡̡̡̛̛̛̮͍̝̻̪̫͙̲̹̪̞͇̱̜̬͍͍̘̬̻͎̰͖̠̻̰͈̺̣̬̖̖̥̥̼̥̩͙̻̗̬̯͉͕̟̰̙̳͙̻͈̝̪̪̬̬͇͈̯̮̩̫̐̊̌̓̋̋͌̽̈́͋̎̉̂͊͛̑̋̿̍̋̾͆̍̂̉̌͆̑̄͂͂̇͆͋̄̓̐̌̆͋̎̀̎̍̒̎̆͐̂͆͑̈́͌̿̌͆̍̒͌͋̄͂̓͐͐͌̀́̈̓̈́̈̈́̅̏͋̀̊̍̽̕͘̚͘̕͜͜͜͠͠͝͝͝͝͠ͅͅͅb̶̧̨̨̧̨̨̛͔̝̬̲͙̗͕̟͙̥̰̪͔̣̪̥̞͚̜͈̯̼͔͎̠̟̳̠̰̰̹͖̲͇̝͙̥̖̭̿̋̏́͗͋͂̋̀̄̓̈͗͑̂̍̅̓̿̓͗̈́̊̾͝͝ͅā̸̡̧̧̨̡̡̢̢̛̛̫̗̞̭̬̤̭̣̮̦͕̺̼̰̫̪͉̦̠̺̖͖͙̳̠͔̗̱͇͉̠̘͙̙̣̫̣̮̭̠̲̮̘̪̟̞̱̯̫͉̳̝̥̘͎̣̰̖͇͓͚̫̦̱̙̤̻̠͎̻̬͓̞͍̱͙̬̠͙͇̭͔̼̩̩̯͍̤̳͚̫̙̙̲̭̗͙͚͔̞͚̪̟͓̺̣͈̟͔̦̅̎̄̑̔̂̉͛̂͆̉̑͌͒̂̎͂̓͋̾͑̄͐͛̃̄͆͌̊͛̀̉̒̂͊̉̀͐͑̾̑̆́́̂̄̂̎̐̐͋͐̇̈̍̀̈́̾̔̈̂̀̿́̑͑̎͆̎̆͊͑̕̚̚̚̕̕̕͜͜͜͠͝͠͝͝ͅͅ ̷̧̡̧̨̧̡̧̧̢̡̨̢̨̧̡̬͇̥̙̥̟͚̩̩̫̗͔̻̣̭̯̣̜̟̜̺͕͉̣̪̻̘̝͍̭̳̥̘͔̻͕̤̺͍͕̭̫͍̦̯̩̲̱͉̪͓̘͓̬̺̗͇͙̯͖̱̬̹͈̱̦͔̘̙̠̪̣̲̲̳̲̹̻͚̹̘͈̹̬͖͇͖̖͙̹̟̗̹͎̜̟̜̫̳̱͔̪͍̦̜̘̫̻͇̅̒̆̍͋̎̓͊̈́̂̌͋͐̊͛̕͜͜͠ͅͅͅm̵̢̢̨̢̳͇͕̳̦̯͙̥̻̼̰͓̤̱̪̳̮̥̥̰̗̭̳͇͖̫̭̩̣̯̥̟̼̞̤̫͖͓̺̖̬̻̭̦̫̠̤̦͈̙̙͔̫̮̜̺̩̌̉͌̄́͌̽̌͗̊͆̊̐͌̍̅͑͛͐̾͒̓͛̿̓͆͛̉̓͗̓̈̿̒̕̚͜͠͝ͅá̷̧̧̡̡̧̡̢̨̡̢̡̨̡̧̧̡̛̜̱̺̲̤̩̞͔̖̖͉̘̗̦͙̙̠̳̰͍̟͍͔̥̙̗̬̝̭̠͈̝̝̹̼̞̖͖̥͖͎̰̩̣̹͚͎̯͍͇̤͓̯̟̹͕͔̼͇͚͖̗̙͖̪̤̗̬̙͓̘̮̫̝̻̖̤̗̯̺̝̠͈̬̞̻̫̩͎̳͇̜̠̮͙̞̮̬̦̳̣͚̣͕̜͕̮͔̞͎̪̰̎̈́͛̆́̉̿̉̊̏̋͐́̾̓͆́̓͌͌͗̈̐̈́̆̌̅͋̓͋͗̀̐̀́͒̇̋̀̇̀͗̒̄̾̏̈́̉̉̍̅͆̑͊̾̿͌͌́̓̚͘̚͘̚͝͝ͅͅÿ̸̧̨̢̨̛̛̛̜̠̩̟̖̦͇̮̥͓͈̗͔̣̹̫̠̙̫̖̪͎̪͖̙̮͕̜̭̗͉̖̺̬̹͔̣̙̫̖̱̗̠̰̪͚̣̟̙͓̖̘̜͚̞̼̺͉͔̫̘͍͚̬̰͍̱̲̝̬̣̮̭͈̻̯̲̜̫͉͚̮̙͖̝͔̙̬͇̃́̂͒̄̂͐̃̔̄̇̀̍̑̔͋͗̂̽͑̅͐̋̿͊̄̀̈̍̅̇̇͑͐͐̏̋̓̈͊̉͑̄̈̾̓̌̇̋̓̐͛̏̾̊̀̿͗̇̐͑͗̍́͒̽̂͐̊͂̈́̄͒͋̑̈́̇̒̐̔̀̿͑͛͐͂̓̕̕̕̚̚̕̚̚̕͘͜͜͝͝͠͝͠͠͝͝",
   "an tao di",
   "chui bo may di",

]


while True:
    
    message = random.choice(messages)
    pyperclip.copy(message)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.01)
    pyautogui.press('enter')
    time.sleep(0.02)
    if keyboard.is_pressed('q'):
        print("Đã dừng gửi tin nhắn.")
        break

print("Kết thúc chương trình.")
