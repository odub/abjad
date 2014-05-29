# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.core.ScoreManager(is_test=True)


def test_MakerFileWrangler_go_to_segments_01():
    r'''Goes from score maker files to score segments.
    '''

    input_ = 'red~example~score k g q'
    score_manager._run(input_=input_)
    titles = [
        'Score Manager - scores',
        'Red Example Score (2013)',
        'Red Example Score (2013) - maker files',
        'Red Example Score (2013) - segments',
        ]
    assert score_manager._transcript.titles == titles


def test_MakerFileWrangler_go_to_segments_02():
    r'''Goes from maker file library to segment library.
    '''

    input_ = 'k g q'
    score_manager._run(input_=input_)
    titles = [
        'Score Manager - scores',
        'Score Manager - maker files',
        'Score Manager - segments',
        ]
    assert score_manager._transcript.titles == titles