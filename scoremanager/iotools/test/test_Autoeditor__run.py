# -*- encoding: utf-8 -*-
from abjad import *
from experimental.tools import handlertools
import scoremanager


def test_Autoeditor__run_01():
    r'''Edits clef name.
    '''

    target = Clef('alto')
    session = scoremanager.core.Session(is_test=True)
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        target=target,
        )
    input_ = 'nm tenor done'
    editor._run(pending_input=input_)

    assert editor.target == Clef('tenor')


def test_Autoeditor__run_02():
    r'''Creates default tempo.
    '''

    target = Tempo()
    session = scoremanager.core.Session(is_test=True)
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        target=target,
        )
    input_ = 'done'
    editor._run(pending_input=input_)

    assert editor.target is target


def test_Autoeditor__run_03():
    r'''Edits tempo duration with pair.
    '''

    session = scoremanager.core.Session(is_test=True)
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        target=Tempo(),
        )
    input_ = 'duration (1, 8) units 98 done'
    editor._run(pending_input=input_)

    assert editor.target == Tempo(Duration(1, 8), 98)


def test_Autoeditor__run_04():
    r'''Edits tempo duration with duration object.
    '''

    session = scoremanager.core.Session(is_test=True)
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        target=Tempo(),
        )
    input_ = 'duration Duration(1, 8) units 98 done'
    editor._run(pending_input=input_)

    assert editor.target == Tempo(Duration(1, 8), 98)


def test_Autoeditor__run_05():
    r'''Edits markup contents.
    '''

    session = scoremanager.core.Session(is_test=True)
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        target=Markup(),
        )
    input_ = 'arg foo~text done'
    editor._run(pending_input=input_)

    markup = markuptools.Markup('foo text')
    assert editor.target == markup


def test_Autoeditor__run_06():
    r'''Edits markup contents and direction.
    '''

    session = scoremanager.core.Session(is_test=True)
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        target=Markup(),
        )
    input_ = '''arg '"foo~text~here"' dir up done'''
    editor._run(pending_input=input_)

    assert editor.target == Markup('"foo text here"', direction=Up)


def test_Autoeditor__run_07():
    r'''Edits markup contents and direction.
    '''

    target = Markup('foo bar')
    session = scoremanager.core.Session(is_test=True)
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        target=target,
        )
    input_ = 'arg entirely~new~text direction up done'
    editor._run(pending_input=input_)

    assert editor.target == Markup('entirely new text', direction=Up)


def test_Autoeditor__run_08():
    r'''Edits mapping component source and target.
    '''

    target = pitchtools.OctaveTranspositionMappingComponent()
    session = scoremanager.core.Session(is_test=True)
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        target=target,
        )
    input_ = 'source [A0, C8] target -18 q'
    editor._run(pending_input=input_)

    component = pitchtools.OctaveTranspositionMappingComponent('[A0, C8]', -18)
    assert editor.target == component


def test_Autoeditor__run_09():
    r'''Edits pitch range.
    '''

    session = scoremanager.core.Session(is_test=True)
    target = pitchtools.PitchRange()
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        target=target,
        )
    input_ = '1 [F#3, C5) q'
    editor._run(pending_input=input_)

    assert editor.target == pitchtools.PitchRange('[F#3, C5)')

    session = scoremanager.core.Session(is_test=True)
    target = pitchtools.PitchRange()
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        target=target,
        )
    input_ = '1 (A0, C8] q'
    editor._run(pending_input=input_)

    assert editor.target == pitchtools.PitchRange('(A0, C8]')


def test_Autoeditor__run_10():
    r'''While editing pitch range: quit, score, home & junk all work.

    Note that back doesn't yet work here
    because 'b' interprets as named chromatic pitch.
    '''

    session = scoremanager.core.Session(is_test=True)
    target = pitchtools.PitchRange()
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        target=target,
        )
    input_ = 'q'
    editor._run(pending_input=input_)
    assert editor._transcript.signature == (2,)

    session = scoremanager.core.Session(is_test=True)
    target = pitchtools.PitchRange()
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        target=target,
        )
    input_ = 's q'
    editor._run(pending_input=input_)
    assert editor._transcript.signature == (4, (0, 2))

    session = scoremanager.core.Session(is_test=True)
    target = pitchtools.PitchRange()
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        target=target,
        )
    input_ = 'h'
    editor._run(pending_input=input_)
    assert editor._transcript.signature == (2,)

    session = scoremanager.core.Session(is_test=True)
    target = pitchtools.PitchRange()
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        target=target,
        )
    input_ = 'foo q'
    editor._run(pending_input=input_)
    assert editor._transcript.signature == (4, (0, 2))


def test_Autoeditor__run_11():
    r'''Edits hairpin handler.
    '''

    session = scoremanager.core.Session(is_test=True)
    target = handlertools.NoteAndChordHairpinHandler()
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        is_autoadvancing=True,
        target=target,
        )
    input_ = "ht ('p', '<', 'f') Duration(1, 8) done"
    editor._run(pending_input=input_)

    handler = handlertools.NoteAndChordHairpinHandler(
        hairpin_token=('p', '<', 'f'),
        minimum_duration=Duration(1, 8),
        )

    assert editor.target == handler


