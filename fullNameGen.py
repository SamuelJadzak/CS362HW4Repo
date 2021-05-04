def nameGen(firstname, lastname):
    try:
        fullname = firstname + " " + lastname
        if not firstname:
            return lastname
        return fullname
    except:
        raise ValueError("input cannot be converted into a string")
