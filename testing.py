import sqlite3
import random
import json

con = sqlite3.connect("testrun.db")

cur = con.cursor()
#cur.execute("CREATE TABLE test1 (Username VARCHAR(225) NOT NULL, Emails VARCHAR(225), Pwd VARCHAR(225), docs VARCHAR);")
#d = str({"med1": "[doc1, desc1, time1]","med1": "[doc1, desc1, time1]"})
#cur.execute('INSERT INTO test1 (Username, Emails, Pwd, docs) VALUES ("testuser", "testuser@gmail.com", "testpswd", ?);', (d,))
#con.commit()

def inputVals(Doc,Med,User):
    cur.execute("SELECT docs FROM test1 WHERE Username == ?", (User,))
    docsl = cur.fetchall()
    docsstr = docsl[0][0]
    docs_extr = dict(eval(docsstr))
    docs_extr[Med]=Doc
    docspkg = str(docs_extr)
    cur.execute("UPDATE test1 SET docs = ? WHERE Username == ?", (docspkg, User))
    print("Value Added!")
    con.commit()
def outputVals(User, Med):
    cur.execute("SELECT docs FROM test1 WHERE Username == ?", (User,))
    docsl = cur.fetchall()
    docsstr = docsl[0][0]
    docs_extr = dict(eval(docsstr))
    x = docs_extr.get(Med)
    return x
def randomMedGen(User):
    l1=[]
    cur.execute("SELECT docs FROM test1 WHERE Username == ?", (User,))
    docsl = cur.fetchall()
    docsstr = docsl[0][0]
    docs_extr = dict(eval(docsstr))
    for key in docs_extr:
        l1.append(key)
    print(l1)
    length = len(l1)
    try: 
        x = random.randint(0,length-1)
        chosenVal = l1[x]
        return chosenVal
    except:
        return "Medicine"

def create(name, password, email):
    d = {}
    ds = str(d)
    cur.execute("INSERT INTO test1 (Username, Emails, Pwd, docs) VALUES (?, ?, ?, ?)", (name, email, password, ds,))
    con.commit()
    print("Value added: ",name," ",email)
    with open("userfiles.json", "r") as jsonFile:
        data = json.load(jsonFile)
    data["username"] = name
    with open("userfiles.json", "w") as jsonFile:
        json.dump(data, jsonFile)

def checking(name, password):
    cur.execute("SELECT EXISTS(SELECT 1 FROM test1 WHERE username=:name LIMIT 1)", {"name": name})
    record = cur.fetchone()
    if record[0]:
        with open("userfiles.json", "r") as jsonFile:
            data = json.load(jsonFile)
        data["username"] = name
        with open("userfiles.json", "w") as jsonFile:
            json.dump(data, jsonFile)
        return True
    else:
        return False

def checkpswd(name, pswd):
    cur.execute("SELECT pwd FROM test1 WHERE username = ?", (name,))
    l = cur.fetchall()
    password = l[0][0]
    if pswd == password:
        return True
    else:
        return False

def reqemail(name):
    cur.execute("SELECT Emails FROM test1 WHERE username = ?", (name,))
    l = cur.fetchall()
    email = l[0][0]
    return email

def getmedlist(User):
    l1=[]
    cur.execute("SELECT docs FROM test1 WHERE Username == ?", (User,))
    docsl = cur.fetchall()
    docsstr = docsl[0][0]
    docs_extr = dict(eval(docsstr))
    for key in docs_extr:
        l1.append(key)
    print(l1)
    return l1

checkpswd("testuser", "testpswd")

#checking("testuserfrfrfr", "hello")

#cur.execute("SELECT * FROM test1")
#print(cur.fetchall())