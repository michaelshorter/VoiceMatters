
import os.path
import time
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap
import urllib



#change the value in return to set the single color need, in hsl format.
def grey_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    return "black"



def get_y_and_heights(text_wrapped, dimensions, margin, font):
    """Get the first vertical coordinate at which to draw text and the height of each line of text"""
    # https://stackoverflow.com/a/46220683/9263761
    ascent, descent = font.getmetrics()
  

    # Calculate the height needed to draw each line of text (including its bottom margin)
    line_heights = [
        font.getmask(text_line).getbbox()[3] + descent + margin
        for text_line in text_wrapped
    ]
    # The last line doesn't have a bottom margin
    line_heights[-1] -= margin

    

    # Total height needed
    height_text = sum(line_heights)

    # Calculate the Y coordinate at which to draw the first line of text
    y = (dimensions[1] - height_text) // 2

    # Return the first Y coordinate and a list with the height of each line
    return (y, line_heights)


# define drawing of the words and links separately.
def plot_main_topics(sorted_dict_topics):

    color=["00000","#36454F","#808080","#899499","#D3D3D3"]

    

    px = 1/plt.rcParams['figure.dpi']
    
    fig = plt.figure(figsize=(640*px, 400*px))
    plt.clf()
    
    i = 0
    for key in sorted_dict_topics:
       
        
        plt.text(0.5,0.9-i*0.2, key[0], ha="center", va="center",size=30, color = color[i])

        i = i+1
        
    plt.axis('off')
    plt.savefig('main_topics.png')



def plot_categories(str_scale, str_rating):
    i=0
    px = 1/plt.rcParams['figure.dpi']
    
    fig = plt.figure(figsize=(640*px, 400*px))
 
    # creating the bar plot
    bar = plt.barh(str_scale,str_rating, color ='blacK')
    

     # Add counts above the two bar graphs
    for rect in bar:
        width = rect.get_width()
     
        
        
        
        plt.text(width+0.5,rect.get_y()+rect.get_height()/2, f'{str_rating[i]}', ha='center', va='bottom',color = 'black', size=20)
        #plt.text(rect.get_x() + rect.get_width() /2, 0.08, f'{str_topic[i]}', ha='center', va='bottom',rotation = 90,color = 'white', size=15)
        i=i+1
    plt.xlim(0,10) 
    plt.axvline(x = 10, color = 'black', label = 'axvline - full height',lw=10)
    plt.xticks([])
    plt.tight_layout()
    plt.savefig('categories.png')
  


def plot_text(text,filename,variant):
    
    px = 1/plt.rcParams['figure.dpi']

    fig = plt.figure(figsize=(2000*px, 1200*px))

    if variant == 'summary':

        #bbox_props = dict(boxstyle='round,pad=0', ec='black', lw=1, fc='white')
        plt.text(-0.1, 0, text, family='serif', size=18, wrap=True, color='red')
        #plt.tight_layout(pad=0)
        #plt.subplots_adjust(left=0.1)


    if variant == 'haiku':

        plt.text(0,0.4,text, family='serif',size=24, wrap=True, linespacing=2, multialignment='center',style='italic')


    plt.xticks([])
    #plt.tight_layout()
    plt.axis('off')
    
    plt.savefig(filename)


def plot_text_pil(text,filename):

    FONT_FAMILY = "Helvetica.ttf"
    WIDTH = 640
    HEIGHT = 400
    FONT_SIZE = 20
    V_MARGIN =  1.5
    CHAR_LIMIT = 60
    TEXT_COLOR = (0,0,0)

    # Create the font
    font = ImageFont.truetype(FONT_FAMILY, FONT_SIZE)
    # New image based on the settings defined above
    img = Image.new("RGB", (WIDTH, HEIGHT),color=(255,255,255))
    # Interface to draw on the image
    draw_interface = ImageDraw.Draw(img)

        # Wrap the `text` string into a list of `CHAR_LIMIT`-character strings
    text_lines = wrap(text, CHAR_LIMIT)
    # Get the first vertical coordinate at which to draw text and the height of each line of text
    y, line_heights = get_y_and_heights(
        text_lines,
        (WIDTH, HEIGHT),
        V_MARGIN,
        font
    )

    # Draw each line of text
    for i, line in enumerate(text_lines):
        # Calculate the horizontally-centered position at which to draw this line
        line_width = font.getmask(line).getbbox()[2]
        x = ((WIDTH - line_width) // 2)
      

        # Draw this line
        draw_interface.text((30, y), line, font=font, fill=TEXT_COLOR)

        # Move on to the height at which the next line should be drawn at
        #print(y)
        y += line_heights[i]
        

    # Save the resulting image
    img.save(filename)


def generate_image(img_url):
    file_name = "image.png"
    urllib.request.urlretrieve(image_url,file_name)



def plot_haiku_pil(haiku):

    haiku_lines = haiku.splitlines()
    print(haiku_lines)


    FONT_FAMILY = "Helvetica.ttf"
    WIDTH = 640
    HEIGHT = 400
    FONT_SIZE = 30
    V_MARGIN =  20
    CHAR_LIMIT = 65
    BG_COLOR = "white"
    TEXT_COLOR = (0,0,0)

    # Create the font
    font = ImageFont.truetype("Helvetica.ttf", 35)
    # New image based on the settings defined above
    img = Image.new("RGB", (640, 400),color=(255,255,255))
    # Interface to draw on the image
    draw_interface = ImageDraw.Draw(img)

    # Wrap the `text` string into a list of `CHAR_LIMIT`-character strings
    
    # Get the first vertical coordinate at which to draw text and the height of each line of text
    y_haiku=80 
    line_heights_haiku = 50

        # Draw each line of text
    
    for i, line in enumerate(haiku_lines):
        # Calculate the horizontally-centered position at which to draw this line
        print(line)
        
        try:
            line_width = font.getmask(line).getbbox()[2]
            x = ((WIDTH - line_width) // 2)
      

            # Draw this line
            draw_interface.text((x, y_haiku+50), line, font=font, fill=TEXT_COLOR)

            # Move on to the height at which the next line should be drawn at
            #print(y)
            y_haiku += line_heights_haiku
        except:
            print('getbox not possible')
        

    # Save the resulting image
    img.save("haiku.png")

