def count_vowels(sentence):
    vowels = "aeiou"
    count = 0
    for ch in sentence.lower():
        if ch in vowels:
            count += 1
    return count

sentence = input("Enter the sentence")
print(count_vowels(sentence))