def test_Autoeditor__run_12():
    r'''Edits hairpins handler.
    '''

    session = scoremanager.core.Session(is_test=True)
    target = handlertools.NoteAndChordHairpinsHandler()
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        is_autoadvancing=True,
        target=target,
        )
    input_ = "ht [('p', '<', 'f')] Duration(1, 8) done"
    editor._run(pending_input=input_)

    handler = handlertools.NoteAndChordHairpinsHandler(
        hairpin_tokens=[('p', '<', 'f')],
        minimum_duration=Duration(1, 8),
        )

    assert editor.target == handler


def test_Autoeditor__run_13():
    r'''Edits patterned articulations handler.
    '''

    session = scoremanager.core.Session(is_test=True)
    target = handlertools.PatternedArticulationsHandler()
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        is_autoadvancing=True,
        target=target,
        )
    input_ = "1 [['.', '^'], ['.']] (1, 16) (1, 8) cs'' c''' done"
    editor._run(pending_input=input_)

    handler = handlertools.PatternedArticulationsHandler(
        articulation_lists=[['.', '^'], ['.']],
        minimum_duration=Duration(1, 16),
        maximum_duration=Duration(1, 8),
        minimum_written_pitch=NamedPitch("cs''"),
        maximum_written_pitch=NamedPitch("c'''"),
        )

    assert editor.target == handler


def test_Autoeditor__run_14():
    r'''Edits reiterated articulation handler.
    '''

    session = scoremanager.core.Session(is_test=True)
    target = handlertools.ReiteratedArticulationHandler()
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        is_autoadvancing=True,
        is_autostarting=True,
        target=target,
        )
    input_ = "['.', '^'] (1, 16) (1, 8) cs'' c''' done"
    editor._run(pending_input=input_)

    handler = handlertools.ReiteratedArticulationHandler(
        articulation_list=['.', '^'],
        minimum_duration=Duration(1, 16),
        maximum_duration=Duration(1, 8),
        minimum_written_pitch=NamedPitch("cs''"),
        maximum_written_pitch=NamedPitch("c'''"),
        )

    assert editor.target == handler


def test_Autoeditor__run_15():
    r'''Edits reiterated articulation handler.
    '''

    session = scoremanager.core.Session(is_test=True)
    target = handlertools.ReiteratedArticulationHandler()
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        is_autoadvancing=True,
        is_autostarting=True,
        target=target,
        )
    input_ = "['.', '^'] None None None None done"
    editor._run(pending_input=input_)

    handler = handlertools.ReiteratedArticulationHandler(
        articulation_list=['.', '^'],
        )

    assert editor.target == handler


def test_Autoeditor__run_16():
    r'''Edits reiterated dynamic handler.
    '''

    session = scoremanager.core.Session(is_test=True)
    target = handlertools.ReiteratedDynamicHandler()
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        is_autoadvancing=True,
        target=target
        )
    input_ = '1 f Duration(1, 8) q'
    editor._run(pending_input=input_)

    handler = handlertools.ReiteratedDynamicHandler(
        dynamic_name='f',
        minimum_duration=Duration(1, 8),
        )

    assert editor.target == handler


def test_Autoeditor__run_17():
    r'''Edits terraced dynamics handler.
    '''

    session = scoremanager.core.Session(is_test=True)
    target = handlertools.TerracedDynamicsHandler()
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        is_autoadvancing=True,
        target=target,
        )
    input_ = "1 ['p', 'f', 'f'] Duration(1, 8) q"
    editor._run(pending_input=input_)

    handler = handlertools.TerracedDynamicsHandler(
        dynamics=['p', 'f', 'f'],
        minimum_duration=Duration(1, 8),
        )

    assert editor.target == handler


def test_Autoeditor__run_18():
    r'''Edits talea rhythm-maker.
    '''

    session = scoremanager.core.Session(is_test=True)
    target = rhythmmakertools.TaleaRhythmMaker()
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        target=target,
        )
    input_ = 't c (-1, 2, -3, 4) d 16 done sdc (6,) xcd (2, 3) done'
    editor._run(pending_input=input_)

    talea = rhythmmakertools.Talea(
        counts=(-1, 2, -3, 4),
        denominator=16,
        )

    maker = rhythmmakertools.TaleaRhythmMaker(
        talea=talea,
        split_divisions_by_counts=(6,),
        extra_counts_per_division=(2, 3),
        )

    assert editor.target == maker


def test_Autoeditor__run_19():
    r'''Adds instruments to performer instrument inventory.
    '''

    session = scoremanager.core.Session(is_test=True)
    target = instrumenttools.Performer()
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        target=target,
        )
    input_ = 'nm flutist i add flute add piccolo done done'
    editor._run(pending_input=input_)

    instruments = instrumenttools.InstrumentInventory([
        instrumenttools.Flute(),
        instrumenttools.Piccolo(),
        ])
    performer = instrumenttools.Performer(
        name='flutist',
        instruments=instruments,
        )

    assert editor.target == performer


