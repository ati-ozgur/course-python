phone_codes_list = ["Germany",49,"Thailand",66,"Iran",98,"Honduras",504,"Turkey",90]
# consider or think that every country in this list.
# find me which country has a phone code of 504

for index in range(len(phone_codes_list)):
    code = phone_codes_list[index]
    if (code == 504):
        country = phone_codes_list[index -1]
        print(f"phone code: {code} belongs to country {country}")
        break

