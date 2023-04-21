"""
File: student.py
Resources to manage a student's name and test scores.
"""
import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

    def __eq__(self, student):
        return self.name == student.name
    
    def __lt__(self, student):
        return self.name < student.name
    
    def __ge__(self, student):
        return self.name >= student.name
    
    def generateScore(self):
        for i in range(1, 6):
            self.setScore(i, 100)
    

def main():
    """A simple test."""
    student = Student("Ken", 5)
    student2 = Student("John", 5)
    student3 = Student("Annabelle", 5)
    student4 = Student("Martin", 5)
    student5 = Student("Kelly", 5)

    studentList = [student, student2, student3, student4, student5]

    random.shuffle(studentList)

    print("Shuffled List:")
    i=0
    while i < 5:
        print(studentList[i])
        i+=1
    
    studentList.sort()

    print("\n")
    print("Sorted List")
    j=0
    while j < 5:
        print(studentList[j])
        j+=1

if __name__ == "__main__":
    main()


