class Course_grade:
    def __init__(self):
        self.exam_score = 0
        self.all_ungraded_assignments = {}
        self.all_graded_assignments = {}
        self.weights = []
        self.exam_weight = []

    def set_ungraded_assignment(self, assignment_nr: int, score: bool):
        self.all_ungraded_assignments[assignment_nr] = score

    def set_ungraded_assignments(self, scores: list):
        self.all_ungraded_assignments = {
            i: grade for i, grade in enumerate(scores)}

    def set_graded_assignment(self, assignment_nr: int, score: int):
        self.all_graded_assignments[assignment_nr] = score

    def set_graded_assignments(self, scores: list):
        for assignment_nr, score in enumerate(scores):
            self.all_graded_assignments[assignment_nr] = score

    def set_exam(self, score: int):
        self.exam_score = score

    def get_lettered_grade(self, numbered_grade: int):
        if numbered_grade >= 90:
            return 'A'
        elif numbered_grade >= 80:
            return 'B'
        elif numbered_grade >= 60:
            return 'C'
        elif numbered_grade >= 50:
            return 'D'
        elif numbered_grade >= 40:
            return 'E'
        else:
            return 'F'
        return None

    def get_grade(self):
        calculated_scores = []
        # Cases where the student fails the course
        if any(grade == False for nr, grade in self.all_ungraded_assignments.items()) or self.exam_score < 40:
            return 'F'
        if len(self.all_graded_assignments) > 0:
            if sum([grade for nr, grade in self.all_graded_assignments.items()])/(len(self.all_graded_assignments)) < 40:
                return 'F'

        if self.all_graded_assignments:
            calculated_scores = [
                g * w for (i, g), w in zip(self.all_graded_assignments.items(), self.weights)]
        total_exam_score = self.exam_weight * self.exam_score
        calculated_scores.append(total_exam_score)
        final_score = self.get_lettered_grade(sum(calculated_scores))
        return final_score


class ACIT4420_2020(Course_grade):
    def __init__(self):
        super().__init__()
        self.all_graded_assignments = {_: 0 for _ in range(1, 8)}
        self.weights = [.05, .07, .1, .06, .07, .08, .07]
        self.exam_weight = .5


class ACIT4420_2019(Course_grade):
    def __init__(self):
        super().__init__()
        self.all_ungraded_assignments = {_: 0 for _ in range(1, 8)}
        self.exam_weight = 1


def main():
    '''Demonstration'''

    a = ACIT4420_2020()
    a.set_graded_assignments([70, 70, 70, 70, 70, 70, 70])
    a.set_graded_assignment(2, 100)
    a.set_exam(76)
    print(a.get_grade())

    a2 = ACIT4420_2019()
    a2.set_ungraded_assignments([True, True, True, True, True, True, True])
    a2.set_exam(76)
    print(a2.get_grade())

    b = ACIT4420_2020()
    b.set_graded_assignments([20, 20, 20, 20, 20, 20, 20])
    b.set_graded_assignment(2, 100)
    b.set_exam(84)
    print(b.get_grade())

    b2 = ACIT4420_2019()
    b2.set_ungraded_assignments([True, True, True, True, True, True, True])
    b2.set_exam(84)
    print(b2.get_grade())


if __name__ == "__main__":
    main()
