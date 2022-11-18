phone_codes_list = ["Germany",49,"Thailand",66,"Iran",98,"Honduras",504,"Turkey",90]
# consider or think that every country in this list.
# find me Turkey's international phone code

for index in range(len(phone_codes_list)):
    val = phone_codes_list[index]
    if (val == "Turkey"):
        code = phone_codes_list[index +1]
        print(f"Turkeys phone code is {code}")
        break

