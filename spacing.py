""" This function corrects the photo layout by changing the placement of the
title and description depending on the number of lines. """

# Examples:
#       draw.text((45, 550), (articles[j])[0], font=font1) #draw title
#       draw.text((45, 770), (articles[j])[1], font=font2) #draw description
#       draw.line((45, 755, 650, 755), fill=(255,255,255), width=1) #draw dividing line



def spacing(lines_in_title, lines_in_description):
    if(lines_in_description==0):
        description_height = 770
        line_height = 0
        title_height = 580

    if(lines_in_description==2):
        description_height = 770
        line_height = 755
        if(lines_in_title==2):
            title_height = 600
        elif(lines_in_title==3):
            title_height = 575
        elif(lines_in_title==4):
            title_height = 540

    elif(lines_in_description==3):
        description_height = 745
        line_height = 730
        if(lines_in_title==2):
            title_height = 580
        elif(lines_in_title==3):
            title_height = 535
        elif(lines_in_title==4):
            title_height = 520

    elif(lines_in_description==4):
        description_height =  730
        line_height = 715
        if(lines_in_title==2):
            title_height = 560
        elif(lines_in_title==3):
            title_height = 517
        elif(lines_in_title==4):
            title_height = 480

    elif(lines_in_description==5):
        description_height = 705
        line_height = 690
        if(lines_in_title==2):
            title_height = 540
        elif(lines_in_title==3):
            title_height = 495
        elif(lines_in_title==4):
            title_height = 460

    elif(lines_in_description==6):
        description_height = 680
        line_height = 665
        if(lines_in_title==2):
            title_height = 520
        elif(lines_in_title==3):
            title_height = 460
        elif(lines_in_title==4):
            title_height = 440

    else:
        title_height = 550
        description_height = 740
        line_height = 725

    return title_height, description_height, line_height
