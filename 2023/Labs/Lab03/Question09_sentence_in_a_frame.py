def sentence_in_frame(sentence,frame_character):
    words = sentence.split(" ")
    max_word_length = 0
    for word in words:
        max_word_length = max(len(word),max_word_length)
    
    print(frame_character * (max_word_length + 4))
    for word in words:
        space_count = max_word_length - len(word) + 1
        line = f"{frame_character} {word}"
        line = line + " " * space_count
        line = line + frame_character
        print(line)
    print(frame_character * (max_word_length + 4))

sentence_in_frame("Constructor University 2023 Class", "*")
