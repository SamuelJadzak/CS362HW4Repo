def cubeVol(userInput):
    try:
        if(int(userInput) > 0):
            return int(userInput**3)
        else:
            raise ValueError("side length must be greate than zero")
    except:
        raise ValueError("input is not an integer value")


