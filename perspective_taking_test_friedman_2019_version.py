# import matplotlib features
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.lines as lines
import matplotlib.patches as patches
import numpy as np
import matplotlib.gridspec as gridspec


# other imports
import tkinter as tk
from tkinter import simpledialog
import time

# import python libraries
import math
import sys

from bidi import algorithm as bidialg

# custom tkinter dialog box in order to display the 'task end' message in a larger font
class CustomDialog(simpledialog.Dialog):
    def body(self, master):
        self.state('normal')  # Maximize the dialog box
        self.title("End of Test")
        self.label = tk.Label(master, text=".המשימה הסתיימה, אנא קראי לבודק", font=("TkDefaultFont", 46))
        self.label.pack()
##################
# task specifications
##################
# this is the text to be shown on top of the practice first example
# (the one that was presented initially as a fixed image
TASK_EXAMPLE_0 = "לפניך תרגיל לדוגמה בו מסומנת התשובה הנכונה.  התאמני על סימון התשובה שלך בעזרת העכבר. כדי להתאמן על סימון התשובה, לחצי על היקף מעגל הסימון וקו יופיע בהתאם. הזיזי את את הקו לאורך מעגל הסימון בעזרת העכבר לתשובה הרצויה. התאימי את התשובה שלך לתשובה הנכונה המסומנת. לחצי על מקש הרווח כשתסיימי"

# add break line at every period, in addition to displaying the text from right to left correctly
TASK_EXAMPLE_0 = bidialg.get_display(TASK_EXAMPLE_0).replace(".", ".\n")


# this is the text to be shown alone, before the three practice examples
TASK_EXAMPLE_1 = ".ךלש הבושתה תא ןמסל ידכ ןומיסה לגעמ לע וקה תא יזיזה אמגוד לכב .ןומיאל תואמגוד שולש ךינפל ועיפוי תעכ\n" +\
".םודא עבצב עיפות הנוכנה הבושתהו חוורה שקמ לע יצחל ןכמ רחאל\n\n"


# this is the text to be shown below each of the three practice examples lines 
# below the TASK_TEXT_1, TASK_TEXT_2, and TASK_TEXT_3 combination
TASK_EXAMPLE_2 = ".ימייסתשכ חוורה שקמ לע יצחל\n"

# this is the text to be shown alone, before the 12 test trials
TASK_EXAMPLE_3 = ".תחא המישמ לע ןמז ידמ רתוי יזבזבת לא לבא ,קיודמב תונעל יסנ .תומישמ 21 םילשהל תוקד 5 ךתושרל .קדבמה ליחתי תעכ\n\n" +\
".וישכע ילאש קדבמה יבגל תונורחא תולאש ךל שי םא\n\n" +\
".ליחתהל הנכומ תאש קדובל יעידוה ,אל םא\n"

# this is the text to be shown below each of the test trials 
# below the TASK_TEXT_1, TASK_TEXT_2, and TASK_TEXT_3 combination
TASK_EXAMPLE_4 = ".ימייסתשכ חוורה שקמ לע יצחל\n"

# this is the text to be shown at the end of the test 

TASK_TEXT_1 = "םוקמב תדמוע תאש יניימד"
TASK_TEXT_2 = "ןוויכל הנופו"
TASK_TEXT_3 = "ןוויכל יעיבצה"



# First 4 are example items, the next 12 are the actual test items
TASK_ITEMS = [
    ("ןומעפה", "ץעה", "ףותה", 306),
    ("ףותה", "רוזמרה", "לגלגה", 57),
    ("ןומעפה", "ץעה", "תיבחה", 326),
    ("חפה", "ףותה", "ןומעפה", 49),
    ("לגלגה", "תיבחה", "רוזמרה", 143),
    ("ףותה", "ץעה", "לגלגה", 249),
    ("רוזמרה", "ףותה", "חפה", 93),
    ("ףותה", "ןומעפה", "לגלגה", 165),
    ("רוזמרה", "ץעה", "תיבחה", 318),
    ("רוזמרה", "ןומעפה", "לגלגה", 250),
    ("תיבחה", "חפה", "ןומעפה", 333),
    ("חפה", "ןומעפה", "רוזמרה", 268),
    ("לגלגה", "רוזמרה", "ץעה", 266),
    ("תיבחה", "ףותה", "לגלגה", 41),
    ("ץעה", "ןומעפה", "חפה", 25),
    ("ףותה", "חפה", "תיבחה", 151)
]
# First 4 are example items, the next 12 are the actual test items
TASK_ITEMS_ENGLISH = [
    ("bell", "tree", "drum", 306),
    ("drum", "traffic light", "wheel", 57), 
    ("bell", "tree", "barrel", 326),
    ("trash can", "drum", "bell", 49),
    ("wheel", "barrel", "traffic light", 143),
    ("drum", "tree", "wheel", 249),
    ("traffic light", "drum", "trash can", 93),
    ("drum", "bell", "wheel", 165),
    ("traffic light", "tree", "barrel", 318),
    ("traffic light", "bell", "wheel", 250),
    ("barrel", "trash can", "bell", 333),
    ("trash can", "bell", "traffic light", 268),
    ("wheel", "traffic light", "tree", 266),
    ("barrel", "drum", "wheel", 41),
    ("tree", "bell", "trash can", 25),
    ("drum", "trash can", "barrel", 151)
]

