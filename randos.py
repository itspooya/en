import uuid
def random_number():
    myrnd = uuid.uuid4().hex 
    myrnd2 = uuid.uuid4().hex
    myrnd = myrnd[:13]
    myrnd2 = myrnd2[:13]
    x = int(myrnd,16)
    y = int(myrnd2,16)
    return(1+0.99*x/(x-y))