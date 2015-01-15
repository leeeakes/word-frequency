
#open file & use readlines to turn it into a list of lines (strings)
#break on spaces, look up split method
#strip out garbage charcters
#run word count functioin to get dict and then covert back to sorted list
#covert back to list so you can sort top 20


with open("sample.txt") as sample_text:
    text_list = sample_text.readlines() #print(text_list)
    text_string = ' '.join(text_list)
    text_string = text_string.lower() #print(text_string)

    for character in ".\"'\!?,;:":
        no_punc = text_string.replace(character, "") #takes out extra characters
    for character in "-":
        no_hyphen = no_punc.replace(character, " ") #changes "-" to a blank space

    strip_down = no_hyphen.split()
    #print(strip_down)

def word_frequency(a_string):
#loops thru word list, makes dict, makes list of tuples and return top 20
    my_dict = {}
    for word in a_string:
        if word not in my_dict:
            my_dict[word] = 1 #adds word in dict if not found with value of 1
        else:
            my_dict[word] += 1 #updated the dict value +1 if already exists

    sorted_list = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    top_20 = sorted_list[:20]

    for item, count in top_20:
        print(item, count)

    #return sorted_list

#print(word_frequency(strip_down))
