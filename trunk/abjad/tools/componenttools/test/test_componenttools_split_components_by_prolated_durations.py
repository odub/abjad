from abjad import *


def test_componenttools_split_components_by_prolated_durations_01():
    '''Cyclically duration partition one leaf in score.  Do not fracture spanners.
    '''

    t = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(t)
    beamtools.BeamSpanner(t[0])
    beamtools.BeamSpanner(t[1])
    spannertools.SlurSpanner(t.leaves)

    r'''
    \new Staff {
        {
            \time 2/8
            c'8 [ (
            d'8 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    durations = [Duration(3, 64)]
    parts = componenttools.split_components_by_prolated_durations(
        t[0][1:2], durations, cyclic=True, fracture_spanners=False)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 2/8
            c'8 [ (
            d'32.
            d'32. ~
            d'64 ~
            d'64 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert len(parts) == 3
    assert t.lilypond_format == "\\new Staff {\n\t{\n\t\t\\time 2/8\n\t\tc'8 [ (\n\t\td'32.\n\t\td'32. ~\n\t\td'64 ~\n\t\td'64 ]\n\t}\n\t{\n\t\t\\time 2/8\n\t\te'8 [\n\t\tf'8 ] )\n\t}\n}"


def test_componenttools_split_components_by_prolated_durations_02():
    '''Cyclically duration partition multiple leaves in score.  Do not fracture spanners.
    '''

    t = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(t)
    beamtools.BeamSpanner(t[0])
    beamtools.BeamSpanner(t[1])
    spannertools.SlurSpanner(t.leaves)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 2/8
            c'8 [ (
            d'8 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    durations = [Duration(3, 32)]
    parts = componenttools.split_components_by_prolated_durations(
        t.leaves, durations, cyclic=True, fracture_spanners=False)

    r'''
    \new Staff {
        {
            \time 2/8
            c'16. [ (
            c'32
            d'16
            d'16 ]
        }
        {
            \time 2/8
            e'32 [
            e'16.
            f'16.
            f'32 ] )
        }
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert len(parts) == 6
    assert t.lilypond_format == "\\new Staff {\n\t{\n\t\t\\time 2/8\n\t\tc'16. [ (\n\t\tc'32\n\t\td'16\n\t\td'16 ]\n\t}\n\t{\n\t\t\\time 2/8\n\t\te'32 [\n\t\te'16.\n\t\tf'16.\n\t\tf'32 ] )\n\t}\n}"


def test_componenttools_split_components_by_prolated_durations_03():
    '''Cyclically duration partition one measure in score.  Do not fracture spanners.
    '''

    t = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(t)
    beamtools.BeamSpanner(t[0])
    beamtools.BeamSpanner(t[1])
    spannertools.SlurSpanner(t.leaves)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 2/8
            c'8 [ (
            d'8 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    durations = [Duration(3, 32)]
    parts = componenttools.split_components_by_prolated_durations(
        t[:1], durations, cyclic=True, fracture_spanners=False)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 3/32
            c'16. [ (
        }
        {
            \time 3/32
            c'32
            d'16
        }
        {
            \time 2/32
            d'16 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert len(parts) == 3
    assert t.lilypond_format == "\\new Staff {\n\t{\n\t\t\\time 3/32\n\t\tc'16. [ (\n\t}\n\t{\n\t\t\\time 3/32\n\t\tc'32\n\t\td'16\n\t}\n\t{\n\t\t\\time 2/32\n\t\td'16 ]\n\t}\n\t{\n\t\t\\time 2/8\n\t\te'8 [\n\t\tf'8 ] )\n\t}\n}"


def test_componenttools_split_components_by_prolated_durations_04():
    '''Cyclically duration partition multiple measures in score.  Do not fracture spanners.
    '''

    t = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(t)
    beamtools.BeamSpanner(t[0])
    beamtools.BeamSpanner(t[1])
    spannertools.SlurSpanner(t.leaves)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 2/8
            c'8 [ (
            d'8 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    durations = [Duration(3, 32)]
    parts = componenttools.split_components_by_prolated_durations(
        t[:], durations, cyclic=True, fracture_spanners=False)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 3/32
            c'16. [ (
        }
        {
            \time 3/32
            c'32
            d'16
        }
        {
            \time 2/32
            d'16 ]
        }
        {
            \time 1/32
            e'32 [
        }
        {
            \time 3/32
            e'16.
        }
        {
            \time 3/32
            f'16.
        }
        {
            \time 1/32
            f'32 ] )
        }
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert len(parts) == 6
    assert t.lilypond_format == "\\new Staff {\n\t{\n\t\t\\time 3/32\n\t\tc'16. [ (\n\t}\n\t{\n\t\t\\time 3/32\n\t\tc'32\n\t\td'16\n\t}\n\t{\n\t\t\\time 2/32\n\t\td'16 ]\n\t}\n\t{\n\t\t\\time 1/32\n\t\te'32 [\n\t}\n\t{\n\t\t\\time 3/32\n\t\te'16.\n\t}\n\t{\n\t\t\\time 3/32\n\t\tf'16.\n\t}\n\t{\n\t\t\\time 1/32\n\t\tf'32 ] )\n\t}\n}"