##################

FIRST_INTERACTIVE_EXAMPLE_TEXT = "Here is a sample item that has the correct answer drawn in. Practice inputting your response using the mouse.\n"+ \
      "To practice marking your answer, click on the arrow circle and a line will appear.\n" + \
      "Drag the line around the arrow circle using the mouse to the desired response.\n" + \
      "Match your answer to the correct answer shown. Can you satisfy yourself that this answer is the correct answer\n\n"+ \
      "Please press SPACE when finished"

INSTRUCTION_TEXT_title = " (Spatial Orientation Test) בחרמב תואצמתה קדבמ \n"
INSTRUCTION_TEXT = ".ןומיס לגעמ הדיצלו טפשמ עיפוי הנומתל תחתמ .םיטקייבוא רפסמ םימקוממ הבו הנומת יארת קדבמב .בחרמב תונוש טבמ תודוקנו םינוויכ ןיימדל ךלש תלוכיה תא ןחוב הז קדבמ\n" + \
                   ".תראותמה הביטקפסרפהמ ישילש טקייבוא אצמנ וב ןוויכה תא ףקשמש וק רייצל היהת ךלש המישמה .רחא טקייבוא ןוויכל הנופו ,הנומתבש םיטקייבואה דחא םוקמב תדמוע תאש ןיימדל ישקבתת תא\n" + \
                   ".ךיילא סחיב והשלכ ישילש טקייבוא לש םוקימה תא ףקשמש וק רייצל ןכמ רחאלו ,שדח טקייבוא ןוויכל הנופו הנומתב רחא טקייבוא םוקמב תדמוע תאש ןיימדל ישקבתת בלש לכב\n\n" + \
                   ",(ןושארה ץפחה םוקמב) בלש ותואב ךלש ןיימודמה םוקימה תא תפקשמ לגעמה זכרמבש הדוקנה .בשחמה לש רבכעה תרזעב הנומתה דצלש ןומיסה לגעמ יבג לע רייצל ךיילע וקה תא\n" + \
                   ".וללה תודוקנה יתשל סחיב ישילשה ץפחה לש ןוויכה תא גציימש וק רייצל הכירצ תא .(הנופ תא וילא ינשה ץפחה לש ןוויכה) ךלש תניימודמה טבמה תדוקנ תא ףקשמ יכנאה ץחהו\n\n" + \
                   ".ףותה לש ןוויכה לא עיבצמש וק רייצל התייה אמגודב המישמה .ץעה ןוויכל הנופו ןומעפה םוקמב תדמוע תאש ןיימדל תשקבתמ תא וז אמגודב .דומעה תיתחתבש אמגודל בלשב יטיבה\n" + \
                   "?וקווקמה וקה עיבצמ וילא ןוויכב היה ףותה , ץעה ןוויכל הנופו ןומעפה םוקמב תדמוע תייה םאש ןיימדל הלוכי תא םאה .וקווקמ וקכ אמגודב עיפומ רייצל ךירצ היהש וקה\n\n" + \
                   ".המישמה יבגל תולאש ךל שי םא ןחובה תא ילאש\n"



##################
# Global variables for the plot creator functions and instructions
##################
fig = None
answer_line = None
example_line_1 = None
example_line_2 = None
example_line_3 = None
picture_ax = None
text_bottom = None
text_top = None
text_example = None
text_instruction = None
example_task_instruction = None


