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
import json
import sys
import Student
from mainAPICall import getAttemptData


def getStudents(quizID):
    f = open("canvasData4737187.txt", "w")
    f.write("")
    f.close()

    resultOfAPICall2 = getAttemptData(quizID)

    f = open("canvasData4737187.txt", "w")
    f.write("")
    f.close()

    indAttempts = resultOfAPICall2.split("}{")

    studentObjs = {}

    # for attempt data
    for attempt in range(0, len(indAttempts)):
        if not attempt == 0:
            indAttempts[attempt] = "{" + indAttempts[attempt]
        if not attempt == (len(indAttempts) - 1):
            indAttempts[attempt] = indAttempts[attempt] + "}"

        if indAttempts[attempt] != '{"errors":[{"message":"The specified resource does not exist."}]}':
            if indAttempts[attempt] != None and indAttempts[attempt] != "":
                parsedData = json.loads(indAttempts[attempt])
                forInParsedAttempts = parsedData["quiz_submissions"]
                thisID = forInParsedAttempts[0]["user_id"]
                if (thisID in studentObjs):
                    studentObjs[thisID].addAttempt(forInParsedAttempts[0], "testQuiz")
                else:
                    studentObjs[thisID] = Student.Student(thisID)
                    studentObjs[thisID].addAttempt(forInParsedAttempts[0], "testQuiz")

    return studentObjs