def test_Autoeditor__run_20():
    r'''Removes instruments from performer instrument inventory.
    '''

    session = scoremanager.core.Session(is_test=True)
    target = instrumenttools.Performer()
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        target=target,
        )
    input_ = 'nm flutist i add flute add piccolo rm piccolo done done'
    editor._run(pending_input=input_)

    instruments = instrumenttools.InstrumentInventory([
        instrumenttools.Flute(),
        ])
    performer = instrumenttools.Performer(
        name='flutist',
        instruments=instruments,
        )

    assert editor.target == performer


def test_Autoeditor__run_21():
    r'''Moves instruments in performer instrument inventory.
    '''

    session = scoremanager.core.Session(is_test=True)
    target = instrumenttools.Performer()
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        target=target,
        )
    input_ = 'nm flutist i add flute add piccolo mv 1 2 done done'
    editor._run(pending_input=input_)

    instruments = instrumenttools.InstrumentInventory([
        instrumenttools.Piccolo(),
        instrumenttools.Flute(),
        ])
    performer = instrumenttools.Performer(
        name='flutist',
        instruments=instruments,
        )

    assert editor.target == performer


# TODO: migrate to PerformerInventory test
def test_Autoeditor__run_22():
    r'''Adds three performers to instrumentation specifier.
    '''

    session = scoremanager.core.Session(is_test=True)
    target = instrumenttools.InstrumentationSpecifier()
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        target=target,
        )
    input_ = 'ps add accordionist default add bassoonist default'
    input_ += ' add cellist default done done'
    editor._run(pending_input=input_)

    specifier = instrumenttools.InstrumentationSpecifier([
        instrumenttools.Performer(
            name='accordionist',
            instruments=[instrumenttools.Accordion()],
            ),
        instrumenttools.Performer(
            name='bassoonist',
            instruments=[instrumenttools.Bassoon()],
            ),
        instrumenttools.Performer(
            name='cellist',
            instruments=[instrumenttools.Cello()],
            )])

    assert editor.target == specifier


# TODO: migrate to PerformerInventory test
def test_Autoeditor__run_23():
    r'''Adds three performers to instrumentation specifier.

    Tests range handling.
    '''

    session = scoremanager.core.Session(is_test=True)
    target = instrumenttools.InstrumentationSpecifier()
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        target=target,
        )
    input_ = 'ps add 1-3 default default default done done'
    editor._run(pending_input=input_)

    specifier = instrumenttools.InstrumentationSpecifier([
        instrumenttools.Performer(
            name='accordionist',
            instruments=[instrumenttools.Accordion()]),
        instrumenttools.Performer(
            name='alto',
            instruments=[instrumenttools.AltoVoice()]),
        instrumenttools.Performer(
            name='baritone',
            instruments=[instrumenttools.BaritoneVoice()]),
            ])

    assert editor.target == specifier


# TODO: migrate to PerformerInventory test
def test_Autoeditor__run_24():
    r'''Edits instrumentation specifier. Adds three performers. Removes two.
    '''

    session = scoremanager.core.Session(is_test=True)
    target = instrumenttools.InstrumentationSpecifier()
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        target=target,
        )
    input_ = 'ps add acc default add bass default add bassoon default'
    input_ += ' rm 3 rm 2 done done'
    editor._run(pending_input=input_)

    specifier = instrumenttools.InstrumentationSpecifier(
        [
            instrumenttools.Performer(
                'accordionist',
                instruments=[instrumenttools.Accordion()],
                ),
            ]
        )

    assert editor.target == specifier


# TODO: migrate to PerformerInventory test
def test_Autoeditor__run_25():
    r'''Edits instrumentation specifier. Adds and removes.

    Tests range handling.
    '''

    session = scoremanager.core.Session(is_test=True)
    target = instrumenttools.InstrumentationSpecifier()
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        target=target,
        )
    input_ = 'ps add 1-3 default default default rm 3-2 done done'
    editor._run(pending_input=input_)

    specifier = instrumenttools.InstrumentationSpecifier(
        [
            instrumenttools.Performer(
                'accordionist',
                instruments=[instrumenttools.Accordion()],
                )
            ]
        )

    assert editor.target == specifier


# TODO: migrate to PerformerInventory test
def test_Autoeditor__run_26():
    r'''Edits instrumentation specifier. Adds three performers.
    Makes two moves.
    '''

    session = scoremanager.core.Session(is_test=True)
    target = instrumenttools.InstrumentationSpecifier()
    editor = scoremanager.iotools.Autoeditor(
        session=session,
        target=target,
        )
    input_ = 'ps add accordionist default add bassist default'
    input_ += ' add bassoonist bassoon mv 1 2 mv 2 3 done done'
    editor._run(pending_input=input_)

    specifier = instrumenttools.InstrumentationSpecifier([
        instrumenttools.Performer(
            name='bassist',
            instruments=[instrumenttools.Contrabass()],
            ),
        instrumenttools.Performer(
            name='bassoonist',
            instruments=[instrumenttools.Bassoon()],
            ),
        instrumenttools.Performer(
            name='accordionist',
            instruments=[instrumenttools.Accordion()],
            ),
        ])

    assert editor.target == specifier