###########
# Some global variables for the tkinter and font and dpi settings
###########
root = tk.Tk() # open a tkinter window to get the screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.withdraw()  # Hide the tkinter window
dpi = 100 # set the dpi for the instructions window and the test window
# Convert screen size from pixels to inches for matplotlib
screen_width_in = screen_width / dpi  
screen_height_in = screen_height / dpi
fontsize_instruction = 15  # Set font size for the instructions window
fontsize_test = 13  # Set font size for the test window

##########
# global varibles for time
##########
start_time = 0
timer = None
elapsed_time = 0




##################
# main function
##################
def main():
    global dpi ,fontsize_instruction, fontsize_test, screen_height_in, screen_width_in, result_file, errors, task_id
    matplotlib.rcParams['toolbar'] = 'None'
    subject_id = input("Please insert your participant ID: ")
    input_values = input("Enter dpi and font size for the instructions window and the test window separated by a space, press 'Enter' for default values(Example input- 100 13 15): ")
    if input_values.strip() == "":
        # if non given, use the default values
        print("Using default values for dpi and font size (dpi=100, fontsize_instruction=15, fontsize_test=13)")
    else:
        dpi, fontsize_instruction, fontsize_test = map(int, input_values.split())
        screen_width_in = screen_width / dpi  
        screen_height_in = screen_height / dpi

    print (f'screen width in inches: {screen_width_in}, screen height in inches: {screen_height_in}')
    result_file = open('results-' + str(subject_id) + '.txt', 'w+')
    create_test_window(subject_id)

    result_file = result_file
    errors = []
    task_id = 0
    load_task(task_id)
    
    plt.show()

##################
# plot creator functions
##################

def create_first_instruction_window():

    # create figure
    ins_fig = plt.figure("Instructions", figsize = (screen_width_in, screen_height_in),dpi=dpi)

    # create subplots with different sizes
    gs = ins_fig.add_gridspec(3, 1)  # adjust the number of rows as needed
    txt_ax = ins_fig.add_subplot(gs[0, :])  # Text on top
    img_ax = ins_fig.add_subplot(gs[1:, :])  # Image on the bottom

    # load image
    img = mpimg.imread('Data/example_image_first_window.png')

    # display image
    img_ax.imshow(img, aspect='equal')

    # remove ticks and 'axis lines' from subplots
    img_ax.axis('off')
    txt_ax.axis('off')

    txt_ax.text(0.99, 0.9, INSTRUCTION_TEXT_title, verticalalignment='top', horizontalalignment='right', fontsize=fontsize_instruction, weight='bold')
    txt_ax.text(0.99, 0.8, INSTRUCTION_TEXT, verticalalignment='top', horizontalalignment='right', fontsize=fontsize_instruction)
    ins_fig.tight_layout()


def create_second_instruction_window():

    # create figure
    ins_fig = plt.figure("Instructions", figsize = (screen_width_in, screen_height_in),dpi=dpi)
    print("success")

    # create subplots
    txt_ax = ins_fig.add_subplot(1, 1, 1)
    # remove ticks and 'axis lines' from plot
    txt_ax.axis('off')
    txt_ax.set_xticks([])
    txt_ax.set_yticks([])

    txt_ax.text(0.99, 0.9, TASK_EXAMPLE_1, verticalalignment='top', horizontalalignment='right', fontsize=fontsize_instruction+5, weight='bold')
    ins_fig.tight_layout()
    plt.show()

def create_third_instruction_window():

    # create figure
    ins_fig = plt.figure("Instructions", figsize = (screen_width_in, screen_height_in),dpi=dpi)
    # create subplots
    txt_ax = ins_fig.add_subplot(1, 1, 1)
    # remove ticks and 'axis lines' from plot
    txt_ax.axis('off')
    txt_ax.set_xticks([])
    txt_ax.set_yticks([])

    txt_ax.text(0.99, 0.9, TASK_EXAMPLE_3, verticalalignment='top', horizontalalignment='right', fontsize=fontsize_instruction+5, weight='bold')
    ins_fig.tight_layout()
    ins_fig.canvas.mpl_connect('close_event', on_close)
    plt.show()

