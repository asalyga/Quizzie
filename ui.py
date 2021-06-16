from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class AppUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz app")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_lab = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_lab.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white",)
        self.question_txt = self.canvas.create_text(150, 125,
                                                    width=290,
                                                    text="Some text",
                                                    fill=THEME_COLOR,
                                                    font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_btn_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_btn_img, highlightthickness=0, pady=0, padx=0, command=self.true_ans)
        self.true_btn.grid(row=2, column=0)

        false_btn_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_btn_img, highlightthickness=0, pady=0, padx=0, command=self.false_ans)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_lab.config(text=f"Score: {self.quiz.score}")
            q_txt = self.quiz.next_question()
            self.canvas.itemconfig(self.question_txt, text=q_txt)
        else:
            self.canvas.itemconfig(self.question_txt, text=f"You've answered all questions Your score is {self.quiz.score}/{len(self.quiz.question_list)}")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_ans(self):
        self.feedback(self.quiz.check_answer("True"))

    def false_ans(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
