def lifeInWeeks(CurrentAge):
    totalTime = (90 * 52)
    passedTime = (int(CurrentAge) * 52)
    timeLeft = totalTime - passedTime
    print(round(timeLeft))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt():
    # take an input message
    message = input("What message would you like to encrypt? ")
    # take a desired shift number
    shift = int(input("What is your shift number? "))
    # move letters in message by shift number
    encryptedMessage = ""
    for letter in message:
        if letter == " ":
            encryptedMessage = encryptedMessage + " "
        else:
            encryptedMessage = encryptedMessage + alphabet[alphabet.index(letter) + int(shift)]
    print(encryptedMessage)

encrypt()


