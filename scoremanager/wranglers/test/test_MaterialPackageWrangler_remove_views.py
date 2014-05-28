# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.core.ScoreManager(is_test=True)


def test_MaterialPackageWrangler_remove_views_01():
    r'''Makes two views. Removes two views at one time.
    '''

    input_ = 'm vnew _test_100 rm all'
    input_ += ' add instrumentation~(Red~Example~Score) done <return>' 
    input_ += ' m vnew _test_101 rm all'
    input_ += ' add tempo~inventory~(Red~Example~Score) done <return>'
    input_ += ' q' 
    score_manager._run(input_=input_)

    input_ = 'm vls q'
    score_manager._run(input_=input_)
    contents = score_manager._transcript.contents
    assert 'found' in contents
    assert '_test_100' in contents
    assert '_test_101' in contents

    input_ = 'm vrm _test_100-_test_101 <return> q'
    score_manager._run(input_=input_)

    input_ = 'm vls q'
    score_manager._run(input_=input_)
    contents = score_manager._transcript.contents
    assert 'found' in contents or 'found' in contents
    assert '_test_100' not in contents
    assert '_test_101' not in contents


def test_MaterialPackageWrangler_remove_views_02():
    r'''Makes sure selector backtracking works.
    '''

    input_ = 'm vrm b q'
    score_manager._run(input_=input_)

    titles = [
        'Score Manager - scores',
        'Score Manager - materials',
        'Score Manager - materials - select view(s) to remove:',
        'Score Manager - materials',
        ]
    assert score_manager._transcript.titles == titles