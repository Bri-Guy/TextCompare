import random
import matplotlib.pyplot as plt

#amount of bootstrapping trials
NUM_TRIALS = 10000

def main():

    #input text files, modify here
    A = parse('textA.txt')
    B = parse('textB.txt')

    Acounts = get_counts(A)
    Bcounts = get_counts(B)

    A_cl_index = cl_index(Acounts)
    B_cl_index = cl_index(Bcounts)

    A_auto_index = auto_index(Acounts)
    B_auto_index = auto_index(Bcounts)

    combined = A + B

    cl_valid = 0
    auto_valid = 0
    sent_valid = 0
    word_valid = 0
    cl_diff = []
    auto_diff = []

    #bootstrapping
    for i in range(NUM_TRIALS):

        sampleA = []
        sampleB = []
        for j in range(len(A)):
            ind = random.randrange(len(combined))
            sampleA.append(combined[ind])
        for j in range(len(B)):
            ind = random.randrange(len(combined))
            sampleB.append(combined[ind])

        sampleA_counts = get_counts(sampleA)
        sampleB_counts = get_counts(sampleB)

        A_sample_cl = cl_index(sampleA_counts)
        B_sample_cl = cl_index(sampleB_counts)

        A_sample_auto = auto_index(sampleA_counts)
        B_sample_auto = auto_index(sampleB_counts)

        cl_diff.append(A_sample_cl - B_sample_cl)
        auto_diff.append(A_sample_auto - B_sample_auto)

        if abs(A_sample_cl - B_sample_cl) > abs(A_cl_index - B_cl_index):
            cl_valid += 1

        if abs(A_sample_auto - B_sample_auto) > abs(A_auto_index - B_auto_index):
            auto_valid += 1

        if abs(sampleA_counts[1] - sampleB_counts[1]) > abs(Acounts[1] - Bcounts[1]):
            sent_valid += 1

        if abs(sampleA_counts[0] - sampleB_counts[0]) > abs(Acounts[0] - Bcounts[0]):
            word_valid += 1

    #output results
    fig, graph = plt.subplots(3, 2)
    graph[0, 0].hist(Acounts[2])
    graph[0, 0].set_title('Characters per Word in Text A')
    graph[0, 0].axvline(Acounts[0], color='red')
    graph[0, 1].hist(Bcounts[2])
    graph[0, 1].set_title('Characters per Word in Text B')
    graph[0, 1].axvline(Bcounts[0], color='red')
    graph[1, 0].hist(Acounts[3])
    graph[1, 0].set_title('Words per Sentence in Text A')
    graph[1, 0].axvline(Acounts[1], color='red')
    graph[1, 1].hist(Bcounts[3])
    graph[1, 1].set_title('Words per Sentence in Text B')
    graph[1, 1].axvline(Bcounts[1], color='red')
    graph[2, 0].hist(cl_diff)
    graph[2, 0].axvline(abs(A_cl_index - B_cl_index), color='red')
    graph[2, 0].axvline(-abs(A_cl_index - B_cl_index), color='red')
    graph[2, 0].set_title('CL Index Diff (Bootstrapping)')
    graph[2, 1].hist(auto_diff)
    graph[2, 1].axvline(abs(A_auto_index - B_auto_index), color='red')
    graph[2, 1].axvline(-abs(A_auto_index - B_auto_index), color='red')
    graph[2, 1].set_title('Auto Index Diff (Bootstrapping)')

    for g in graph.flat:
        g.set(ylabel='Frequencies')

    fig.tight_layout()

    print()
    print('Text A Coleman-Liau Index:', A_cl_index)
    print('Text B Coleman-Liau Index:', B_cl_index)
    print()
    print('Text A Automated Readability Index:', A_auto_index)
    print('Text B Automated Readability Index:', B_auto_index)
    print()
    print('Text A Mean Sentence Length:', Acounts[1])
    print('Text B Mean Sentence Length:', Bcounts[1])
    print()
    print('Text A Mean Word Length:', Acounts[0])
    print('Text B Mean Word Length:', Bcounts[0])
    print()
    print('Coleman-Liau Index p-value:', cl_valid / NUM_TRIALS)
    print('Automated Readability Index p-value:', auto_valid / NUM_TRIALS)
    print('Mean Sentence Length p-value:', sent_valid / NUM_TRIALS)
    print('Mean Word Length p-value:', word_valid / NUM_TRIALS)
    print()

    plt.show()

#Automated Readability Index
def auto_index(counts):
    return 4.71 * counts[4]/counts[5] + 0.5 * counts[5]/len(counts[3]) - 21.43

#Coleman-Liau Index
def cl_index(counts):
    sent_per_word = 1 / counts[1]
    return 0.0588 * 100 * counts[0] - 0.296 * 100 * sent_per_word - 15.8

#Process Word and Sentence Lengths
def get_counts(text):
    words_per_sent = 0
    sent_length = []
    for s in text:
        words_per_sent += len(s)
        sent_length.append(len(s))
    words_per_sent /= len(text)

    chars_per_word = 0
    total_words = 0
    word_length = []
    for s in text:
        for w in s:
            chars_per_word += len(w)
            word_length.append(len(w))
        total_words += len(s)
    total_chars = chars_per_word
    chars_per_word /= total_words

    return (chars_per_word, words_per_sent, word_length, sent_length, total_chars, total_words)

#Process Text Input Files
def parse(filename):
    text = ""
    with open(filename) as f:
        for line in f:
            text += line + " "

    text = text.replace('!', '.')
    text = text.replace('?', '.')
    text = text.replace('—', ' ')
    text = text.replace('-', ' ')
    sentences = text.split('.')

    words = []
    for s in sentences:
        w = s.split(' ')
        add = []
        for word in w:
            curr = ''
            for ch in word:
                if ch.isalpha():
                    curr += ch

            if len(curr) >= 1:
                add.append(curr)
        words.append(add)

    return words

if __name__ == "__main__":
    main()
