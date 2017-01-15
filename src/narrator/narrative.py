import os
import datetime
import json


class Narrative()
        def __init__(self, narrative_dir=None):
            # Check to be sure it is not none.
            if narrative_dir is None:
                raise ValueError("No narrator as narrator is None: " + narrative_dir)
            # Check the dir exists.
            if not os.path.isdir(narrative_dir):
                raise ValueError("narrator_dir is not a directory: " + narrative_dir)
            # Check to be sure there are files in the dir.
            if not os.listdir(work_path):
                raise ValueError("narrator_dir is empty: " + narrative_dir)

            self.narrative_dir = narrative_dir
            self.narrative_list = []

        def load():

            # Check at min that there is a value
            if self.narrative_dir is None:
                raise ValueError("No narrator as narrator is None: " + narrative_dir)


        def load_files(self, dir):

            # Check at min that there is a value
            if self.narrative_dir is None:
                raise ValueError("No narrator as narrator is None: " + narrative_dir)

            # Read directory for files.

            # If files then loop through non diretories

        def read_file(self):


        def response(self, intent):
