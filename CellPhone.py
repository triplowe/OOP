import CellPhoneClass as c

def main():
    phone = (c.CellPhone("Verizon", "189dxfg", 450))
    phone.set_manufact("AT&T")
    print(phone.get_manufact())
    print(phone.get_model())
    print("$", phone.get_retail_price(), sep = '')

main()