def test_componenttools_split_components_by_prolated_durations_05():
    '''Cyclically duration partition list of leaves outside of score.
    '''

    leaves = [Note("c'8"), Note("d'8"), Note("e'8"), Note("f'8")]
    durations = [Duration(3, 32)]
    parts = componenttools.split_components_by_prolated_durations(
        leaves, durations, cyclic=True, fracture_spanners=False)

    assert len(parts) == 6

    t = Staff([])
    for part in parts:
        t.extend(part)

    r'''
    \new Staff {
        c'16.
        c'32
        d'16
        d'16
        e'32
        e'16.
        f'16.
        f'32
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert t.lilypond_format == "\\new Staff {\n\tc'16.\n\tc'32\n\td'16\n\td'16\n\te'32\n\te'16.\n\tf'16.\n\tf'32\n}"


# TODO: Fix cyclic duration partition bug with spanners on outside-of-score measures #

def test_componenttools_split_components_by_prolated_durations_06():
    '''Cyclically duration partition list of measures outside of score.  Do not fracture spanners.
    '''

    measures = Measure((2, 8), notetools.make_repeated_notes(2)) * 2
    beamtools.BeamSpanner(measures[0])
    beamtools.BeamSpanner(measures[1])
    pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(measures)

    durations = [Duration(3, 32)]
    parts = componenttools.split_components_by_prolated_durations(
        measures, durations, cyclic=True, fracture_spanners=False)

    assert len(parts) == 6

    t = Staff([])
    for part in parts:
        t.extend(part)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 3/32
            c'16.
        }
        {
            \time 3/32
            c'32
            d'16
        }
        {
            \time 2/32
            d'16 [ ]
        }
        {
            \time 1/32
            e'32
        }
        {
            \time 3/32
            e'16.
        }
        {
            \time 3/32
            f'16.
        }
        {
            \time 1/32
            f'32 [ ]
        }
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert t.lilypond_format == "\\new Staff {\n\t{\n\t\t\\time 3/32\n\t\tc'16.\n\t}\n\t{\n\t\t\\time 3/32\n\t\tc'32\n\t\td'16\n\t}\n\t{\n\t\t\\time 2/32\n\t\td'16 [ ]\n\t}\n\t{\n\t\t\\time 1/32\n\t\te'32\n\t}\n\t{\n\t\t\\time 3/32\n\t\te'16.\n\t}\n\t{\n\t\t\\time 3/32\n\t\tf'16.\n\t}\n\t{\n\t\t\\time 1/32\n\t\tf'32 [ ]\n\t}\n}"


def test_componenttools_split_components_by_prolated_durations_07():
    '''Duration partition one leaf in score.  Read durations cyclically in list.
    Do not fracture spanners. Do add tie after each split.
    '''

    t = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(t)
    beamtools.BeamSpanner(t[0])
    beamtools.BeamSpanner(t[1])
    spannertools.SlurSpanner(t.leaves)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 2/8
            c'8 [ (
            d'8 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    durations = [Duration(1, 32)]
    parts = componenttools.split_components_by_prolated_durations(
        t[0][1:], durations, cyclic=True, fracture_spanners=False, tie_after=True)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 2/8
            c'8 [ (
            d'32 ~
            d'32 ~
            d'32 ~
            d'32 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert len(parts) == 4
    assert t.lilypond_format == "\\new Staff {\n\t{\n\t\t\\time 2/8\n\t\tc'8 [ (\n\t\td'32 ~\n\t\td'32 ~\n\t\td'32 ~\n\t\td'32 ]\n\t}\n\t{\n\t\t\\time 2/8\n\t\te'8 [\n\t\tf'8 ] )\n\t}\n}"


def test_componenttools_split_components_by_prolated_durations_08():
    '''Duration partition multiple leaves in score.
    Read durations cyclically in list.
    Do not fracture spanners. Do add tie after each leaf split.
    '''

    t = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(t)
    beamtools.BeamSpanner(t[0])
    beamtools.BeamSpanner(t[1])
    spannertools.SlurSpanner(t.leaves)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 2/8
            c'8 [ (
            d'8 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    durations = [Duration(1, 16)]
    parts = componenttools.split_components_by_prolated_durations(
        t.leaves, durations, cyclic=True, fracture_spanners=False, tie_after=True)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 2/8
            c'16 [ ( ~
            c'16
            d'16 ~
            d'16 ]
        }
        {
            \time 2/8
            e'16 [ ~
            e'16
            f'16 ~
            f'16 ] )
        }
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert len(parts) == 8
    assert t.lilypond_format == "\\new Staff {\n\t{\n\t\t\\time 2/8\n\t\tc'16 [ ( ~\n\t\tc'16\n\t\td'16 ~\n\t\td'16 ]\n\t}\n\t{\n\t\t\\time 2/8\n\t\te'16 [ ~\n\t\te'16\n\t\tf'16 ~\n\t\tf'16 ] )\n\t}\n}"


def test_componenttools_split_components_by_prolated_durations_09():
    '''Duration partition one measure in score.
    Read durations cyclically in list.
    Do not fracture spanners. Do add tie after each leaf split.
    '''

    t = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(t)
    beamtools.BeamSpanner(t[0])
    beamtools.BeamSpanner(t[1])
    spannertools.SlurSpanner(t.leaves)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 2/8
            c'8 [ (
            d'8 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    durations = [Duration(1, 16)]
    parts = componenttools.split_components_by_prolated_durations(
        t[:1], durations, cyclic=True, fracture_spanners=False, tie_after=True)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 1/16
            c'16 [ ( ~
        }
        {
            \time 1/16
            c'16
        }
        {
            \time 1/16
            d'16 ~
        }
        {
            \time 1/16
            d'16 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert len(parts) == 4
    assert t.lilypond_format == "\\new Staff {\n\t{\n\t\t\\time 1/16\n\t\tc'16 [ ( ~\n\t}\n\t{\n\t\t\\time 1/16\n\t\tc'16\n\t}\n\t{\n\t\t\\time 1/16\n\t\td'16 ~\n\t}\n\t{\n\t\t\\time 1/16\n\t\td'16 ]\n\t}\n\t{\n\t\t\\time 2/8\n\t\te'8 [\n\t\tf'8 ] )\n\t}\n}"


def test_componenttools_split_components_by_prolated_durations_10():
    '''Duration partition multiple measures in score.
    Read durations cyclically in list.
    Do not fracture spanners. Do add tie after each leaf split.
    '''

    t = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(t)
    beamtools.BeamSpanner(t[0])
    beamtools.BeamSpanner(t[1])
    spannertools.SlurSpanner(t.leaves)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 2/8
            c'8 [ (
            d'8 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    durations = [Duration(3, 32)]
    parts = componenttools.split_components_by_prolated_durations(
        t[:], durations, cyclic=True, fracture_spanners=False, tie_after=True)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 3/32
            c'16. [ ( ~
        }
        {
            \time 3/32
            c'32
            d'16 ~
        }
        {
            \time 2/32
            d'16 ]
        }
        {
            \time 1/32
            e'32 [ ~
        }
        {
            \time 3/32
            e'16.
        }
        {
            \time 3/32
            f'16. ~
        }
        {
            \time 1/32
            f'32 ] )
        }
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert len(parts) == 6
    assert t.lilypond_format == "\\new Staff {\n\t{\n\t\t\\time 3/32\n\t\tc'16. [ ( ~\n\t}\n\t{\n\t\t\\time 3/32\n\t\tc'32\n\t\td'16 ~\n\t}\n\t{\n\t\t\\time 2/32\n\t\td'16 ]\n\t}\n\t{\n\t\t\\time 1/32\n\t\te'32 [ ~\n\t}\n\t{\n\t\t\\time 3/32\n\t\te'16.\n\t}\n\t{\n\t\t\\time 3/32\n\t\tf'16. ~\n\t}\n\t{\n\t\t\\time 1/32\n\t\tf'32 ] )\n\t}\n}"


def test_componenttools_split_components_by_prolated_durations_11():
    '''Cyclically duration partition one leaf in score.  Fracture spanners.
    '''

    t = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(t)
    beamtools.BeamSpanner(t[0])
    beamtools.BeamSpanner(t[1])
    spannertools.SlurSpanner(t.leaves)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 2/8
            c'8 [ (
            d'8 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    durations = [Duration(3, 64)]
    parts = componenttools.split_components_by_prolated_durations(
        t[0][1:2], durations, cyclic=True, fracture_spanners=True)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 2/8
            c'8 [ (
            d'32. )
            d'32. ( )
            d'64 ( ~
            d'64 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert t.lilypond_format == "\\new Staff {\n\t{\n\t\t\\time 2/8\n\t\tc'8 [ (\n\t\td'32. )\n\t\td'32. ( )\n\t\td'64 ( ~\n\t\td'64 ]\n\t}\n\t{\n\t\t\\time 2/8\n\t\te'8 [\n\t\tf'8 ] )\n\t}\n}"


def test_componenttools_split_components_by_prolated_durations_12():
    '''Cyclically duration partition multiple leaves in score.  Fracture spanners.
    '''

    t = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(t)
    beamtools.BeamSpanner(t[0])
    beamtools.BeamSpanner(t[1])
    spannertools.SlurSpanner(t.leaves)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 2/8
            c'8 [ (
            d'8 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    durations = [Duration(3, 32)]
    parts = componenttools.split_components_by_prolated_durations(
        t.leaves, durations, cyclic=True, fracture_spanners=True)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 2/8
            c'16. ( ) [
            c'32 (
            d'16 )
            d'16 ] (
        }
        {
            \time 2/8
            e'32 ) [
            e'16. (
            f'16. )
            f'32 ] ( )
        }
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert len(parts) == 6
    assert t.lilypond_format == "\\new Staff {\n\t{\n\t\t\\time 2/8\n\t\tc'16. ( ) [\n\t\tc'32 (\n\t\td'16 )\n\t\td'16 ] (\n\t}\n\t{\n\t\t\\time 2/8\n\t\te'32 ) [\n\t\te'16. (\n\t\tf'16. )\n\t\tf'32 ] ( )\n\t}\n}"


def test_componenttools_split_components_by_prolated_durations_13():
    '''Cyclically duration partition one measure in score.  Fracture spanners.
    '''

    t = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(t)
    beamtools.BeamSpanner(t[0])
    beamtools.BeamSpanner(t[1])
    spannertools.SlurSpanner(t.leaves)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 2/8
            c'8 [ (
            d'8 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    durations = [Duration(3, 32)]
    parts = componenttools.split_components_by_prolated_durations(
        t[:1], durations, cyclic=True, fracture_spanners=True)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 3/32
            c'16. [ ] ( )
        }
        {
            \time 3/32
            c'32 [ (
            d'16 ] )
        }
        {
            \time 2/32
            d'16 [ ] (
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert len(parts) == 3
    assert t.lilypond_format == "\\new Staff {\n\t{\n\t\t\\time 3/32\n\t\tc'16. [ ] ( )\n\t}\n\t{\n\t\t\\time 3/32\n\t\tc'32 [ (\n\t\td'16 ] )\n\t}\n\t{\n\t\t\\time 2/32\n\t\td'16 [ ] (\n\t}\n\t{\n\t\t\\time 2/8\n\t\te'8 [\n\t\tf'8 ] )\n\t}\n}"


def test_componenttools_split_components_by_prolated_durations_14():
    '''Cyclically duration partition multiple measures in score.  Fracture spanners.
    '''

    t = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(t)
    beamtools.BeamSpanner(t[0])
    beamtools.BeamSpanner(t[1])
    spannertools.SlurSpanner(t.leaves)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 2/8
            c'8 [ (
            d'8 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    durations = [Duration(3, 32)]
    parts = componenttools.split_components_by_prolated_durations(
        t[:], durations, cyclic=True, fracture_spanners=True)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 3/32
            c'16. [ ] ( )
        }
        {
            \time 3/32
            c'32 [ (
            d'16 ] )
        }
        {
            \time 2/32
            d'16 [ ] (
        }
        {
            \time 1/32
            e'32 [ ] )
        }
        {
            \time 3/32
            e'16. [ ] ( )
        }
        {
            \time 3/32
            f'16. [ ] ( )
        }
        {
            \time 1/32
            f'32 [ ] ( )
        }
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert len(parts) == 6
    assert t.lilypond_format == "\\new Staff {\n\t{\n\t\t\\time 3/32\n\t\tc'16. [ ] ( )\n\t}\n\t{\n\t\t\\time 3/32\n\t\tc'32 [ (\n\t\td'16 ] )\n\t}\n\t{\n\t\t\\time 2/32\n\t\td'16 [ ] (\n\t}\n\t{\n\t\t\\time 1/32\n\t\te'32 [ ] )\n\t}\n\t{\n\t\t\\time 3/32\n\t\te'16. [ ] ( )\n\t}\n\t{\n\t\t\\time 3/32\n\t\tf'16. [ ] ( )\n\t}\n\t{\n\t\t\\time 1/32\n\t\tf'32 [ ] ( )\n\t}\n}"


def test_componenttools_split_components_by_prolated_durations_15():
    '''Cyclically duration partition list of leaves outside of score.
    '''

    notes = [Note("c'8"), Note("d'8"), Note("e'8"), Note("f'8")]
    durations = [Duration(3, 32)]
    parts = componenttools.split_components_by_prolated_durations(
        notes, durations, cyclic=True, fracture_spanners=True)

    assert len(parts) == 6

    t = Staff([])
    for part in parts:
        t.extend(part)

    r'''
    \new Staff {
        c'16.
        c'32
        d'16
        d'16
        e'32
        e'16.
        f'16.
        f'32
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert t.lilypond_format == "\\new Staff {\n\tc'16.\n\tc'32\n\td'16\n\td'16\n\te'32\n\te'16.\n\tf'16.\n\tf'32\n}"


def test_componenttools_split_components_by_prolated_durations_16():
    '''Cyclically duration partition list of measures outside of score.  Fracture spanners.
    '''

    measures = Measure((2, 8), notetools.make_repeated_notes(2)) * 2
    beamtools.BeamSpanner(measures[0])
    beamtools.BeamSpanner(measures[1])
    pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(measures)

    durations = [Duration(3, 32)]
    parts = componenttools.split_components_by_prolated_durations(
        measures, durations, cyclic=True, fracture_spanners=True)

    assert len(parts) == 6

    t = Staff([])
    for part in parts:
        t.extend(part)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 3/32
            c'16. [ ]
        }
        {
            \time 3/32
            c'32 [
            d'16 ]
        }
        {
            \time 2/32
            d'16 [ ]
        }
        {
            \time 1/32
            e'32 [ ]
        }
        {
            \time 3/32
            e'16. [ ]
        }
        {
            \time 3/32
            f'16. [ ]
        }
        {
            \time 1/32
            f'32 [ ]
        }
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert t.lilypond_format == "\\new Staff {\n\t{\n\t\t\\time 3/32\n\t\tc'16. [ ]\n\t}\n\t{\n\t\t\\time 3/32\n\t\tc'32 [\n\t\td'16 ]\n\t}\n\t{\n\t\t\\time 2/32\n\t\td'16 [ ]\n\t}\n\t{\n\t\t\\time 1/32\n\t\te'32 [ ]\n\t}\n\t{\n\t\t\\time 3/32\n\t\te'16. [ ]\n\t}\n\t{\n\t\t\\time 3/32\n\t\tf'16. [ ]\n\t}\n\t{\n\t\t\\time 1/32\n\t\tf'32 [ ]\n\t}\n}"


