import pytest
from rasa_nlu.narrator.narrative import Narrative



def test_load():
    narrator = Narrative("test_narrative")
    narrator_files = narrator.load_files()

    assert narrator_files == {}

def test_load_no_dir():
    with pytest.raises(ValueError) as error:
        Narrative("test_narrative_no")
    assert error.value.message == 'narrator_dir is not a directory: test_narrative_no'

def test_load_None():
    with pytest.raises(ValueError) as error:
        Narrative(None)
    assert error.value.message == 'No narrator as narrator is None.'
