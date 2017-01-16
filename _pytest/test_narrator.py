import pytest
import os
from rasa_nlu.narrator.narrative import Narrative

def test_init_no_dir():
    with pytest.raises(ValueError) as error:
        Narrative(os.path.abspath("test_narrative_no"))
    assert error.value.message == 'narrator_dir is not a directory: /home/kalab/github/rasa_nlu/_pytest/test_narrative_no'

def test_init_None():
    with pytest.raises(ValueError) as error:
        Narrative(None)
    assert error.value.message == 'No narrator as narrator is None.'

def test_load():
    narrator = Narrative(os.path.abspath("test_narrative"))
    narrator_files = []
    narrator_files = narrator.load_files()

    assert narrator_files.index('/home/kalab/github/rasa_nlu/_pytest/test_narrative/complement/complement_physical.json') == 1
    assert narrator_files.index('/home/kalab/github/rasa_nlu/_pytest/test_narrative/greet.json') == 0

def test_validate_file_json_True():
    narrator = Narrative(os.path.abspath("test_narrative"))
    valid = narrator.validate_file_json(os.path.abspath("test_narrative/greet.json"))

    assert valid == True

def test_validate_file_json_False_file_ending():
    narrator = Narrative(os.path.abspath("test_narrative"))
    valid = narrator.validate_file_json(os.path.abspath("test_narrative/complement/not_json.txt"))

    assert valid == False

def test_validate_file_json_False_file_empty_json():
    narrator = Narrative(os.path.abspath("test_narrative"))
    valid = narrator.validate_file_json(os.path.abspath("test_narrative/complement/complement_empty.json"))

    assert valid == False

def test_validate_file_json_False_file_missing_intent_json():
    narrator = Narrative(os.path.abspath("test_narrative"))
    valid = narrator.validate_file_json(os.path.abspath("test_narrative/complement/complement_no_intent.json"))

    assert valid == False

def  test_read_files():
    narrator = Narrative(os.path.abspath("test_narrative"))
    narrator_files = []
    narrator_files = narrator.load_files()
    narrative_dict = {}
    narrative_dict = narrator.read_files()

    assert narrative_dict['wordsum_narrative'][0] == {'intent': 'greet', 'response': {'annoyed': 'HI!', 'bored': '...Hi...', 'continued': 'Hi?', 'initial': 'Hi'}, 'state': 'initial'}
