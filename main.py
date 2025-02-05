def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lcase_content = file_contents.lower()
        char_count = {}
        for char in lcase_content:
            if char.isalpha() == True:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

        return(char_count)    

def wordscount():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        contentword = file_contents.split()
        return len(contentword)

beforesortingdict = main()
sorted_worddict = sorted(beforesortingdict.items(),key=lambda x:x[1], reverse=True)



print("--- Begin report of books/frankenstein.txt ---")
print(wordscount(), "words found in the document")
for i in sorted_worddict:
    print(f"The '{i[0]}' character was found '{i[1]}'times")
print("--- End report ---")

