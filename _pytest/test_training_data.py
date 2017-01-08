# -*- coding: UTF-8 -*-
from rasa_nlu.training_data import TrainingData



def test_wit_spacy():
    td = TrainingData('data/examples/wit/demo-flights.json', 'spacy_sklearn', 'en')
    assert td.fformat == 'wit'


def test_rasa_whitespace():
    td = TrainingData('data/examples/rasa/demo-rasa.json', '', 'en')
    assert td.fformat == 'rasa_nlu'


