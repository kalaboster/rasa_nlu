import os
import datetime
import json


class Narrative():
        def __init__(self, narrative_dir=None):
            # Check to be sure it is not none.
            if narrative_dir is None:
                raise ValueError("No narrator as narrator is None.")
            # Check the dir exists.
            if not os.path.isdir(narrative_dir):
                raise ValueError("narrator_dir is not a directory: " + narrative_dir)
            # Check to be sure there are files in the dir.
            if not os.listdir(narrative_dir):
                raise ValueError("narrator_dir is empty: " + narrative_dir)

            self.narrative_dir = narrative_dir
            self.narrative_files = []
            self.narrative_dict = {}

        # Read all the files for narrative and do a simple check to see if they
        # have .json file ending.
        def load_files(self):

            # Check at min that there is a value
            if self.narrative_dir is None:
                raise ValueError("No narrator as narrator is None: " + self.narrative_dir)

            print "Loading files..."

            for (dirpath, dirnames, filenames) in os.walk(self.narrative_dir):
                for filename in filenames:
                    if filename.endswith('.json'):
                        self.narrative_files.append(dirpath + os.path.sep + filename)
                        print dirpath + os.path.sep + filename

            return self.narrative_files


        # Check the files for json and if that json fits the pattern.
        def validate_file_json(self, file):

            json_object = {}

            print(file)
            # Unlike information, it's easier to assume true and any False changes.
            valid = True

            # Check at min that there is a value
            if file is None:
                raise ValueError("No file to check.")

            # Check for file ending for it will be easy and conform user.
            if not file.endswith('.json'):
                valid = False

            # Check for valid json by loading file.
            try:
                json_object = json.loads(file)
                print(json_object)
            except ValueError, e:
                valid = False

            # Check for object assuming that the previous try doesn't puke.
            if not json_object['intent']:
                valid = False

            return valid



            json_data = json.load(file_data)




        # Read all the believed to valid files and load into the Narrative.
        def read_files(self):

            # Check at min that there is a value
            if self.narrative_files is None:
                raise ValueError("No narrative_files is None: " + self.narrative_files)



        def reply(self, intent):

            # Check at min that there is a value
            if self.narrative_dict is None:
                raise ValueError("No narrator as narrator is None: " + self.narrative_dict)
