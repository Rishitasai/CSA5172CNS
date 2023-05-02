list_1 = "abcdefghijklmnopqrstuvwxyz"
list_2 = "eifjbkpmgnqalhdczorstuvwxy"
plain_text = input()
cipher_text =""
l1 = len(list_1)
l2 = len(list_2)
for i in plain_text:
    for j in range(l1):
        if i == list_1[j]:
            cipher_text += str(list_2[j])
print(cipher_text)
