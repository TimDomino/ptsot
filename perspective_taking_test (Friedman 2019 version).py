# import matplotlib features
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.lines as lines
import matplotlib.patches as patches
import numpy as np

# import python libraries
import builtins
import math
import sys
import time

##################
# task specifications
##################
TASK_TEXT_1 = "Imagine you are standing at the"
TASK_TEXT_2 = "and facing the"
TASK_TEXT_3 = "Point to the"

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

TIME_IN_SECONDS = 5 * 60

INSTRUCTION_TEXT = "This is a test of your ability to imagine different perspectives\n" + \
                   "or orientations in space. On each of the following screens you will\n" + \
                   "see a picture of an array of objects and an \"arrow circle\" with a question\n" + \
                   "about the direction between some of the objects. For the question on\n" + \
                   "each screen, you should imagine that you are standing at one object in\n" + \
                   "the array (which will be named in the center of the circle) and facing\n" + \
                   "another object, named at the top of the circle. Your task is to draw an\n" + \
                   "arrow from the center object showing the direction to a third object\n" + \
                   "from this facing orientation.\n\n" + \
                   "Look at the sample item in the other window. In this item you are asked to\n" + \
                   "imagine that you are standing at the flower, which is named in the center\n" + \
                   "of the circle, and facing the tree, which is named at the top of the\n" + \
                   "circle. Your task is to draw an arrow pointing to the cat. In the sample\n" + \
                   "item this arrow has been drawn for you. In the test items, your task is to\n" + \
                   "draw this arrow. Can you see that if you were at the flower facing the tree,\n" + \
                   "the cat would be in this direction? Please ask the experimenter now if you\n" + \
                   "have any questions about what you are required to do.\n\n" + \
                   "There are 12 items in this test, one on each screen. For each item, the array\n" + \
                   "of objects is shown at the top of the window and the arrow circle is shown at\n" + \
                   "the bottom. Please do not pick up or turn the monitor, and do not make\n" + \
                   "any marks on the maps. Try to mark the correct directions but do not spend\n" + \
                   "too much time on any one question.\n\n" + \
                   "You will have 5 minutes for this test. Use SPACE in the other window to\n" + \
                   "confirm your selections."


##################
# main function
##################
def main():
    matplotlib.rcParams['toolbar'] = 'None'
    subject_id = input("Please insert your participant ID: ")
    result_file = open('results-' + str(subject_id) + '.txt', 'w+')

    create_test_window(subject_id)
    create_instruction_window()

    builtins.result_file = result_file
    builtins.errors = []
    builtins.task_id = 0
    load_task(builtins.task_id)

    plt.show()


##################
# plot creator functions
##################
def create_instruction_window():
    ins_fig = plt.figure("Instructions", figsize = (8, 7))
    ins_ax = ins_fig.add_subplot(1, 1, 1)
    ins_ax.text(0.01, 0, INSTRUCTION_TEXT, verticalalignment='center', fontsize=12.5)
    plt.xticks([])
    plt.yticks([])
    plt.ylim([-1.0, 1.0])
    ins_fig.tight_layout()


def create_test_window(SUBJECT_ID):
    test_fig = plt.figure("Perspective Taking Test - Participant " + str(SUBJECT_ID), figsize = (7.5, 7.5))

    # object array subplot
    pic_ax = test_fig.add_subplot(2, 1, 1)
    picture = mpimg.imread('object_array.png')
    plt.xticks([])
    plt.yticks([])
    pic_ax.set_title("Remaining Time: " + str(TIME_IN_SECONDS))
    pic_ax.imshow(picture)

    # user input subplot
    input_ax = test_fig.add_subplot(2, 1, 2)
    input_ax.axis('equal')

    circle = patches.Circle((0, 0), 1.015, facecolor='none', edgecolor='black', linewidth=3)
    input_ax.add_patch(circle)

    upright_line = lines.Line2D((0, 0), (0, 1), linewidth=3, color='black')
    input_ax.add_line(upright_line)
    input_ax.add_line(lines.Line2D((0, -0.03), (1, 0.95), linewidth=3, color='black')) # left arrow wedge
    input_ax.add_line(lines.Line2D((0, 0.03), (1, 0.95), linewidth=3, color='black')) # right arrow wedge

    answer_line = lines.Line2D((0, 0), (0, 1), linewidth=3, color='orange')
    input_ax.add_line(answer_line)

    text_bottom = input_ax.text(0.0, -0.15, 'text_bottom', fontsize=10, horizontalalignment='center')
    text_top = input_ax.text(0.0, 1.15, 'text_top', fontsize=10, horizontalalignment='center')
    text_example = input_ax.text(-1.0, 0.58, 'text_example', fontsize=10, horizontalalignment='center')
    text_instruction = input_ax.text(0.0, -1.2, 'text_instruction', fontsize=10, horizontalalignment='center')

    plt.xlim(-1.5, 1.5)
    plt.xticks([])
    plt.ylim(-1.5, 1.5)
    plt.yticks([])
    test_fig.tight_layout()

    # event handling
    builtins.fig = test_fig
    builtins.answer_line = answer_line
    builtins.picture_ax = pic_ax
    builtins.text_bottom = text_bottom
    builtins.text_top = text_top
    builtins.text_example = text_example
    builtins.text_instruction = text_instruction
    test_fig.canvas.mpl_connect('button_press_event', on_click)
    test_fig.canvas.mpl_connect('key_press_event', on_key_press)


def load_task(INDEX):
    task_id_as_text = str(INDEX) + '.'
    item_tuple = TASK_ITEMS[INDEX]
    located_at = item_tuple[0].replace(' ', '\; ')
    facing_to = item_tuple[1].replace(' ', '\; ')
    pointing_to = item_tuple[2].replace(' ', '\; ')

    instruction_text = task_id_as_text + ' ' + TASK_TEXT_1 + ' $\mathtt{' + located_at + '}$ ' + TASK_TEXT_2 + \
                       ' $\mathtt{' + facing_to + '}$. ' + TASK_TEXT_3 + ' $\mathtt{' + pointing_to + '}$.'
    builtins.text_instruction.set_text(instruction_text)
    
    if INDEX == 0: # example case
        builtins.answer_line.set_data([0.0, -0.86], [0.0, 0.52])
        text_example.set_text('cat')
    else:
        builtins.answer_line.set_data([0.0, 0.0], [0.0, 1.0])
        text_example.set_text('')

    if INDEX == 1: # first real task, start timer
        timer = builtins.fig.canvas.new_timer(interval=1000)
        timer.add_callback(update_time)
        builtins.start_time = time.time()
        timer.start()
    
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

        builtins.task_id += 1

        if builtins.task_id < len(TASK_ITEMS): # move on to the next task
            load_task(builtins.task_id)
        else: # no more tasks, terminate the test
            avg_error = np.mean(builtins.errors)
            builtins.result_file.write('Average Error: ' + str(round(avg_error, 4)))
            builtins.result_file.close()
            print('The test has terminated successfully. Results saved to file ' + builtins.result_file.name + '.')
            sys.exit(0)


def update_time():
    elapsed = max(TIME_IN_SECONDS - round(time.time()-builtins.start_time), 0)
    builtins.picture_ax.set_title("Remaining Time: " + str(elapsed))
    builtins.fig.canvas.draw()


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