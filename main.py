

def get_frequencies():
    freq = {}
    with open("word_frequency5.txt", "r", encoding="utf8") as f:
        for line in f:
            line_list = line.split(" ")
            w = line_list[0].upper()
            if len(w) == 5:
                n = int(line_list[1])
                freq[w] = n
    return freq

def compare_words(w1, w2, positions, wrong_positions, wrong_letters):
    i = 0
    while i < len(w1):
        if i in positions:
            if w1[i] != w2[i]:
                return False

        if i in wrong_positions.keys() and w1[i] in wrong_positions[i]:
            return False
        if w1[i] in wrong_letters:
            return False
        for key, value in wrong_positions.items():
            for l in value:
                if l not in list(w1):
                    return False
        i += 1

    return True

def main():
    #with open("words5.txt", "r") as f:
    #    words = f.read()

    freqs = get_frequencies()
    words = freqs.keys()
    print("Indexed {} words".format(len(words)))

    #correct_letters = input("Correct letters, wrong position: (A12 B23 C15 ..): ").upper()
    #correct_positions = input("Correct positions: (..AB.): ").upper()
    #wrong_letters = input("Wrong letters: (A B ...): ").upper()
    correct_letters = ""
    correct_positions = ".OUSE"
    wrong_letters = "R A I H M"

    if len(correct_positions) != 5:
        print("Wrong length!")
        return
    positions = []
    word = ['.', '.', '.', '.', '.']
    i = 0
    while i < len(correct_positions):
        letter = correct_positions[i]
        if letter != ".":
            positions.append(i)
            word[i] = letter
        i += 1

    wrong_positions = {}
    if len(correct_letters) > 1:
        correct_letters = correct_letters.split(" ")

        for item in correct_letters:
            npos = len(item)
            letter = item[0]
            i = 1
            while i < npos:
                p = int(item[i]) - 1
                if p not in wrong_positions.keys():
                    wrong_positions[p] = [letter]
                else:
                    wrong_positions[p].append(letter)

                i += 1

    candidates = []
    candidates_dict = {}
    for item in words:
        if compare_words(item, "".join(word), positions, wrong_positions, wrong_letters):
            if item:
                candidates.append(item)
                if item in freqs.keys():
                    candidates_dict[item] = freqs[item]
                else:
                    print("{} not found".format(item))

    print("Candidates: ")
    sorted_candidates = dict(sorted(candidates_dict.items(), key=lambda item: item[1], reverse=True))
    for k,v in sorted_candidates.items():
        if v > 4:
            print("[{}] {}".format(v, k), end="\t")
    print()


if __name__ == '__main__':
    main()
