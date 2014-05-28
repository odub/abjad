# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager

# must be is_test=False to test view application
score_manager = scoremanager.core.ScoreManager(is_test=False)


def test_SegmentPackageWrangler_list_views_01():
    r'''Makes sure only one segment is visible with view.
    '''
    
    input_ = 'g vls vnew _test rm all'
    input_ += ' add A~(Red~Example~Score) done <return>'
    input_ += ' vls vrm _test <return> vls q'
    score_manager._run(input_=input_)
    transcript = score_manager._transcript

    view_list_entries = [
        _ for _ in transcript
        if ('found' in _.contents or 'found' in _.contents)
        ]
    assert len(view_list_entries) == 3

    assert '_test' not in view_list_entries[0].contents
    assert '_test' in view_list_entries[1].contents
    assert '_test' not in view_list_entries[2].contents