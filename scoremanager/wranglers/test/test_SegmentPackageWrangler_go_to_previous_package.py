# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager


def test_SegmentPackageWrangler_go_to_previous_package_01():
    r'''Previous material package.
    '''

    score_manager = scoremanager.core.ScoreManager(is_test=True)
    input_ = 'red~example~score g < < < < q'
    score_manager._run(input_=input_)
    titles = [
        'Score Manager - scores',
        'Red Example Score (2013)',
        'Red Example Score (2013) - segments',
        'Red Example Score (2013) - segments - C',
        'Red Example Score (2013) - segments - B',
        'Red Example Score (2013) - segments - A',
        'Red Example Score (2013) - segments - C',
        ]
    assert score_manager._transcript.titles == titles