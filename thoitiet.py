# (Chỉ là ví dụ ngắn gọn – đoạn này sẽ được thay bằng mã thật trong bước tiếp theo.)
print("=== W8Team ===")
print("Scanning for networks...")
network_list = {
    1: {'BSSID': '00:11:22:33:44:55', 'ESSID': 'MyWiFi', 'Security type': 'WPA2',
        'Level': '-60', 'Device name': 'RalinkAP', 'Model': 'RT2860', 'Model number': 'v1',
        'WPS locked': False},
    2: {'BSSID': '66:77:88:99:AA:BB', 'ESSID': 'Public', 'Security type': 'WPA/WPA2',
        'Level': '-70', 'Device name': 'RalinkAP', 'Model': 'RT2860', 'Model number': 'v1',
        'WPS locked': True}
}
stored = [('00:11:22:33:44:55', 'MyWiFi')]

for n, network in network_list.items():
    number = f"{n})"
    model = '{} {}'.format(network['Model'], network['Model number'])
    essid = network['ESSID']
    line = '{:<4} {:<18} {:<25} {:<8} {:<4} {:<27} {:<}'.format(
        number, network['BSSID'], essid,
        network['Security type'], network['Level'],
        network['Device name'], model
    )
    if (network['BSSID'], essid) in stored:
        line = '[*] ' + line
        print('\033[1;33m' + line + '\033[0m')  # Màu vàng
    elif network['WPS locked']:
        print('\033[1;31m' + line + '\033[0m')  # Màu đỏ
    else:
        print(line)

input("Select target (press Enter to refresh): ")