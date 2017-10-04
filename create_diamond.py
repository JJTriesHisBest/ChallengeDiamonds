import sys

def create_diamond(letter):
    if(len(letter) != 1):
        print("Too many letters for this here diamond machine. Just use one")
    letter.upper()
    longest_sequence = ord(letter) - ord('A') + 1
    
    lines = []
    for i in range(ord('A'), ord(letter) + 1):
        line = ' ' * (ord(letter) - i)
        letters = ""
        for j in range(ord('A'), i + 1):
            letters += chr(j)
        letters = letters + letters[-2::-1]
        line += letters
        lines.append(line)
    
    lines += lines[-2::-1]
    return '\n'.join(lines)

if __name__ == "__main__":
    print(create_diamond(sys.argv[1]))


