#keyword transposition cipher


def keyword_transposition(keyword):
    letter_number =[]
    #generate unduplicated letter matrix
    letters = list(keyword)
    let =0
    row = int(26/len(keyword))+1
    #print (row)
    keyset = [[0]*len(keyword) for i in range(row)]
    
    keyset[0]=letters
    for i in range(1,row):
        for j in range(len(keyword)):
            #print (i,j,let)
            if let >25:
                keyset[i][j]=0
                continue
            while True:
                if chr(65+let) not in letters:
                    keyset[i][j]=chr(65+let)  
                    let = let +1
                    break
                let = let+1
            
    #matrix transpose
    keyset2 = [[0]*row for i in range(len(keyword))]
    for i in range(len(keyword)):
        for j in range(row):
            keyset2[i][j] = keyset[j][i]
            
    keyset2.sort()        
    keycipher =[]
    for i in keyset2:        
        keycipher = keycipher +i
    keycipher=[i for i in keycipher if i!=0]
    print(keycipher)
    return keycipher

def decipher(keyword,cipher):
    keylist =[]
    result =[]
    keyword_list = list(keyword)
    for i in keyword_list:
        keylist.append(i) if keylist.count(i)==0 else ''
    
    keycipher = keyword_transposition(keylist)
    key_dict = dict()
    for i in range (26):
        key_dict[keycipher[i]]=chr(65+i)
    for i in cipher:
        try:
            result.append(key_dict[i])
        except:
            result.append(i)
    return (''.join(result))

    
n = raw_input()
for i in range(int(n)):
    keyword = raw_input()
    cipher = raw_input()
    print (decipher(keyword,cipher))



