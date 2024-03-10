# import matplotlib features
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.lines as lines
import matplotlib.patches as patches
import numpy as np
import textwrap

# import python libraries
import builtins
import math
import sys

##################
# task specifications
##################
# this is the text to be shown on top of the practice first example
# (the one that was presented initially as a fixed image)
TASK_EXAMPLE_0 = ".םאתהב עיפוי וקו ןומיסה לגעמ ףקיה לע יצחל ,הבושתה ןומיס לע ןמאתהל ידכ .רבכעה תרזעב ךלש הבושתה ןומיס לע ינמאתה .הנוכנה הבושתה תנמוסמ וב המגודל ליגרת ךינפל\n" + \
                 ".תנמוסמה הנוכנה הבושתל ךלש הבושתה תא ימיאתה .היוצרה הבושתל רבכעה תרזעב ןומיסה לגעמ ךרואל וקה תא תא יזיזה\n\n" + \
                 ".ימייסתשכ חוורה שקמ לע יצחל\n"

# this is the text to be shown alone, before the three practice examples
TASK_EXAMPLE_1 = ".ךלש הבושתה תא ןמסל ידכ ןומיסה לגעמ לע וקה תא יזיזה אמגוד לכב .ןומיאל תואמגוד שולש ךינפל ועיפוי תעכ\n" +\
".םודא עבצב עיפות הנוכנה הבושתהו חוורה שקמ לע יצחל ןכמ רחאל\n\n" +\
".ךשמהל חוורה שקמ לע יצחל\n"


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
TASK_EXAMPLE_5 = ".קדובל יארק אנא , המייתסה המישמה\n"


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



############## OLD task items
'''
TASK_ITEMS = [ ("flower", "tree", "cat", 301), # example
               ("car", "traffic light", "stop sign", 123),
               ("cat", "tree", "car", 237),
               ("stop sign", "cat", "house", 83),
               ("cat", "flower", "car", 156),
               ("stop sign", "tree", "traffic light", 319),
               ("stop sign", "flower", "car", 235),
               ("traffic light", "house", "flower", 333),
               ("house", "flower", "stop sign", 260),
               ("car", "stop sign", "tree", 280),
               ("traffic light", "cat", "car", 48),
               ("tree", "flower", "house", 26),
               ("cat", "house", "traffic light", 150)
             ]

'''

##################

FIRST_INTERACTIVE_EXAMPLE_TEXT = "Here is a sample item that has the correct answer drawn in. Practice inputting your response using the mouse.\n"+ \
      "To practice marking your answer, click on the arrow circle and a line will appear.\n" + \
      "Drag the line around the arrow circle using the mouse to the desired response.\n" + \
      "Match your answer to the correct answer shown. Can you satisfy yourself that this answer is the correct answer\n\n"+ \
      "Please press SPACE when finished"

ENTER_INSTRUCTION_TEXT = "Please press SPACE to enter your response."

INSTRUCTION_TEXT_title = " (Spatial Orientation Test) בחרמב תואצמתה קדבמ \n"
INSTRUCTION_TEXT = ".בחרמב תונוש טבמ תודוקנו םינוויכ ןיימדל ךלש תלוכיה תא ןחוב הז קדבמ\n" + \
                   ".ןומיס לגעמו טפשמ עיפוי הנומתל תחתמ .םיטקייבוא רפסמ םימקוממ הבו הנומת יארת קדבמב\n" + \
                   ".רחא טקייבוא ןוויכל הנופו ,הנומתבש םיטקייבואה דחא םוקמב תדמוע תאש ןיימדל ישקבתת תא\n" + \
                   ".תראותמה הביטקפסרפהמ ישילש טקייבוא אצמנ וב ןוויכה תא ףקשמש וק רייצל היהת ךלש המישמה\n" + \
                   ",שדח טקייבוא ןוויכל הנופו הנומתב רחא טקייבוא םוקמב תדמוע תאש ןיימדל ישקבתת בלש לכב\n" + \
                   ".ךיילא סחיב והשלכ ישילש טקייבוא לש םוקימה תא ףקשמש וק רייצל ןכמ רחאלו\n\n" + \
                   ".בשחמה לש רבכעה תרזעב הנומתה תיתחתבש ןומיסה לגעמ יבג לע רייצל ךיילע וקה תא\n" + \
                   ",(ןושארה ץפחה םוקמב) בלש ותואב ךלש ןיימודמה םוקימה תא תפקשמ לגעמה זכרמבש הדוקנה\n" + \
                   ".(הנופ תא וילא ינשה ץפחה לש ןוויכה) ךלש תניימודמה טבמה תדוקנ תא ףקשמ יכנאה ץחהו\n" + \
                   ".וללה תודוקנה יתשל סחיב ישילשה ץפחה לש ןוויכה תא גציימש וק רייצל הכירצ תא\n\n" + \
                   ".דומעה תיתחתבש אמגודל בלשב יטיבה\n" + \
                   ".ץעה ןוויכל הנופו ןומעפה םוקמב תדמוע תאש ןיימדל תשקבתמ תא וז אמגודב\n" + \
                   ".וקווקמ וקכ אמגודב עיפומ רייצל ךירצ היהש וקה .ףותה לש ןוויכה לא עיבצמש וק רייצל התייה אמגודב המישמה\n" + \
                   "?וקווקמה וקה עיבצמ וילא ןוויכב היה ףותה ,ץעה ןוויכל הנופו ןומעפה םוקמב תדמוע תייה םאש ןיימדל הלוכי תא םאה\nֿ\n" + \
                   ".המישמה יבגל תולאש ךל שי םא ןחובה תא ילאש\n\n" + \
                   ".ךשמהל חוורה שקמ לע יצחל\n" 




