#Eduardo Nunes

def amigas(string1 , string2):
    diferem = 0
    for x in range(len(string1)):
        if string1[x] != string2[x]:
            diferem += 1

    percentagem = diferem/ len(string1)
    if percentagem < 0.1:
        print(f"As palavras {string1} e {string2} são amigas")

    else:
        print(f"As palavras {string1} e {string2} não são amigas")


amigas("alaaaaaaaaaa","alaaaaaaaaao")