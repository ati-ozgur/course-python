name_sentence = "adidela gunnu revanth amolo karl avery hoffmann david iyer sridhar"
name_list = name_sentence.split()
email_text_template = """
Dear {name}

Hello, we have python lesson today.
Do not forget it.

Best regards

"""


for n in name_list:
    name = n.capitalize()
    email_text = email_text_template.replace("{name}",name)
    print(email_text)

