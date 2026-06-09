def word_frequency(filename):
    with open(filename, 'r') as file:
        text = file.read().lower().split()
        frequency = {}
        for word in text:
            #freuency[word] = frequency.get(word,0) + 1
            frequency[word] = frequency[word] + 1 if word in frequency else 1
        return frequency
    
if __name__ == "__main__":   filename = input("Enter the filename")
frequencies = word_frequency(filename)
for word,cnt in frequencies.items():
    print(f"{word}: {cnt}")