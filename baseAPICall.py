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
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

TOKEN = os.environ.get('CANVAS_API_TOKEN')
COURSE_ID = os.environ.get('COURSE_ID')
STUDENTS_IN_COURSE = os.environ.get('STUDENTS_IN_COURSE')

BASEURL = 'https://usu.instructure.com'

def getOneQuizData(quizID):
    REQUEST_URL = BASEURL + "/api/v1/courses/" + COURSE_ID + "/quizzes/" + quizID + "/submissions" + "?per_page=" + STUDENTS_IN_COURSE

    shellCommand = f"curl {REQUEST_URL} \
      -X GET \
      -H 'Authorization: Bearer {TOKEN}'"

    oneQuizData = os.popen(shellCommand)

    parsedData = oneQuizData.read()
    oneQuizData.close()

    f = open("canvasData4737187.txt", "w")
    f.write(parsedData)
    f.close()

    return parsedData

