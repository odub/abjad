# -*- encoding: utf-8 -*-
import os
from abjad import *
configuration = systemtools.AbjadConfiguration()

path_1 = os.path.join(
    configuration.abjad_directory,
    'test_1.ly',
    )
path_2 = os.path.join(
    configuration.abjad_directory,
    'test_2.ly',
    )

lines = [
    r'\language "english"',
    '',
    r'\new Staff {',
    "    c'4",
    "    d'4",
    "    e'4",
    "    f'4",
    ]


def test_systemtools_TestManager_compare_lys_01():
    r'''True when lines are exactly the same.
    '''

    with systemtools.FilesystemState(remove=[path_1, path_2]):
        first_lines = [r'\version "2.19.7"'] + lines
        second_lines = first_lines[:]
        file(path_1, 'w').write('\n'.join(first_lines))
        file(path_2, 'w').write('\n'.join(second_lines))
        assert systemtools.TestManager.compare_lys(path_1, path_2)


def test_systemtools_TestManager_compare_lys_02():
    r'''True when version strings differ.
    '''

    with systemtools.FilesystemState(remove=[path_1, path_2]):
        first_lines = [r'\version "2.19.7"'] + lines
        second_lines = [r'\version "2.19.8"'] + lines
        file(path_1, 'w').write('\n'.join(first_lines))
        file(path_2, 'w').write('\n'.join(second_lines))
        assert systemtools.TestManager.compare_lys(path_1, path_2)


def test_systemtools_TestManager_compare_lys_03():
    r'''False when any other lines differ.
    '''

    with systemtools.FilesystemState(remove=[path_1, path_2]):
        first_lines = [r'\version "2.19.7"'] + lines
        second_lines = [r'\version "2.19.8"'] + lines + ['foo']
        file(path_1, 'w').write('\n'.join(first_lines))
        file(path_2, 'w').write('\n'.join(second_lines))
        assert not systemtools.TestManager.compare_lys(path_1, path_2)