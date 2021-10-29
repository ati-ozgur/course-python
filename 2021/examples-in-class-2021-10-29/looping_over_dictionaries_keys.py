# phone numbers for countries

country_information = {}
country_information["DE"] = [49, "Germany", "Federal Republic of Germany"]
country_information["TR"] = [90, "Turkey", "Republic of Turkey"]
country_information["PK"] = [92, "Pakistan", "Islamic Republic of Pakistan"]
country_information["IN"] = [91, "India", "Republic of India"]


info = country_information["IN"]
print(info)

# key -> value   
for key in country_information.keys():
    val = country_information[key]
    print(key,val)