def test_componenttools_split_components_by_prolated_durations_17():
    '''Duration partition one leaf in score.
    Read durations cyclically in list.
    Fracture spanners but add tie after each split.
    '''

    t = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(t)
    beamtools.BeamSpanner(t[0])
    beamtools.BeamSpanner(t[1])
    spannertools.SlurSpanner(t.leaves)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 2/8
            c'8 [ (
            d'8 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    durations = [Duration(1, 32)]
    parts = componenttools.split_components_by_prolated_durations(
        t[0][1:], durations, cyclic=True, fracture_spanners=True, tie_after=True)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 2/8
            c'8 [ (
            d'32 ) ~
            d'32 ( ) ~
            d'32 ( ) ~
            d'32 ] (
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert len(parts) == 4
    assert t.lilypond_format == "\\new Staff {\n\t{\n\t\t\\time 2/8\n\t\tc'8 [ (\n\t\td'32 ) ~\n\t\td'32 ( ) ~\n\t\td'32 ( ) ~\n\t\td'32 ] (\n\t}\n\t{\n\t\t\\time 2/8\n\t\te'8 [\n\t\tf'8 ] )\n\t}\n}"


def test_componenttools_split_components_by_prolated_durations_18():
    '''Duration partition multiple leaves in score.
    Read durations cyclically in list.
    Fracture spanners but add tie after each split.
    '''

    t = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(t)
    beamtools.BeamSpanner(t[0])
    beamtools.BeamSpanner(t[1])
    spannertools.SlurSpanner(t.leaves)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 2/8
            c'8 [ (
            d'8 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    durations = [Duration(1, 16)]
    parts = componenttools.split_components_by_prolated_durations(
        t.leaves, durations, cyclic=True, fracture_spanners=True, tie_after=True)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 2/8
            c'16 ( ) [ ~
            c'16 (
            d'16 ) ~
            d'16 ] (
        }
        {
            \time 2/8
            e'16 ) [ ~
            e'16 (
            f'16 ) ~
            f'16 ] ( )
        }
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert len(parts) == 8
    assert t.lilypond_format == "\\new Staff {\n\t{\n\t\t\\time 2/8\n\t\tc'16 ( ) [ ~\n\t\tc'16 (\n\t\td'16 ) ~\n\t\td'16 ] (\n\t}\n\t{\n\t\t\\time 2/8\n\t\te'16 ) [ ~\n\t\te'16 (\n\t\tf'16 ) ~\n\t\tf'16 ] ( )\n\t}\n}"


