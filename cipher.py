def lifeInWeeks(CurrentAge):
    totalTime = (90 * 52)
    passedTime = (int(CurrentAge) * 52)
    timeLeft = totalTime - passedTime
    print(round(timeLeft))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

message_in = input("What message would you like to encrypt? ").lower()
shift_num = int(input("What is your shift number? "))

def encrypt(message, shift):
    encryptedMessage = ""
    for letter in message:
        if letter == " ":
            encryptedMessage += " "
        else:
            shiftedPosition = alphabet.index(letter) + int(shift)
            # This is the best part of the program.  Using modulo cleverly to prevent index error.
            shiftedPosition %= len(alphabet)
            encryptedMessage += alphabet[shiftedPosition]
    print(encryptedMessage)
    return encryptedMessage


def decrypt(message, shift):
    decryptedMessage = ""
    for letter in message:
        if letter == " ":
            decryptedMessage += " "
        else:
            shiftedPosition = alphabet.index(letter) - int(shift)
            shiftedPosition %= len(alphabet)
            decryptedMessage += alphabet[shiftedPosition]

    print(decryptedMessage)
            
outputMessage = encrypt(message_in, shift_num)

decrypt(outputMessage, shift_num)




