from matplotlib import pyplot as plt
from matplotlib import animation
from tkinter import *

# intialize input window using tkinter
window = Tk()
window.geometry('350x200')
window.title('Input')
# text input variable
text_var = StringVar()


# closes window when Go button is pressed
def go_clicked():
    window.destroy()


# text entry and go button widgets added
txt = Entry(window, textvariable=text_var, width=10)
txt.pack()
btn = Button(window, text="Go", command=go_clicked)
btn.pack()

# loop window to keep it open until go button destroys
window.mainloop()

# list of x and y values start with 0 and given starting value from input
start = int(text_var.get())
xs = [0]
ys = [start]

# create plot and axes
fig = plt.figure()
ax = fig.add_subplot(1,1,1)


# runs when graph is finished plotting
def show_results():

    # initialize new results window
    window2 = Tk()
    window2.geometry('350x200')
    window2.title('Results')

    # closes plot and results window when done button is clicked
    def done_clicked():
        plt.close()
        window2.destroy()

    # result labels and done button widgets added
    start_lbl = Label(window2, text='Start:\t\t' + str(start))
    start_lbl.grid(column=0, row=0, sticky=W)
    iterations_lbl = Label(window2, text='Iterations:\t' + str(len(xs) - 1))
    iterations_lbl.grid(column=0, row=1, sticky=W)
    max_lbl = Label(window2, text='Max:\t\t' + str(int(max(ys))))
    max_lbl.grid(column=0, row=2, sticky=W)
    done_btn = Button(window2, text="Done", command=done_clicked)
    done_btn.grid(column=0, row=3)

    # loop window until done button destroys
    window2.mainloop()


# function that is sequentially called
def animate(i):

    # add new data point
    xs.append(xs[-1] + 1)
    ys.append(collatz(ys[-1]))

    # clear the axes and plot again with new values
    ax.clear()
    ax.plot(xs, ys)

    # if y value is 1 (reached the end of sequence) stop the animation and show results
    if ys[-1] == 1:
        anim.event_source.stop()
        show_results()


# collatz function
def collatz(i):
    if i % 2 == 0:
        return i / 2
    return 3 * i + 1


# animation object that sequentially calls animate function
anim = animation.FuncAnimation(fig, animate, interval=20)

# makes plot visible
plt.show()