def test_componenttools_split_components_by_prolated_durations_19():
    '''Duration partition one measure in score.
    Read durations cyclically in list.
    Fracture spanners but add tie after each split.
    '''

    t = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(t)
    beamtools.BeamSpanner(t[0])
    beamtools.BeamSpanner(t[1])
    spannertools.SlurSpanner(t.leaves)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 2/8
            c'8 [ (
            d'8 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    durations = [Duration(1, 16)]
    parts = componenttools.split_components_by_prolated_durations(
        t[:1], durations, cyclic=True, fracture_spanners=True, tie_after=True)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 1/16
            c'16 [ ] ( ) ~
        }
        {
            \time 1/16
            c'16 [ ] ( )
        }
        {
            \time 1/16
            d'16 [ ] ( ) ~
        }
        {
            \time 1/16
            d'16 [ ] (
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert len(parts) == 4
    assert t.lilypond_format == "\\new Staff {\n\t{\n\t\t\\time 1/16\n\t\tc'16 [ ] ( ) ~\n\t}\n\t{\n\t\t\\time 1/16\n\t\tc'16 [ ] ( )\n\t}\n\t{\n\t\t\\time 1/16\n\t\td'16 [ ] ( ) ~\n\t}\n\t{\n\t\t\\time 1/16\n\t\td'16 [ ] (\n\t}\n\t{\n\t\t\\time 2/8\n\t\te'8 [\n\t\tf'8 ] )\n\t}\n}"



def test_componenttools_split_components_by_prolated_durations_20():
    '''Duration partition multiple measures in score.
    Read durations cyclically in list.
    Fracture spanners but add tie after each split.
    '''

    t = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(t)
    beamtools.BeamSpanner(t[0])
    beamtools.BeamSpanner(t[1])
    spannertools.SlurSpanner(t.leaves)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 2/8
            c'8 [ (
            d'8 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    durations = [Duration(3, 32)]
    parts = componenttools.split_components_by_prolated_durations(
        t[:], durations, cyclic=True, fracture_spanners=True, tie_after=True)
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \time 3/32
            c'16. [ ] ( ) ~
        }
        {
            \time 3/32
            c'32 [ (
            d'16 ] ) ~
        }
        {
            \time 2/32
            d'16 [ ] (
        }
        {
            \time 1/32
            e'32 [ ] ) ~
        }
        {
            \time 3/32
            e'16. [ ] ( )
        }
        {
            \time 3/32
            f'16. [ ] ( ) ~
        }
        {
            \time 1/32
            f'32 [ ] ( )
        }
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert len(parts) == 6
    assert t.lilypond_format == "\\new Staff {\n\t{\n\t\t\\time 3/32\n\t\tc'16. [ ] ( ) ~\n\t}\n\t{\n\t\t\\time 3/32\n\t\tc'32 [ (\n\t\td'16 ] ) ~\n\t}\n\t{\n\t\t\\time 2/32\n\t\td'16 [ ] (\n\t}\n\t{\n\t\t\\time 1/32\n\t\te'32 [ ] ) ~\n\t}\n\t{\n\t\t\\time 3/32\n\t\te'16. [ ] ( )\n\t}\n\t{\n\t\t\\time 3/32\n\t\tf'16. [ ] ( ) ~\n\t}\n\t{\n\t\t\\time 1/32\n\t\tf'32 [ ] ( )\n\t}\n}"


