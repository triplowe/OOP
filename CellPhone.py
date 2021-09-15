import CellPhoneClass as c

def main():
    phone = c.CellPhone("Verizon", "189dxfg", 450)
    phone.set_manufact("AT&T")
    phone.set_model("123456789")
    phone.set_retail_price(700)
    print(phone.get_manufact())
    print(phone.get_model())
    print("$", phone.get_retail_price(), sep = '')

main()