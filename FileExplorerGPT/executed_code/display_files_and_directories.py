output = """total 328\n-rw-rw-r-- 1 arrogant arrogant 147319 Aug 19 06:13 about-us.html\ndrwxrwxr-x 6 arrogant arrogant   4096 Aug 19 06:13 assets\n-rw-rw-r-- 1 arrogant arrogant      2 Aug 19 06:37 auto-gpt-memory.json\n-rw-rw-r-- 1 arrogant arrogant     22 Aug 19 06:05 file_logger.txt\n-rw-rw-r-- 1 arrogant arrogant 128700 Aug 19 06:14 index.html\n-rw-rw-r-- 1 arrogant arrogant  43273 Aug 19 06:14 single-shop.html\n"""

lines = output.split('\n')
header = f"{'Permissions':<12} {'Owner':<10} {'Size':<10} {'Date':<12} {'Time':<10} {'Name':<20}"
print(header)
for line in lines[1:]:
    if not line:
        continue
    parts = line.split()
    permissions, owner, size, month, day, time, name = parts[0], parts[2], parts[4], parts[5], parts[6], parts[7], parts[8]
    formatted_line = f"{permissions:<12} {owner:<10} {size:<10} {month:<12} {day:<10} {name:<20}"
    print(formatted_line)