##################
# main function
##################
def main():
    matplotlib.rcParams['toolbar'] = 'None'
    subject_id = input("Please insert your participant ID: ")
    result_file = open('results-' + str(subject_id) + '.txt', 'w+')

    create_test_window(subject_id)

    builtins.result_file = result_file
    builtins.errors = []
    builtins.task_id = 0
    
    load_task(builtins.task_id)

    plt.show()


##################
# plot creator functions
##################

##################1
def create_instruction_window():
    ins_fig = plt.figure("Instructions", figsize = (25, 14))
    ins_ax = ins_fig.add_subplot(1, 1, 1)
    #ins_ax.text(0.01, 0, INSTRUCTION_TEXT, verticalalignment='center', fontsize=12.5)
    ins_ax.text(0.99, 0.9, INSTRUCTION_TEXT_title, verticalalignment='top', horizontalalignment='right', fontsize=25, weight='bold')
    ins_ax.text(0.99, 0.8, INSTRUCTION_TEXT, verticalalignment='top', horizontalalignment='right', fontsize=35)
    plt.xticks([])
    plt.yticks([])
    plt.ylim([-1.0, 1.0])
    ins_fig.tight_layout()


def create_test_window(SUBJECT_ID):
    test_fig = plt.figure("Perspective Taking Test - Participant " + str(SUBJECT_ID), figsize = (20, 14))
    plt.rcParams['text.usetex'] = False

    # object array subplot
    pic_ax = test_fig.add_subplot(1, 2, 1)
    picture = mpimg.imread('Data/2019v_object_array.png')
    pic_ax.imshow(picture)
    pic_ax.set_xticks([])
    pic_ax.set_yticks([])

    # user input subplot
    input_ax = test_fig.add_subplot(1, 2, 2)
    input_ax.axis('equal')
   

    circle = patches.Circle((0, 0), 1.0, facecolor='none', edgecolor='black', linewidth=3)
    input_ax.add_patch(circle)

    upright_line = lines.Line2D((0, 0), (0, 1), linewidth=3, color='black')
    input_ax.add_line(upright_line)
    input_ax.add_line(lines.Line2D((0, -0.03), (1, 0.95), linewidth=3, color='black')) # left arrow wedge
    input_ax.add_line(lines.Line2D((0, 0.03), (1, 0.95), linewidth=3, color='black')) # right arrow wedge


    # creating main line and example lines
    answer_line = lines.Line2D((0, 0), (0, 1), linewidth=3, color='orange')
    example_line_1 = lines.Line2D((0, 0.838), (0, 0.544), visible=False, linewidth=3, color='red') # added example line 1 
    example_line_2 = lines.Line2D((0, -0.56), (0, 0.83), visible=False, linewidth=3, color='red') # added example line 2
    example_line_3 = lines.Line2D((0, 0.755), (0, 0.656), visible=False, linewidth=3, color='red') # added example line 3

    # adding main line and example lines to axes
    input_ax.add_line(answer_line)
    input_ax.add_line(example_line_1) # added example line
    input_ax.add_line(example_line_2) # added example line
    input_ax.add_line(example_line_3) # added example line


    text_bottom = input_ax.text(0.0, -0.15, 'text_bottom', fontsize=14, horizontalalignment='center')
    text_top = input_ax.text(0.0, 1.15, 'text_top', fontsize=14, horizontalalignment='center')
    text_example = input_ax.text(-1.0, 0.58, 'text_example', fontsize=14, horizontalalignment='center')
    text_instruction = input_ax.text(0.0, -1.2, 'text_instruction', fontsize=14, horizontalalignment='center')
    example_task_instruction = pic_ax.text(300, 480, ' ', fontsize=13, horizontalalignment='center')
    input_ax.set_xlim(-1.5, 1.5)
    input_ax.set_ylim(-1.5, 1.5)
    input_ax.set_xticks([])
    input_ax.set_yticks([])
    test_fig.tight_layout()

    # event handling
    builtins.fig = test_fig
    builtins.answer_line = answer_line
    builtins.example_line_1 = example_line_1
    builtins.example_line_2 = example_line_2
    builtins.example_line_3 = example_line_3
    builtins.picture_ax = pic_ax
    builtins.text_bottom = text_bottom
    builtins.text_top = text_top
    builtins.text_example = text_example
    builtins.text_instruction = text_instruction
    builtins.example_task_instruction = example_task_instruction
    test_fig.canvas.mpl_connect('button_press_event', on_click)
    test_fig.canvas.mpl_connect('key_press_event', on_key_press)


