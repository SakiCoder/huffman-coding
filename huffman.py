run = True
while run:
    def sort():
        finished = False
        while not finished:
            swaps = 0
            for i in range(len(letters)-1):
                if letters[i][1] > letters[i+1][1]:
                    letters[i], letters[i+1] = letters[i+1], letters[i]
                    swaps += 1
            if swaps == 0:
                finished = True
    # input sentence
    sentence = input("Enter sentence: ")
    # get letter frequency
    letters = []
    # list of letters and frequency
    for letter in sentence:
        # if letter not already in list
        # add letter to list and the count of 0
        # endif
        present = False
        for letter_frequency in letters:
            if letter in letter_frequency:
                present = True
        if not present:
            letters.append([letter, 0])
        # find index of letter (letter_frequency in letters)
        letter_index = 0
        for index in range(0, len(letters)):
            if letter in letters[index]:
                letter_index = index
        # update count += 1 for letters[index][1]
        letters[letter_index][1] += 1
    # for letter_frequency in letters:
    #     print(f"{letter_frequency[0]}: {letter_frequency[1]}")
    # we now have a list of letters, consisting of several letter frequency pairs as sublists
    # next step: order from most frequent to least frequent (bubble sort)
    sort()
    data = []
    # print(letters) # v1
    data.append(letters.copy())
    # combine letters with lowest frequencies
    # combine first two letters, and then reorder
    progress = True
    while progress:
        if len(letters) >= 2:
            # Combine the least common characters in a new node and adding the individual frequencies of each character together.
            combined_letter = letters[0][0]+letters[1][0]
            combined_frequency = letters[0][1]+letters[1][1]
            letters.remove(letters[1])
            letters.remove(letters[0])
            letters.append([combined_letter, combined_frequency])
            sort()
            data.append(letters.copy()) # or letters[:] or list(letters)
        else:
            progress = False
    # the data (tree) has been formulated
    for row in data:
        print(row)
    character_data = {}
    for character in (data[len(data)-1])[0][0]:
        character_encoding = ""
        previous = (data[len(data)-1])[0][0]
        for i in range(len(data)-1, -1, -1):
            # print(data[i]) # each table
            for j in range(0, len(data[i])):
                # print(data[i][j]) # each row in a table
                if character in data[i][j][0]:
                    if data[i][j][0] != previous: # change
                        # check if before or after the split part
                        # if before, add 0
                        # if after, add 1
                        try:
                            if data[i][j][0]+data[i][j+1][0] == previous:
                                character_encoding += "0"
                            else:
                                character_encoding += "1"
                        except:
                            character_encoding += "1"
                    previous = data[i][j][0]
            # print()
        character_data[character] = character_encoding
        print(character+ ":"+character_encoding)
    # output number of bits used for 7-bit ASCII
    ascii_7_bit = 0
    for letter in sentence:
        ascii_7_bit += 7
    print(f"7-bit ASCII: {ascii_7_bit} bits")
    # output number of bits used for Huffman Coding
    huffman = 0
    for letter in sentence:
        huffman += len(character_data[letter])
    print(f"Huffman coding: {huffman} bits")
    # calculate number of bits saved and compression percentage
    print(f"Number of bits saved: {ascii_7_bit-huffman} bits")
    print(f"Compression percentage: {(ascii_7_bit-huffman)/ascii_7_bit*100}%")
    answered = False
    while not answered:
        again = input("Do you want to go again? (yes/no) ")
        if again == "yes" or again == "Y" or again == "y":
            print()
            answered = True
        elif again == "no" or again == "N" or again == "n":
            answered = True
            run = False