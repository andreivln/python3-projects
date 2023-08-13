from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:



    def __init__(self, quiz_brain: QuizBrain):  
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        # theme
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # images
        false = PhotoImage(file="./images/false.png")  

        true = PhotoImage(file="./images/true.png")  
        # canvas

        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg="#FFFFFF", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=200,                                                                                     text="some question",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 15, "italic")) 
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)


        # buttons
        self.button_right = Button(image=true, highlightthickness=0, command=self.correct)
        self.button_right.grid(column=0, row=2)
        self.button_wrong = Button(image=false, highlightthickness=0, command=self.wrong)
        self.button_wrong.grid(column=1, row=2)

        # label
        self.score = Label(text=f"Score: {0}", highlightthickness=0, bg=THEME_COLOR, fg="#FFFFFF")
        self.score.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")  
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question() 
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quizz.")
            self.button_wrong.config(state="disabled")
            self.button_right.config(state="disabled")  
    def correct(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)


