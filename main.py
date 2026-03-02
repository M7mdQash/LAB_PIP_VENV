from art import * 
from colorama import *

if __name__ == "__main__":
    art1 = art("coffee")
    phrase1 = "BELIEVE AND ACHEIVE" #block
    artPhrase1 = text2art(phrase1, font="block", chr_ignore=True)
    print(Fore.RED + artPhrase1)
    phrase2 = "HELLO" #subzero
    artPhrase2 = text2art(phrase2, font="sub-zero", chr_ignore=True)
    print(Fore.GREEN + artPhrase2)
    
    artPhrase3 = text2art(phrase1, font="sub-zero", chr_ignore=True)
    print(Fore.BLUE + artPhrase3)
    
    tprint(Fore.BLUE+ phrase1,"rnd-large")
    
    phraseCustom = text2art("12 days left", font = "rnd-medium", chr_ignore=True)
    print(Fore.YELLOW + phraseCustom)
    