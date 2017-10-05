import sys

def create_diamond(letter):
    if(len(letter) != 1):
        print("Too many letters for this here diamond machine. Just use one")
    letter.upper()
    
    lines = []

    # Create top half of diamond
    for i in range(ord('A'), ord(letter) + 1):
        # Create a line padded with enough spaces to center align
        line = ' ' * (ord(letter) - i)
 
        letters = ""
        for j in range(ord('A'), i + 1):
            letters += chr(j)

        # Add reversed string minus last char
        letters = letters + letters[-2::-1]
        line += letters

        lines.append(line)
    
    # Reverse top half of diamond except the longest row and add to lines
    lines += lines[-2::-1]
    return '\n'.join(lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Give me a letter, and I give you a diamond. No freebies! [Needs one 'char' arg]")
        quit()
    print(create_diamond(sys.argv[1]))


