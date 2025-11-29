import hashlib
dic = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for a in dic:
    for b in dic:
        for c in dic:
            for d in dic:
                t =str(a)+str(b)+str(c)+str(d)+'pZxMZTgznPAVn0PHF5ehbaj9vak0'
                m = (hashlib.sha256(t.encode())).hexdigest()
                if m[:64] == 'f9dbbf9b2dedc113996c4a831add5db1114a3097a2a160fdb45055a24ef23784':
                   print(t)
                   break