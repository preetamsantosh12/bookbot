import sys
from stats import calculateWords
from stats import createLetterFrequencyMap

def get_book_text(filePath):
    with open(filePath) as file:
        return file.read()
        
def main():
    args = sys.argv;
    if(len(args)!= 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    path = args[1]
    content = get_book_text(path)
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    num_words = calculateWords(content) 
    print(f"Found {num_words} total words")
    print("--------- Character Count -------") 
    frequencyMap = createLetterFrequencyMap(content)
    sortedMap = dict(sorted(frequencyMap.items(), key=lambda item: item[1], reverse=True))
    for x in sortedMap:
        if(x.isalpha()):
            print(f"{x}: {sortedMap[x]}")
    print("============= END ===============")
if __name__ == "__main__":
    main()
