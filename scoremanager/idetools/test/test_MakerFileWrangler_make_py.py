# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager
score_manager = scoremanager.idetools.AbjadIDE(is_test=True)


def test_MakerFileWrangler_make_py_01():

    path = os.path.join(
        score_manager._configuration.example_score_packages_directory,
        'red_example_score',
        'makers',
        'FooMaker.py',
        )

    with systemtools.FilesystemState(remove=[path]):
        input_ = 'red~example~score k new FooMaker.py q'
        score_manager._run(input_=input_)
        assert os.path.exists(path)