characteristic={}
def build_profile(first,last,**characteristics):
    characteristic['First Name']=first
    characteristic['Last Name']=last
    for key,value in characteristics.items():
        characteristic[key] = value
    return characteristic