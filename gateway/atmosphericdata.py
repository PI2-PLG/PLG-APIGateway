import os
#Class used to test the values that are going to be transmited to other microservices
def atmospheric(userid, towerid, temperature, co2, umidadear, latitude, longitude):
    try:
        userid = int(userid)
    except ValueError:
        print("""userid not a int!""")
        raise
    try:
        towerid = int(towerid)
    except ValueError:
        print("towerid not a int!")
        raise
    try:
        temperature = int(temperature)
    except ValueError:
        print("temperature not a int!")
        raise

    try:
        co2 = int(co2)
    except ValueError:
        print("co2 not a int!")
        raise
    try:
        umidadear = int(umidadear)
    except ValueError:
        print("umidadear not a int!")
        raise
    try:
        latitude = int(latitude)
    except ValueError:
        print("umidadear not a int!")
        raise
    try:
        longitude = int(longitude)
    except ValueError:
        print("longitude not a int!")
        raise
    return atmospheric

def main():
    user = raw_input("enter userid")
    tower = raw_input("enter towerid")
    temp = raw_input("enter temperature")
    co = raw_input("enter co2")
    umidade = raw_input("enter umidadear")
    lat = raw_input("enter latitude")
    lon = raw_input("enter longitude")
    atmospheric(user,tower,temp,co,umidade,lat,lon)