def load_task(INDEX):
    task_id_as_text = str(INDEX)
    item_tuple = TASK_ITEMS[INDEX]
    located_at = item_tuple[0].replace(' ', '\; ')
    facing_to = item_tuple[1].replace(' ', '\; ')
    pointing_to = item_tuple[2].replace(' ', '\; ')


    instruction_text =  r'$\bf{' + pointing_to + '}$ '  + TASK_TEXT_3  + ' ' + r'$\bf{' + facing_to +  '}$ ' + TASK_TEXT_2 + \
                   ' ' + r'$\bf{' + located_at + '}$ ' + TASK_TEXT_1 + ' .' + task_id_as_text
                   
    builtins.text_instruction.set_text(instruction_text)

    if INDEX == 0: # example case
        create_instruction_window() # show general instructions at the beginning
        builtins.answer_line.set_data([0.0, -0.809], [0.0, 0.587])
        text_example.set_text('ףות')
    else:
        builtins.answer_line.set_data([0.0, 0.0], [0.0, 1.0])
        text_example.set_text('')

    if INDEX == 0: # first example task
        builtins.example_task_instruction.set_text(TASK_EXAMPLE_0)
    if INDEX > 0:
        builtins.example_task_instruction.set_text(TASK_EXAMPLE_3)

    
    builtins.text_bottom.set_text(item_tuple[0])
    builtins.text_top.set_text(item_tuple[1])
    builtins.fig.canvas.draw()


##################
# callbacks
##################
def on_click(EVENT):
    if EVENT.inaxes is None:
        return
    length = euclidean_distance([0, 0], [EVENT.xdata, EVENT.ydata])
    builtins.answer_line.set_data([0.0, EVENT.xdata/length], [0.0, EVENT.ydata/length])
    builtins.fig.canvas.draw()


def on_key_press(EVENT):
    if EVENT.key == ' ':
        if builtins.task_id > 0: # exclude example
            correct_angle = round(TASK_ITEMS[builtins.task_id][3], 4)
            logged_angle = round(compute_response_line_angle(), 4)
            error = round(angle_difference(correct_angle, logged_angle), 4)
            builtins.result_file.write(str(builtins.task_id) + ',' + str(correct_angle) + ',' + str(logged_angle) + ',' + str(error) + '\n')
            builtins.errors.append(error)

        # If the task id is between 1 and 3, show the corresponding example line
        if 1 <= builtins.task_id <= 3:
            if builtins.task_id == 1:
                builtins.example_line_1.set_visible(True)
                builtins.fig.canvas.draw()
                plt.pause(5)
                builtins.example_line_1.set_visible(False)

            elif builtins.task_id == 2:
                builtins.example_line_2.set_visible(True)
                builtins.fig.canvas.draw()
                plt.pause(5)
                builtins.example_line_2.set_visible(False)
            
            elif builtins.task_id == 3:
                builtins.example_line_3.set_visible(True)
                builtins.fig.canvas.draw()
                plt.pause(5)
                builtins.example_line_3.set_visible(False)
        builtins.task_id += 1

        

        
        
        
        if builtins.task_id < len(TASK_ITEMS): # move on to the next task
            load_task(builtins.task_id)

        else: # no more tasks, terminate the test
            avg_error = np.mean(builtins.errors)
            builtins.result_file.write('Average Error: ' + str(round(avg_error, 4)))
            builtins.result_file.close()
            print('The test has terminated successfully. Results saved to file ' + builtins.result_file.name + '.')
            sys.exit(0)



##################
# math helpers
##################
def compute_response_line_angle():
    answer_line_data = builtins.answer_line.get_data()
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