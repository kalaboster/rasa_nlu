import pytest
import os
from rasa_nlu.narrator.narrative import Narrative

def test_init_no_dir():
    with pytest.raises(ValueError) as error:
        Narrative("test_narrative_no")
    assert error.value.message == 'narrator_dir is not a directory: test_narrative_no'

def test_init_None():
    with pytest.raises(ValueError) as error:
        Narrative(None)
    assert error.value.message == 'No narrator as narrator is None.'

def test_load():
    narrator = Narrative("test_narrative")
    narrator_files = []
    narrator_files = narrator.load_files()

    assert narrator_files.index('test_narrative/complement/complement_empty.json') == 3
    assert narrator_files.index('test_narrative/greet.json') == 0

def test_validate_file_json():
    narrator = Narrative("test_narrative")
    print(os.path.abspath("test_narrative/greet.json"))
    valid = narrator.validate_file_json("test_narrative/greet.json")


    assert valid == true
