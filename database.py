from deta import Deta
from getkeys import getdatabasekey
DETA_KEY=getdatabasekey()
deta=Deta(DETA_KEY)
rooms=deta.Base("rooms")


def check_room(roomname):
    print("Chekcing")
    if(rooms.get(roomname)):
        return 404
    else:
        return 100
def create_room(roomname,msgstack):
    rooms.put(key=roomname,data={"val":msgstack},expire_in=3600)

def getallrooms():
    print("Items : ",rooms.fetch().items)

def getmsgstack(roomname):
    return rooms.get(key=roomname)["val"]

create_room("dev",['Dev:Hi','Kirthana:Hello'])
getallrooms()
print(getmsgstack("dev"))