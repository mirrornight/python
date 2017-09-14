import hashlib, sys

# db = {
    # 'michael': 'e10adc3949ba59abbe56e057f20f883e',
    # 'bob': '878ef96e86145580c38c87f0410ad153',
    # 'alice': '99b1c2188db85afee403b1536010c2c9'
# }

# def calc_md5(password):
    # md5 = hashlib.md5()
    # md5.update(password)
    # return md5.hexdigest()

# def login(user, password):
    # storagemd5 = db[user]
    # return storagemd5 == calc_md5(password)


# username = sys.argv[1]
# password = sys.argv[2]

# print login(username, password)



db = {}
def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')
    

def login(username, password):
    storagemd5 = db[username]
    return storagemd5 == get_md5(password + username + 'the-Salt')

def get_md5(s):
    md5 = hashlib.md5()
    md5.update(s)
    return md5.hexdigest()

if __name__ == '__main__':
    register('michael', '123456')
    register('bob', 'abc999')
    register('alice', 'alice2008')
    print db
    print login('alice', 'alice2008')
