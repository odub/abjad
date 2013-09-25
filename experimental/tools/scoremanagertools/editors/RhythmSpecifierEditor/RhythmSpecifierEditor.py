# -*- encoding: utf-8 -*-
from experimental.tools.scoremanagertools import getters
from experimental.tools.scoremanagertools import io
from experimental.tools.scoremanagertools.editors.ParameterSpecifierEditor \
    import ParameterSpecifierEditor
from experimental.tools.scoremanagertools.editors.TargetManifest \
    import TargetManifest
from experimental.tools.scoremanagertools.specifiers.RhythmSpecifier \
    import RhythmSpecifier


class RhythmSpecifierEditor(ParameterSpecifierEditor):

    ### CLASS VARIABLES ###

    target_manifest = TargetManifest(
        RhythmSpecifier,
        ('name', 'nm', getters.get_string),
        ('description', 'ds', getters.get_string),
        (),
        (
            'rhythm_maker_package_path', 
            'time-menu_entry', 
            'ttm', 
            io.Selector.make_rhythm_maker_package_selector,
            ),
        )
