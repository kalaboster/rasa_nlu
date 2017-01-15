import pytest
from rasa_nlu.narrator.narrative import Narrative



def test_load():
    narrator_dir = "test_narrative"
    narrator = Narrative(narrator_dir)
    narrator_data = narrator.load_files()
