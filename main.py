def main():
    file_contents = ""
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    #print(file_contents)
    
    length_in_words = len(file_contents.split())
    #print(length_in_words)

    character_count = {}

    for character in file_contents:
        if character.lower() in character_count:
            character_count[character.lower()] += 1
        else:
            character_count.update({character.lower(): 1})

    del character_count[" "]
    del character_count["."]
    del character_count["#"]
    #del character_count["/n"]

    print("- - - Begin report of books/frankenstein.txt - - -")
    print(f"{length_in_words} words found in the document")
    print()

    for key  in character_count.keys():
        print(f"The '{key}' character was found {character_count[key]} times")

    print("- - - End report - - -")

    

main()
