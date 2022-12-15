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
import dotenv
from baseAPICall import getOneQuizData

dotenv.load_dotenv(dotenv.find_dotenv())

TOKEN = os.environ.get('CANVAS_API_TOKEN')
COURSE_ID = os.environ.get('COURSE_ID')
BASEURL = 'https://usu.instructure.com'

def getAttemptData(quizID):
    parsedData1 = json.loads(getOneQuizData(quizID))
    quizBlocks = parsedData1["quiz_submissions"]

    attemptData = ""

    for student in quizBlocks:
        if (student["attempt"] != None):
            for attempt in range(0, student["attempt"]):
                requestURL = BASEURL + "/api/v1/courses/" + COURSE_ID + "/quizzes/" + quizID + "/submissions/" + str(student["id"]) + "\?attempt\=" + str(attempt + 1) + " \\"

                shellCommand = f"curl {requestURL}\n -X GET \\\n -H 'Authorization: Bearer {TOKEN}'"

                oneAttempt = os.popen(shellCommand)
                attemptData += oneAttempt.read()
                oneAttempt.close()

    return attemptData