def create_test_window(SUBJECT_ID):
    global fig, answer_line, example_line_1, example_line_2, example_line_3, picture_ax, text_bottom, text_top, text_example, text_instruction, example_task_instruction
    test_fig = plt.figure("Perspective Taking Test - Participant " + str(SUBJECT_ID), figsize = (screen_width_in, screen_height_in), dpi=dpi)
    plt.rcParams['text.usetex'] = False
    # Define the grid
    gs = gridspec.GridSpec(2, 2, width_ratios=[1.5, 1], height_ratios=[1, 1])


    # object array subplot
    pic_ax = test_fig.add_subplot(gs[:, 0])
    pic_ax.imshow(mpimg.imread('Data/2019v_object_array.png'), aspect='equal')
    pic_ax.set_xticks([])
    pic_ax.set_yticks([])
    pic_ax.axis('off')


    # user input subplot
    input_ax = test_fig.add_subplot(gs[:, 1])
    input_ax.axis('equal')
    circle = patches.Circle((0, 0), 1.0, facecolor='none', edgecolor='black', linewidth=3)
    input_ax.add_patch(circle)
    upright_line = lines.Line2D((0, 0), (0, 1), linewidth=3, color='black')
    input_ax.add_line(upright_line)
    input_ax.add_line(lines.Line2D((0, -0.03), (1, 0.95), linewidth=3, color='black')) # left arrow wedge
    input_ax.add_line(lines.Line2D((0, 0.03), (1, 0.95), linewidth=3, color='black')) # right arrow wedge


    # creating main line and example lines
    answer_line = lines.Line2D((0, 0), (0, 1), linewidth=3, color='black')
    example_line_1 = lines.Line2D((0, 0.838), (0, 0.544), visible=False, linewidth=3, color='red') # added example line 1 
    example_line_2 = lines.Line2D((0, -0.56), (0, 0.83), visible=False, linewidth=3, color='red') # added example line 2
    example_line_3 = lines.Line2D((0, 0.755), (0, 0.656), visible=False, linewidth=3, color='red') # added example line 3

    # adding main line and example lines to axes
    input_ax.add_line(answer_line)
    input_ax.add_line(example_line_1) # added example line
    input_ax.add_line(example_line_2) # added example line
    input_ax.add_line(example_line_3) # added example line


    text_bottom = input_ax.text(0.0, -0.15, 'text_bottom', fontsize=fontsize_test, horizontalalignment='center')
    text_top = input_ax.text(0.0, 1.15, 'text_top', fontsize=fontsize_test, horizontalalignment='center')
    text_example = input_ax.text(-1.0, 0.58, 'text_example', fontsize=fontsize_test, horizontalalignment='center')
    text_instruction = input_ax.text(0.0, -1.2, 'text_instruction', fontsize=fontsize_test, horizontalalignment='center')
    # example_task_instruction = pic_ax.text(300, 480, ' ', fontsize=fontsize_test, horizontalalignment='center')
    example_task_instruction = input_ax.text(1.5, -1.3, ' ', fontsize=fontsize_test,horizontalalignment='right', verticalalignment='top',wrap=True)
    input_ax.set_xlim(-1.5, 1.5)
    input_ax.set_ylim(-1.5, 1.5)
    input_ax.set_xticks([])
    input_ax.set_yticks([])
    input_ax.axis('off')
    test_fig.tight_layout()


    # event handling
    fig = test_fig
    answer_line = answer_line
    example_line_1 = example_line_1
    example_line_2 = example_line_2
    example_line_3 = example_line_3
    picture_ax = pic_ax
    text_bottom = text_bottom
    text_top = text_top
    text_example = text_example
    text_instruction = text_instruction
    example_task_instruction = example_task_instruction
    test_fig.canvas.mpl_connect('button_press_event', on_click)
    test_fig.canvas.mpl_connect('key_press_event', on_key_press)


def load_task(INDEX):
    global answer_line,text_example, example_task_instruction, fig, text_bottom, text_top, text_instruction

    item_tuple = TASK_ITEMS[INDEX]
    located_at = item_tuple[0].replace(r' ', r'\; ')
    facing_to = item_tuple[1].replace(r' ', r'\; ')
    pointing_to = item_tuple[2].replace(r' ',r'\; ')


    instruction_text =  r'$\bf{' +  '.' + pointing_to + '}$ '  + TASK_TEXT_3  + ' ' + r'$\bf{' + facing_to +  '}$ ' + TASK_TEXT_2 + \
                   ' ' + r'$\bf{' + located_at + '}$ ' + TASK_TEXT_1
                   
    text_instruction.set_text(instruction_text)
    
    
    if INDEX == 0: # example case
        create_first_instruction_window() # show general instructions at the beginning
        answer_line.set_data([0.0, -0.809], [0.0, 0.587])
        text_example.set_text('ףות')
    else:
        answer_line.set_data([0.0, 0.0], [0.0, 1.0])
        text_example.set_text('')

    if INDEX == 0: # first example task
        example_task_instruction.set_text(TASK_EXAMPLE_0)
    if INDEX == 1:
        print("INDEX 1")
        create_second_instruction_window()
    if INDEX > 0:
        example_task_instruction.set_text(TASK_EXAMPLE_2)
    if INDEX == 4:
        create_third_instruction_window() # Show the final instructions before the test starts
    text_bottom.set_text(item_tuple[0])
    text_top.set_text(item_tuple[1])
    fig.canvas.draw()


