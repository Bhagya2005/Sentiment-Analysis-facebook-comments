from tkinter import *
import tkinter.messagebox
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Function to center the window on the screen
def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

# Function to handle the quit confirmation dialog
def callback():
    if tkinter.messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        main.destroy()

# Function to update the labels with sentiment results
def setResult(type, res):
    main.update() # Add this line to update the GUI
    if type == "neg":
        negativeLabel.configure(text="Negative: " + '%.2f' % res + "\n")
    elif type == "neu":
        neutralLabel.configure(text="Neutral: " + '%.2f' % res + "\n")
    elif type == "pos":
        positiveLabel.configure(text="Positive: " + '%.2f' % res + "\n")

# Function to run sentiment analysis on the input text
def runAnalysis():
    sentences = [line.get()]
    sid = SentimentIntensityAnalyzer()
    for sentence in sentences:
        ss = sid.polarity_scores(sentence)
        for k in sorted(ss):
            setResult(k, ss[k])

# Function to handle the Enter key event
def runByEnter(event):
    typedText.configure(text=line.get())
    runAnalysis()

# Create the main window
main = Tk()
main.title("Sentiment Analysis")
main.geometry("500x300")
main.resizable(width=FALSE, height=FALSE)
main.protocol("WM_DELETE_WINDOW", callback)
main.focus()
center(main)

# Add widgets to the window
label1 = Label(main, text="Enter text:")
label1.pack()

line = Entry(main, width=70)
line.bind("<Return>", runByEnter)
line.pack()

textLabel = Label(main, text="\nEntered Text:", font=("Helvetica", 15))
textLabel.pack()
typedText = Label(main, text="", fg="blue", font=("Helvetica", 20))
typedText.pack()

result = Label(main, text="\nResults", font=("Helvetica", 15))
result.pack()
negativeLabel = Label(main, text="", fg="red", font=("Helvetica", 20))
negativeLabel.pack()
neutralLabel = Label(main, text="", font=("Helvetica", 20))
neutralLabel.pack()
positiveLabel = Label(main, text="", fg="green", font=("Helvetica", 20))
positiveLabel.pack()

# Run the main event loop
main.mainloop()