game={"scissors","paper","rock"}
user=input("enter scissors paper or rock:")
pc=game.pop()
print("pc choice:",pc)
if pc==user:{
    print("match tie")
}
elif (
        (user == 'rock' and pc == 'scissors') or
        (user == 'paper' and pc == 'rock') or
        (user == 'scissors' and pc == 'paper')
    ):
    {
        print("you win")
    }
else:
    {
        print("you losee")
    }