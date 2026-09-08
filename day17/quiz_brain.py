class QuizBrain:

    def __init__(self, questions_list):
        self.question_num = 0
        self.questions_list = questions_list
        self.score = 0


    def still_has_questions(self):
        return len(self.questions_list) > self.question_num

    def next_question(self):
        current_question = self.questions_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num } {current_question.text} (True/False): ")
        correct_answer = current_question.answer
        self.check_answer(user_answer, correct_answer)


    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            print("that was correct ")
            self.score +=1
        else:
            print("that was wrong")
        print(f"current score {self.score}/{self.question_num}")
        print("\n")
