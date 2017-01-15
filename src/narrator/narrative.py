import os
import datetime
import json


class Narrative():
        def __init__(self, narrative_dir=None):
            # Check to be sure it is not none.
            if narrative_dir is None:
                raise ValueError("No narrator as narrator is None: " + narrative_dir)
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

            for (dirpath, dirnames, filenames) in os.walk(self.narrative_dir):
                for filename in filenames:
                    if filename.endswith('.json'):
                        self.narrative_files.extend(filenames)

                    break

            return self.narrative_files


        # Check the files for json and if that json fits the pattern.
        def check_files_json(self):

            # Check at min that there is a value
            if self.narrative_files is None:
                raise ValueError("No narrative_files is None: " + self.narrative_files)

            for file in self.narrative_files:
                with open(file) as file_data:
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
