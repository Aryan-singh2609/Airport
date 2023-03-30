def check_baggage(baggage_weight):
    if 0 <= baggage_weight <= 40:
        return True
    else:
        return False


def check_immigration(expiry_year):
    if 2030 <= expiry_year <= 2050:
        return True
    else:
        return False


def check_security(noc_status):
    if noc_status == 'valid' or 'VALID':
        return True
    else:
        return False


def traveller(t_id, name):
    print('traveller id is: ', t_id, 'traveller name is', name)
    if check_baggage(_baggage_weight) != True or check_immigration(_expiry_year) != True or check_security(_noc_status) != True:
        print("Detain Traveler for Re-checking!")
    else:
        print("Allow to FLY!")


_id = int(input("Enter Id: "))
_name = input("Enter name:")
_baggage_weight = float(input("Enter Baggage weight: "))
_expiry_year = int(input("Enter Year: "))
_noc_status = input("Enter noc status: ")
traveller(_id, _name)