def test_componenttools_split_components_by_prolated_durations_21():
    '''Duration partition one container in score
        Do no fracture spanners.'''

    t = Staff(Container(notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(t)
    beamtools.BeamSpanner(t[0])
    beamtools.BeamSpanner(t[1])
    spannertools.SlurSpanner(t.leaves)

    r'''
    \new Staff {
        {
            c'8 [ (
            d'8 ]
        }
        {
            e'8 [
            f'8 ] )
        }
    }
    '''

    durations = [Duration(1, 32), Duration(3, 32), Duration(5, 32)]
    parts = componenttools.split_components_by_prolated_durations(
        t[:1], durations, cyclic=False, fracture_spanners=False)

    r'''
    \new Staff {
        {
            c'32 [ (
        }
        {
            c'16.
        }
        {
            d'8 ]
        }
        {
            e'8 [
            f'8 ] )
        }
    }
    '''


    assert componenttools.is_well_formed_component(t)
    assert len(parts) == 3
    assert t.lilypond_format == "\\new Staff {\n\t{\n\t\tc'32 [ (\n\t}\n\t{\n\t\tc'16.\n\t}\n\t{\n\t\td'8 ]\n\t}\n\t{\n\t\te'8 [\n\t\tf'8 ] )\n\t}\n}"


def test_componenttools_split_components_by_prolated_durations_22():
    '''Duration partition multiple containers in score.
        Do not fracture spanners.'''

    t = Staff(Container(notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(t)
    beamtools.BeamSpanner(t[0])
    beamtools.BeamSpanner(t[1])
    spannertools.SlurSpanner(t.leaves)

    r'''
    \new Staff {
        {
            c'8 [ (
            d'8 ]
        }
        {
            e'8 [
            f'8 ] )
        }
    }
    '''

    durations = [Duration(1, 32), Duration(3, 32), Duration(5, 32)]
    parts = componenttools.split_components_by_prolated_durations(
        t[:], durations, cyclic=False, fracture_spanners=False)

    r'''
    \new Staff {
        {
            c'32 [ (
        }
        {
            c'16.
        }
        {
            d'8 ]
        }
        {
            e'32 [
        }
        {
            e'16.
            f'8 ] )
        }
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert len(parts) == 4
    assert t.lilypond_format == "\\new Staff {\n\t{\n\t\tc'32 [ (\n\t}\n\t{\n\t\tc'16.\n\t}\n\t{\n\t\td'8 ]\n\t}\n\t{\n\t\te'32 [\n\t}\n\t{\n\t\te'16.\n\t\tf'8 ] )\n\t}\n}"


def test_componenttools_split_components_by_prolated_durations_23():
    '''Duration partition one container in score, and fracture spanners.
    '''

    t = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(t)
    beamtools.BeamSpanner(t[0])
    beamtools.BeamSpanner(t[1])
    spannertools.SlurSpanner(t.leaves)

    r'''
    \new Staff {
        {
            \time 2/8
            c'8 [ (
            d'8 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    durations = [Duration(1, 32), Duration(3, 32), Duration(5, 32)]
    parts = componenttools.split_components_by_prolated_durations(
        t[:1], durations, cyclic=False, fracture_spanners=True)

    r'''
    \new Staff {
        {
            \time 1/32
            c'32 [ ] ( )
        }
        {
            \time 3/32
            c'16. [ ] ( )
        }
        {
            \time 4/32
            d'8 [ ] (
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert len(parts) == 3
    assert t.lilypond_format == "\\new Staff {\n\t{\n\t\t\\time 1/32\n\t\tc'32 [ ] ( )\n\t}\n\t{\n\t\t\\time 3/32\n\t\tc'16. [ ] ( )\n\t}\n\t{\n\t\t\\time 4/32\n\t\td'8 [ ] (\n\t}\n\t{\n\t\t\\time 2/8\n\t\te'8 [\n\t\tf'8 ] )\n\t}\n}"


def test_componenttools_split_components_by_prolated_durations_24():
    '''Duration partition multiple containers in score, and fracture spanners.
    '''

    t = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(t)
    beamtools.BeamSpanner(t[0])
    beamtools.BeamSpanner(t[1])
    spannertools.SlurSpanner(t.leaves)

    r'''
    \new Staff {
        {
            \time 2/8
            c'8 [ (
            d'8 ]
        }
        {
            \time 2/8
            e'8 [
            f'8 ] )
        }
    }
    '''

    durations = [Duration(1, 32), Duration(3, 32), Duration(5, 32)]
    parts = componenttools.split_components_by_prolated_durations(
        t[:], durations, cyclic=False, fracture_spanners=True)

    r'''
    \new Staff {
        {
            \time 1/32
            c'32 [ ] ( )
        }
        {
            \time 3/32
            c'16. [ ] ( )
        }
        {
            \time 4/32
            d'8 [ ] (
        }
        {
            \time 1/32
            e'32 [ ] )
        }
        {
            \time 7/32
            e'16. [ (
            f'8 ] )
        }
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert len(parts) == 4
    assert t.lilypond_format == "\\new Staff {\n\t{\n\t\t\\time 1/32\n\t\tc'32 [ ] ( )\n\t}\n\t{\n\t\t\\time 3/32\n\t\tc'16. [ ] ( )\n\t}\n\t{\n\t\t\\time 4/32\n\t\td'8 [ ] (\n\t}\n\t{\n\t\t\\time 1/32\n\t\te'32 [ ] )\n\t}\n\t{\n\t\t\\time 7/32\n\t\te'16. [ (\n\t\tf'8 ] )\n\t}\n}"


def test_componenttools_split_components_by_prolated_durations_25():
    '''Duration partition container outside of score.
    This example includes no spanners.
    Spanners do not apply outside of score.
    '''

    t = Container(notetools.make_repeated_notes(2)) * 2
    pitchtools.set_ascending_named_diatonic_pitches_on_nontied_pitched_components_in_expr(t)

    "[{c'8, d'8}, {e'8, f'8}]"

    durations = [Duration(1, 32), Duration(3, 32), Duration(5, 32)]
    parts = componenttools.split_components_by_prolated_durations(
        t, durations, cyclic=False, fracture_spanners=True)

    "[[{c'32}], [{c'16.}], [{d'8}, {e'32}], [{e'16., f'8}]]"

    assert len(parts) == 4


def test_componenttools_split_components_by_prolated_durations_26():
    '''Duration partition one leaf outside of score.
    '''

    t = Note("c'4")

    "c'4"

    durations = [Duration(1, 32), Duration(5, 32)]
    parts = componenttools.split_components_by_prolated_durations(
        [t], durations, cyclic=False, fracture_spanners=True)

    "[[Note(c', 32)], [Note(c', 8), Note(c', 32)], [Note(c', 16)]]"

    assert len(parts) == 3


def test_componenttools_split_components_by_prolated_durations_27():
    '''Duration partition leaf in score and fracture spanners.
    '''

    t = Staff([Note(0, (1, 8))])
    beamtools.BeamSpanner(t[0])

    r'''
    \new Staff {
        c'8 [ ]
    }
    '''

    durations = [Duration(1, 64), Duration(5, 64)]
    parts = componenttools.split_components_by_prolated_durations(
        t[:], durations, cyclic=False, fracture_spanners=True)

    r'''
    \new Staff {
        c'64 [ ]
        c'16 [ ~
        c'64 ]
        c'32 [ ]
    }
    '''

    assert componenttools.is_well_formed_component(t)
    assert t.lilypond_format == "\\new Staff {\n\tc'64 [ ]\n\tc'16 [ ~\n\tc'64 ]\n\tc'32 [ ]\n}"
