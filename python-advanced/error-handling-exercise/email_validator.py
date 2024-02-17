class NameTooShortError(Exception):
    """Name must be more than 4 characters"""
    pass

class MustContainAtSymbolError(Exception):
    """Email must contain @"""
    pass

class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""
    pass

email = input()

while email != "End":
    if "@" in email:
        name, other_stuff = email.split("@")
        if len(name) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")
        
        if ".com" not in other_stuff and ".bg" not in other_stuff and ".org" not in other_stuff and ".net" not in other_stuff:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        raise MustContainAtSymbolError("Email must contain @")
    
    print("Email is valid")
    email = input()