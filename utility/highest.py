'''

    _   ___    _   ___
   /_\ | _ \  /_\ / __|___ _ __ _  _ _ __  ___ _ _  __ _ ___
  / _ \|   / / _ \\__ \___| '_ \ || | '  \/ _ \ ' \/ _` / _ \
 /_/ \_\_|_\/_/ \_\___/   | .__/\_, |_|_|_\___/_||_\__, \___/
                          |_|   |__/               |___/

ARAS PYmongo example

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0.

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


__author__ = "@netwookie"
__credits__ = ["Rick Kauffman"]
__license__ = "Apache2"
__version__ = "0.1.1"
__maintainer__ = "Rick Kauffman"
__status__ = "Alpha"


'''

import pymongo
from bson.json_util import dumps
from bson.json_util import loads


def get_highest(db):
    highest_record = db.customer.find({}).sort("number", pymongo.DESCENDING).limit(1)

    customer = loads(dumps(highest_record))
    if customer == []:
        number = 1
    else:
        number = customer[0]["number"] + 1

    return number
