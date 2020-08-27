import bcrypt
#-----------------------------------#
#            clsecurity             #
#  Secure Password Hashing Library  #
#       Made By Darin Tanner        #
#-----------------------------------#
version = "1_a"
development = False
######################################
def hash(passwd, security): #MUST BE BYTES
    """ Remember to use the same security rounds, or else the results will be different. """
    salt = bcrypt.gensalt(rounds=security) #generate salt
    hashed = bcrypt.hashpw(passwd.encode('utf-8'), salt) #hash it with salt
    return hashed
def comparehash(passwd, hash, security):
    """ Remember to use the same security rounds, or else the results will be different. """
    salt = bcrypt.gensalt(rounds=security) # generate salt
    hashed = bcrypt.hashpw(passwd.encode('utf-8'), salt) #hash it with salt

    if bcrypt.checkpw(passwd.encode('utf-8'), hash):
        return True #Something feels wrong here... oh well
    else:
        return False


passwordtest = 'hello123'
passwordtest2 = 'hello123'
x = hash(passwordtest, 14)

r = comparehash(passwordtest2, x, 14)
print(str(r))