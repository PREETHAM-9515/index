
import random
compwins=0
playerwins=0
def choose_option():
    userchoice=input("choose rock,paper,sissors: ")
    if userchoice in ["rock","Rock","r","R"]:
        userchoice="r"
    elif userchoice in ["paper","Paper","p","P"]:
        userchoice="p"
    elif userchoice in ["scissors","s","S","Scissors"]:
        userchoice="s"
    else:
        print("try again, you stupid.")
        choose()
    return userchoice
def comp_option():
    compchoice=random.randint(1,3)
    if compchoice==1:
        compchoice="r"
    elif compchoice==2:
        compchoice="p"
    else:
        compchoice="s"
        return compchoice
while True:
    print("")
    userchoice=choose_option()
    compchoice=comp_option()
    print("")

    if userchoice=="r":
        if compchoice=="r":
            print("you and computer choose same. you tied")
        elif compchoice=="p":
            print("you choose rock and computer choose paper.loseer")
            compwins+=1
        elif compchoice=="s":
            print("you choose rock and the computer choose scissors.winner winner chiken dinner")
            playerwins+=1
    elif userchoice=="p":
        if compchoice=="r":
            print("you choose paper.computer choose rock.winner winner chiken dinner")
            playerwins+=1
        elif compchoice=="p":
            print("you choose paper. the computer choose paper.you tied")
        elif compchoice=="s":
            print("you chose scissor compuetr chose paper. loseer")
            compwins+=1
    elif userchoice=="s":
        if compchoice=="r":
            print("you chose scissor computer choose rock . losser")
            compwins+=1
        elif compchoice=="p":
            print("you choose scissor computer choose paper.winner winner dinner")
            playerwins+=1
        elif compchoice=="s":
            print("you choice scissor computer choose scissor.you tied")

    print("")
    print("player wins: "+str(playerwins))
    print("computer wins: "+str(compwins))
    print("")

    userchoice=input("do you want to play? (y/n)")
    if userchoice in ["Y","yes","yes","y"]:
        pass
    elif userchoice in ["n","N","no","No"]:
        break
