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
                    if self.validate_file_json(dirpath + os.path.sep + filename):
                        self.narrative_files.append(dirpath + os.path.sep + filename)
                        print dirpath + os.path.sep + filename

            return self.narrative_files


        # Check the files for json and if that json fits the pattern.
        def validate_file_json(self, file):

            json_string = ""
            json_object = {}
            # Unlike information, it's easier to assume true and any False changes.
            valid = True

            # Check at min that there is a value
            if file is None:
                raise ValueError("No file to check.")

            # Check for file ending for it will be easy and conform user.
            if not file.endswith('.json'):
                valid = False

            # Open file and read in the json or try.
            if os.path.isfile(file):
                try:
                    with open(file, 'r') as file_data:
                        json_object = json.load(file_data)
                except ValueError, e:
                    valid = False
            else:
                valid = False

            # Check for object assuming that the previous try doesn't puke.
            try:
                value = json_object['wordsum_narrative']
            except KeyError, e:
                valid = False

            return valid


        # Read all the believed to valid files and load into the Narrative.
        def read_files(self):

            narrative_json = json.loads('{"wordsum_narrative" : []}')

            # Check at min that there is a value
            if self.narrative_files is None:
                raise ValueError("No narrative_files is None: " + self.narrative_files)

            for file in self.narrative_files:
                try:
                    with open(file, 'r') as file_data:
                        tmp_dict = json.load(file_data)
                        for item in tmp_dict['wordsum_narrative']:
                            narrative_json['wordsum_narrative'].append(item)
                except ValueError, e:
                    valid = False

            return narrative_json


        def reply(self, intent):

            # Check at min that there is a value
            if self.narrative_dict is None:
                raise ValueError("No narrator as narrator is None: " + self.narrative_dict)
