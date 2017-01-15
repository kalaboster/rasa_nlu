import pytest
from rasa_nlu.narrator import Narrative



def test_load():
    narratir_dir = "test_narrative"
    narrator = Narrative(self, narratir_dir)
