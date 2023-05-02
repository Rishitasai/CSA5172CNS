def encrypt_text(plaintext,k):
    ans= ""
    for i in range(len(plaintext)):
        ch = plaintext[i]
        if ch==" ":
            ans+=" "
        elif (ch.isupper()):
            ans += chr((ord(ch) + k-65)% 26+65)
        else:
            ans +=chr((ord(ch) + k-97)% 26 + 97)
    return ans
plaintext = "abcdefghijklmopqrstuvwxyz"
k=6
print("plain text is:"+plaintext)
print("key:"+str(k))
print("cipher text is:"+ encrypt_text(plaintext,k))
