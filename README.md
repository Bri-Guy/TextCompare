# TextCompare

This Python script compares two texts side by side, analyzing the probability that the two texts were written in the same style and difficulty. The program utilizes the Coleman-Liau Index and Automated Readability Index to determine each text's readability, and the bootstrapping technique is applied when comparing the likelihood that the two texts are the same difficulty.

When there is a single red line in a graph, that represents the mean value over the entire text. When there are two red lines, those represent how extreme the true difference in value is between the two texts.

To test this program out on your own, download the files and modify 'textA.txt' and 'textB.txt' to any texts of your choosing. Ensure that Python and matplotlib are installed on your computer, and run the program by executing the 'compareTexts.py' file.

For more details, check out the full writeup here: https://docs.google.com/document/d/1SCBBEZVfEmaED7xrbKXHzIHmYtACnwC-Zof0t2jDwuc/edit?usp=sharing

Video demo available here: https://youtu.be/Db3JJigJR_w
