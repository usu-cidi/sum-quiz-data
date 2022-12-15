# Copyright (C) 2022  Emma Lynn
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, version 3 of the License.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import csv
from getAllData import getAllQuizIDs
from parseData import getStudents
from time import time

beginTime = time()

quizIDs = getAllQuizIDs()

f = open("contextReport8747525.txt", "w")
f.write("")
f.close()

def writeToReport(object, label):
    f = open("contextReport8747525.txt", "a")
    f.write(f"{label}: {object}\n")
    f.close()

def getAvg(total, numStudents):
    if numStudents == 0:
        return 0
    return round(total/numStudents, 2)

writeToReport(quizIDs, "QuizIDs")


fields = ["Quiz Name", "Quiz ID", "Average time spent (per student, minutes)", "Average number of attempts made (per student)", "Average score (%)", "Number of students who took quiz"]
rows = []

allTheStudents = {}

timesThrownOut = 0

for quiz in quizIDs:
    numStudentsTook = 0
    totalTimeTaken = 0
    totalAttemptsMade = 0
    totalScorePer = 0

    writeToReport(quiz, "On quiz")
    callResult = getStudents(str(quiz))
    if callResult != None:
        students = callResult
        for student in students:
            writeToReport(student, "On student")

            numStudentsTook += 1
            totalTimeTaken += students[student].getTotalTimeSpent()
            totalAttemptsMade += students[student].getNumAttempts()
            totalScorePer += students[student].getFinalScorePerc()
            if students[student].timeThrownOut:
                timesThrownOut += 1

        rowToAdd = [quizIDs[quiz], quiz, round(getAvg(totalTimeTaken, numStudentsTook - timesThrownOut) / 60, 2), getAvg(totalAttemptsMade, numStudentsTook),
                    getAvg(totalScorePer, numStudentsTook), numStudentsTook]
        rows.append(rowToAdd)
        writeToReport(rowToAdd, "Row added")

outFile = "quizData.csv"

with open(outFile, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

print(f"\nDone in {time() - beginTime:.3f} seconds!")
writeToReport("", f"Done in {time() - beginTime:.3f} seconds!")

if timesThrownOut != 0:
    print(f"Note: {timesThrownOut} piece(s) of time spent data were thrown out since they were over the limit of 4 hours.")

os.remove("canvasData4737187.txt")
#os.remove("contextReport8747525.txt")

os.system('open "quizData.csv"')

