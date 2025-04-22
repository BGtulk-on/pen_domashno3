class Course:
    def __init__(self, lessonsis):
        self.lessonsis = lessonsis
        self.index = 0
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.lessonsis):
            lesson = self.lessonsis[self.index]
            self.index += 1
            return f"Урок: {lesson}"
        else:
            raise StopIteration

lessonsis = ["Въведение", "Функции", "Итератори", "Проект"]
course = Course(lessonsis)

for lesson in course:
    print(lesson)
