""" This function takes a block of text and a number 'n' as parameters, and adds
a line break to the text every n words. This ensures the text fits within the
photo. """

def break_line(full_text, limit):
    all_words = full_text.split(' ')
    final_text = ""
    lines = 0
    characters = 0


    while(len(all_words)>=limit):
        for i in range(limit):
            final_text = final_text + all_words[0] + " "
            characters = characters + len(all_words[0])
            all_words.pop(0)

        final_text = final_text + "\n"
        lines += 1

    if(len(all_words)):
        if(len(all_words[0])>=1 and not(all_words[0] == " ")):
            lines += 1

    for rest in all_words:
        final_text = final_text + rest + " "

    return final_text, lines