##################
# callbacks
##################
def on_click(EVENT):
    global answer_line, fig
    if EVENT.inaxes is None:
        return
    length = euclidean_distance([0, 0], [EVENT.xdata, EVENT.ydata])
    answer_line.set_data([0.0, EVENT.xdata/length], [0.0, EVENT.ydata/length])
    fig.canvas.draw()


def on_key_press(EVENT):
    global task_id,result_file,errors,example_line_1,example_line_2,example_line_3,fig
    if EVENT.key == ' ':
        if task_id > 0: # exclude example
            correct_angle = round(TASK_ITEMS[task_id][3], 4)
            logged_angle = round(compute_response_line_angle(), 4)
            error = round(angle_difference(correct_angle, logged_angle), 4)
            result_file.write(str(task_id) + ',' + str(correct_angle) + ',' + str(logged_angle) + ',' + str(error) + '\n')
            errors.append(error)

        # If the task id is between 1 and 3, show the corresponding example line
        if 1 <= task_id <= 3:
            if task_id == 1:
                example_line_1.set_visible(True)
                fig.canvas.draw()
                plt.pause(5)
                example_line_1.set_visible(False)

            elif task_id == 2:
                example_line_2.set_visible(True)
                fig.canvas.draw()
                plt.pause(5)
                example_line_2.set_visible(False)
            
            elif task_id == 3:
                example_line_3.set_visible(True)
                fig.canvas.draw()
                plt.pause(5)
                example_line_3.set_visible(False)
        task_id += 1

        
        if task_id < len(TASK_ITEMS): # move on to the next task
            load_task(task_id)

        else: # no more tasks, terminate the test
            avg_error = np.mean(errors)
            result_file.write('Average Error: ' + str(round(avg_error, 4)))
            result_file.close()
            print('The test has terminated successfully. Results saved to file ' + result_file.name + '.')
            sys.exit(0)



def on_close(EVENT):
    global fig, start_time, timer
    timer = fig.canvas.new_timer(interval=1000) # create a timer that fires every 1 second
    timer.add_callback(update_time) # add a callback to the timer
    start_time = time.time() # set the start time
    timer.start() # start the timer



def update_time():
    global start_time, elapsed_time,result_file,errors
    elapsed_time = time.time() - start_time
    if elapsed_time > 10.0:
        show_popup_message()
        avg_error = np.mean(errors)
        result_file.write('Average Error: ' + str(round(avg_error, 4)))
        result_file.close()
        print('The test has terminated successfully. Results saved to file ' + result_file.name + '.')
        sys.exit(0)    
    print(f'Time elapsed: {elapsed_time} seconds')
   


def show_popup_message():
    d = CustomDialog(root)

##################
# math helpers
##################
def compute_response_line_angle():
    global answer_line
    answer_line_data = answer_line.get_data()
    answer_line_endpoint = (answer_line_data[0][1], answer_line_data[1][1])
    upright_endpoint = (0.0, 1.0)
    cosine_value = answer_line_endpoint[0]*upright_endpoint[0] + \
                   answer_line_endpoint[1]*upright_endpoint[1]

    angle = angle_between_normalized_2d_vectors(upright_endpoint, answer_line_endpoint) * 180.0/math.pi

    # convert angle to range (0; 360]
    if angle < 0:
        angle *= -1
    else:
        angle = 360.0 - angle

    return angle


def euclidean_distance(POINT_1, POINT_2):
    return math.sqrt(pow(POINT_1[0]-POINT_2[0], 2) + pow(POINT_1[1]-POINT_2[1], 2))


def angle_between_normalized_2d_vectors(VEC1, VEC2):
    return math.atan2(VEC1[0]*VEC2[1] - VEC1[1]*VEC2[0], VEC1[0]*VEC2[0] + VEC1[1]*VEC2[1])


def angle_difference(ANGLE_1, ANGLE_2):
    phi = math.fmod(abs(ANGLE_2-ANGLE_1), 360)
    distance = 360 - phi if phi > 180 else phi
    return distance


if __name__ == '__main__':
    main()