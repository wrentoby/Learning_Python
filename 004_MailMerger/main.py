#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open(file="D:/New folder/Mail Merge Project Start/Input/Letters/starting_letter.txt",mode="r") as the_format:
    contents = the_format.read()
    #print(contents)
    all_names = []

    with open(file="D:/New folder/Mail Merge Project Start/Input/Names/invited_names.txt",mode="r+") as the_name:
        all_names = [name.strip() for name in the_name.readlines()]

    print(all_names)

    for name in all_names:
        with open(file=f"D:/New folder/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt",mode="w+") as merged:
            merged.write(contents.replace("[name]",f"{name}"))





