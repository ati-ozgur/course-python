def capitalize_words(s):
    word_list = s.split(" ")
    output = ""
    for word in word_list:
        cap = word.capitalize()
        output = output + cap +      " "
    
    output = output.rstrip()
    return output

line = "adidela gunnu revanth audit amolo karl avery hoffmann david iyer sridhar kathiresan tamilselvan sripathy kyalo benedetta nagaraj patil pranjal parmar nishant patil omkar vishwas rudasunikwa jonas shahveisi sheyda telfort ershed"
result1 = capitalize_words(line)
print(result1)