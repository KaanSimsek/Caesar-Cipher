


def main():
    message=input("Enter the message: ")
    key=int(input("Enter a key between 1-26: "))
    print("Encrypted: ",encrypt(message,key))
    print("decrypt: ",decrypt(decrypt(message,key),key))

def encrypt(text,s):
   result = ""
   for i in range(len(text)):
      char = text[i]
      
      #Encrypt uppercase characters
      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
   return result


def decrypt(text,s):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        
        if(char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)

    return result


main()