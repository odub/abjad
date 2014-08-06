# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager
ide = scoremanager.idetools.AbjadIDE(is_test=True)


def test_MaterialPackageWrangler_list_init_py_01():

    init_py_path = os.path.join(
        ide._configuration.example_score_packages_directory,
        'red_example_score',
        'materials',
        '__init__.py',
        )

    input_ = 'red~example~score m nl q'
    ide._run(input_=input_)
    contents = ide._transcript.contents

    assert init_py_path in contents