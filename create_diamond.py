import sys

def create_diamond(letter):
    if(len(letter) != 1):
        print("Too many letters for this here diamond machine. Just use one")
    letter = letter.upper()
    
    lines = []

    # Create top half of diamond
    letters = ""
    for i in range(ord('A'), ord(letter) + 1):
        # Create a line padded with enough spaces to center align
        line = ' ' * (ord(letter) - i)
 
        letters += chr(i)

        # Add reversed string minus last char
        symmetrical = letters + letters[-2::-1]
        line += symmetrical

        lines.append(line)
    
    # Reverse top half of diamond except the longest row and add to lines
    lines += lines[-2::-1]
    return '\n'.join(lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Give me a letter, and I give you a diamond. No freebies! [Needs one 'char' arg]")
        quit()
    print(create_diamond(sys.argv[1]))


