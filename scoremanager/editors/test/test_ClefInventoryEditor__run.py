# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager


def test_ClefInventoryEditor__run_01():

    session = scoremanager.core.Session()
    editor = scoremanager.editors.ClefInventoryEditor(session=session)
    editor._run(pending_user_input='add treble add bass done')

    inventory = indicatortools.ClefInventory(['treble', 'bass'])
    assert editor.target == inventory