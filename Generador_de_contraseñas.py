import random


def generate_password ():
    nums = ["0","1","2","3","4","5","6","7","8","9"]
    mins= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    caps= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    spetial = ["@","#","~","€","$","%"]
    characters = nums + mins + caps + spetial

    password = []

    for i in range (15):
        characters_random = random.choice (characters)
        password.append(characters_random)
    
    password = "".join (password)
    return password

def run():
    password= generate_password()
    print ("Here is your new password"+ " : "+ password)
    


if __name__== "__main__":
    run()
