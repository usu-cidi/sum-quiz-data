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
import json

dotenv.load_dotenv(dotenv.find_dotenv())

TOKEN = os.environ.get('CANVAS_API_TOKEN')
COURSE_ID = os.environ.get('COURSE_ID')
NUM_QUIZZES = os.environ.get('NUM_QUIZZES_IN_COURSE')

BASEURL = 'https://usu.instructure.com'

REQUEST_URL = BASEURL + "/api/v1/courses/" + COURSE_ID + "/quizzes" + "?per_page=" + NUM_QUIZZES

shellCommand = f"curl {REQUEST_URL} \
  -X GET \
  -H 'Authorization: Bearer {TOKEN}'"

quizData = os.popen(shellCommand)

parsedData = json.loads(quizData.read())
quizData.close()

allTheQuizzes = {}

for x in range(0, len(parsedData)):
    allTheQuizzes[parsedData[x]["id"]] = parsedData[x]["title"]

def getAllQuizIDs():
    return allTheQuizzes