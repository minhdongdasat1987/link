import os
import sys
import subprocess
import argparse

def check_interface(interface):
    print(f"[+] Kiểm tra giao diện mạng: {interface}")
    result = subprocess.run(["ip", "link", "show", interface], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[!] Không tìm thấy giao diện {interface}")
        sys.exit(1)

def run_oneshot(interface, kill_network_manager=False):
    if kill_network_manager:
        print("[+] Dừng NetworkManager...")
        os.system("sudo systemctl stop NetworkManager")

    print(f"[+] Chạy OneShot trên giao diện {interface}...")
    os.system(f"sudo oneshot -i {interface}")

def main():
    parser = argparse.ArgumentParser(description="WiPwn Launcher (Lite)")
    parser.add_argument("-i", "--interface", type=str, required=True, help="Tên giao diện WiFi (ví dụ: wlan0)")
    parser.add_argument("-K", "--kill-network-manager", action="store_true", help="Tự động tắt NetworkManager")
    args = parser.parse_args()

    check_interface(args.interface)
    run_oneshot(args.interface, args.kill_network_manager)

if __name__ == "__main__":
    main()