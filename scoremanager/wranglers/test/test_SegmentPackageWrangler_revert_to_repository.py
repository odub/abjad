# -*- encoding: utf-8 -*-
import scoremanager


def test_SegmentPackageWrangler_revert_to_repository_01():

    score_manager = scoremanager.core.AbjadIDE(is_test=True)
    score_manager._session._is_repository_test = True
    input_ = 'red~example~score g rrv <return> q'
    score_manager._run(input_=input_)
    assert score_manager._session._attempted_to_revert_to_repository


def test_SegmentPackageWrangler_revert_to_repository_02():

    score_manager = scoremanager.core.AbjadIDE(is_test=True)
    score_manager._session._is_repository_test = True
    input_ = 'g rrv <return> q'
    score_manager._run(input_=input_)
    assert score_manager._session._attempted_to_revert_to_repository