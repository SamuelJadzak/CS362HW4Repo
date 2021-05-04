def nameGen(firstname, lastname):
    try:
        fullname = firstname + " " + lastname
        if not firstname:
            return lastname
        elif not lastname:
            return firstname
        return fullname
    except:
        raise ValueError("input cannot be converted into a string")
