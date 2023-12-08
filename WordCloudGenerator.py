from wordcloud import WordCloud
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import time

dirname = os.path.dirname(__file__)
content_path = os.path.join(dirname, 'AzureSpeechCC/content.txt')
wordcloud_image_path = os.path.join(dirname, 'latestWordCloud.png')
dither_image_what_path = os.path.join(dirname, 'dither-image-what.py')

#change the value in return to set the single color need, in hsl format.
def grey_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return "#E73E55" 

def generate_wordcloud_from_file(file_path):
    print("Reading " + file_path + "...")
    # read text from file and store in a variable
    with open(file_path, 'r') as file:
        data = file.read()

    print("Generating wordcloud...")
    # create wordcloud using data
    wordcloud = WordCloud(
        background_color="white", height=900, width=1200,
        include_numbers = True, min_word_length=6, # minimum length of word
        max_words = 70, margin = 4 # margin between words
    ).generate(data)

    default_colors = wordcloud.to_array()

    plt.imshow(wordcloud.recolor(color_func=grey_color_func), interpolation="bilinear")

    plt.figure(figsize=(24, 18))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(wordcloud_image_path)
    #plt.savefig('/home/pi/latestWordCloud.png')
    #plt.show()

    # 

def main():
    while True:
        try:
            # Generate wordcloud from content file
            generate_wordcloud_from_file(content_path)
        except ValueError as e:
            print("Warning: Not enough words to generate wordcloud from!")
        # Sleep
        print("Sleeping...")
        time.sleep(250)

if __name__ == "__main__":
    main()
