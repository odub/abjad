from abjad import *
from abjad.tools.lilypondparsertools._LilyPondSyntaxNode._LilyPondSyntaxNode import _LilyPondSyntaxNode as Node
from abjad.tools.lilypondparsertools._LilyPondLexicalDefinition._LilyPondLexicalDefinition import _LilyPondLexicalDefinition


class _LilyPondSyntacticalDefinition(object):

    def __init__(self, client):
        self.client = client

    tokens = _LilyPondLexicalDefinition.tokens

    ### SYNTACTICAL RULES ###

    def p_lilypond(self, p):
        '''lilypond : 
                    | lilypond toplevel_expression
                    | lilypond assignment
                    | lilypond error
                    | lilypond INVALID
        '''
        if len(p) == 1:
            p[0] = Node('lilypond', [ ])
        else:
            items = list(p[1].value)
            if p[2] is not None:
                items.append(p[2])
            p[0] = Node('lilypond', items)


    def p_toplevel_expression(self, p):
        '''toplevel_expression : lilypond_header
                               | book_block
                               | bookpart_block
                               | score_block
                               | composite_music
                               | full_markup
                               | full_markup_list
                               | output_def
        '''
        p[0] = Node('toplevel_expression', p[1:])


    def p_embedded_scm_bare(self, p):
        '''embedded_scm_bare : SCM_TOKEN
                             | SCM_IDENTIFIER
        '''
        p[0] = Node('embedded_scm_bare', p[1:])


    def p_embedded_scm(self, p):
        '''embedded_scm : embedded_scm_bare
                        | scm_function_call
        '''
        p[0] = Node('embedded_scm', p[1:])


    def p_scm_function_call(self, p):
        '''scm_function_call : SCM_FUNCTION function_arglist
        '''
        p[0] = Node('scm_function_call', p[1:])


    def p_embedded_lilypond(self, p):
        '''embedded_lilypond : 
                             | identifier_init
                             | music music music_list
                             | error
                             | INVALID embedded_lilypond
        '''
        p[0] = Node('embedded_lilypond', p[1:])


    def p_lilypond_header_body(self, p):
        '''lilypond_header_body : 
                                | lilypond_header_body assignment
        '''
        if len(p) == 1:
            p[0] = Node('lilypond_header_body', [ ])
        else:
            items = list(p[1].value)
            items.append(p[2])
            p[0] = Node('lilypond_header_body', items)


    def p_lilypond_header(self, p):
        '''lilypond_header : HEADER '{' lilypond_header_body '}'
        '''
        p[0] = Node('lilypond_header', p[1:])


    def p_assignment_id(self, p):
        '''assignment_id : STRING
                         | LYRICS_STRING
        '''
        p[0] = Node('assignment_id', p[1:])


    def p_assignment(self, p):
        '''assignment : assignment_id '=' identifier_init
                      | assignment_id property_path '=' identifier_init
                      | embedded_scm
        '''
        self.client.assignments[p[1].value[0]] = p[3].value[0]


    def p_identifier_init(self, p):
        '''identifier_init : score_block
                           | book_block
                           | bookpart_block
                           | output_def
                           | context_def_spec_block
                           | music
                           | post_event_nofinger
                           | number_expression
                           | string
                           | embedded_scm
                           | full_markup
                           | full_markup_list
                           | context_modification
        '''
        p[0] = Node('identifier_init', p[1:])


    def p_context_def_spec_block(self, p):
        '''context_def_spec_block : CONTEXT '{' context_def_spec_body '}'
        '''
        p[0] = Node('context_def_spec_block', p[1:])


    def p_context_def_spec_body(self, p):
        '''context_def_spec_body : 
                                 | CONTEXT_DEF_IDENTIFIER
                                 | context_def_spec_body GROBDESCRIPTIONS embedded_scm
                                 | context_def_spec_body context_mod
                                 | context_def_spec_body context_modification
        '''
        p[0] = Node('context_def_spec_body', p[1:])


    def p_book_block(self, p):
        '''book_block : BOOK '{' book_body '}'
        '''
        p[0] = Node('book_block', p[1:])


    def p_book_body(self, p):
        '''book_body : 
                     | BOOK_IDENTIFIER
                     | book_body paper_block
                     | book_body bookpart_block
                     | book_body score_block
                     | book_body composite_music
                     | book_body full_markup
                     | book_body full_markup_list
                     | book_body lilypond_header
                     | book_body embedded_scm
                     | book_body error
        '''
        p[0] = Node('book_body', p[1:])


    def p_bookpart_block(self, p):
        '''bookpart_block : BOOKPART '{' bookpart_body '}'
        '''
        p[0] = Node('bookpart_block', p[1:])


    def p_bookpart_body(self, p):
        '''bookpart_body : 
                         | BOOK_IDENTIFIER
                         | bookpart_body paper_block
                         | bookpart_body score_block
                         | bookpart_body composite_music
                         | bookpart_body full_markup
                         | bookpart_body full_markup_list
                         | bookpart_body lilypond_header
                         | bookpart_body embedded_scm
                         | bookpart_body error
        '''
        p[0] = Node('bookpart_body', p[1:])


    def p_score_block(self, p):
        '''score_block : SCORE '{' score_body '}'
        '''
        p[0] = Node('score_block', p[1:])


    def p_score_body(self, p):
        '''score_body : music
                      | SCORE_IDENTIFIER
                      | score_body lilypond_header
                      | score_body output_def
                      | score_body error
        '''
        p[0] = Node('score_body', p[1:])


    def p_paper_block(self, p):
        '''paper_block : output_def
        '''
        p[0] = Node('paper_block', p[1:])


    def p_output_def(self, p):
        '''output_def : output_def_body '}'
        '''
        p[0] = Node('output_def', p[1:])


    def p_output_def_head(self, p):
        '''output_def_head : PAPER
                           | MIDI
                           | LAYOUT
        '''
        p[0] = Node('output_def_head', p[1:])


    def p_output_def_head_with_mode_switch(self, p):
        '''output_def_head_with_mode_switch : output_def_head
        '''
        p[0] = Node('output_def_head_with_mode_switch', p[1:])


    def p_output_def_body(self, p):
        '''output_def_body : output_def_head_with_mode_switch '{'
                           | output_def_head_with_mode_switch '{' OUTPUT_DEF_IDENTIFIER
                           | output_def_body assignment
                           | output_def_body context_def_spec_block
                           | output_def_body error
        '''
        p[0] = Node('output_def_body', p[1:])


    def p_tempo_event(self, p):
        '''tempo_event : TEMPO steno_duration '=' tempo_range
                       | TEMPO scalar_closed steno_duration '=' tempo_range
                       | TEMPO scalar
        '''
        p[0] = Node('tempo_event', p[1:])


    def p_music_list(self, p):
        '''music_list : 
                      | music_list music
                      | music_list embedded_scm
                      | music_list error
        '''
        if len(p) == 1:
            p[0] = Node('music_list', [ ])
        else:
            items = list(p[1].value)
            items.append(p[2])
            p[0] = Node('music_list', items)


    def p_braced_music_list(self, p):
        '''braced_music_list : '{' music_list '}'
        '''
        p[0] = Node('braced_music_list', p[1:])


    def p_music(self, p):
        '''music : simple_music
                 | composite_music
        '''
        p[0] = Node('music', p[1:])


    def p_repeated_music(self, p):
        '''repeated_music : REPEAT simple_string unsigned_number music
                          | REPEAT simple_string unsigned_number music ALTERNATIVE braced_music_list
        '''
        p[0] = Node('repeated_music', p[1:])


    def p_sequential_music(self, p):
        '''sequential_music : SEQUENTIAL braced_music_list
                            | braced_music_list
        '''
        p[0] = Node('sequential_music', p[1:])


    def p_simultaneous_music(self, p):
        '''simultaneous_music : SIMULTANEOUS braced_music_list
                              | DOUBLE_ANGLE_OPEN music_list DOUBLE_ANGLE_CLOSE
        '''
        p[0] = Node('simultaneous_music', p[1:])


    def p_simple_music(self, p):
        '''simple_music : event_chord
                        | music_property_def
                        | context_change
        '''
        p[0] = Node('simple_music', p[1:])


    def p_context_modification(self, p):
        '''context_modification : WITH '{' context_mod_list '}'
                                | WITH CONTEXT_MOD_IDENTIFIER
                                | CONTEXT_MOD_IDENTIFIER
        '''
        p[0] = Node('context_modification', p[1:])
        p.lexer.pop_state( )


    def p_optional_context_mod(self, p):
        '''optional_context_mod : 
                                | context_modification
        '''
        p[0] = Node('optional_context_mod', p[1:])


    def p_context_mod_list(self, p):
        '''context_mod_list : 
                            | context_mod_list context_mod
                            | context_mod_list CONTEXT_MOD_IDENTIFIER
        '''
        p[0] = Node('context_mod_list', p[1:])


    def p_composite_music(self, p):
        '''composite_music : complex_music
                           | closed_music
        '''
        p[0] = Node('composite_music', p[1:])


    def p_closed_music(self, p):
        '''closed_music : mode_changed_music
                        | MUSIC_IDENTIFIER
                        | grouped_music_list
        '''
        if type(p[1]) == str:
            id = p[1][1:]
            p[0] = Node('closed_music', [self.client.assignments[id]])
        else:
            p[0] = Node('closed_music', p[1:])


    def p_grouped_music_list(self, p):
        '''grouped_music_list : simultaneous_music
                              | sequential_music
        '''
        p[0] = Node('grouped_music_list', p[1:])


    def p_function_arglist(self, p):
        '''function_arglist : function_arglist_bare
                            | EXPECT_MUSIC function_arglist_optional music
                            | EXPECT_SCM function_arglist_optional embedded_scm
        '''
        p[0] = Node('function_arglist', p[1:])


    def p_function_arglist_optional(self, p):
        '''function_arglist_optional : function_arglist_keep
                                     | EXPECT_OPTIONAL EXPECT_MUSIC function_arglist_optional
                                     | EXPECT_OPTIONAL EXPECT_PITCH function_arglist_optional
                                     | EXPECT_OPTIONAL EXPECT_DURATION function_arglist_optional
                                     | EXPECT_OPTIONAL EXPECT_MARKUP function_arglist_optional
                                     | EXPECT_OPTIONAL EXPECT_SCM function_arglist_optional
        '''
        p[0] = Node('function_arglist_optional', p[1:])


    def p_function_arglist_keep(self, p):
        '''function_arglist_keep : EXPECT_OPTIONAL EXPECT_MARKUP function_arglist_keep full_markup
                                 | EXPECT_OPTIONAL EXPECT_MARKUP function_arglist_keep simple_string
                                 | EXPECT_OPTIONAL EXPECT_PITCH function_arglist_keep pitch_also_in_chords
                                 | EXPECT_OPTIONAL EXPECT_DURATION function_arglist_closed_keep duration_length
                                 | EXPECT_OPTIONAL EXPECT_SCM function_arglist_keep simple_string
                                 | EXPECT_OPTIONAL EXPECT_MUSIC function_arglist_keep closed_music
                                 | EXPECT_OPTIONAL EXPECT_SCM function_arglist_keep embedded_scm
                                 | function_arglist
        '''
        p[0] = Node('function_arglist_keep', p[1:])


    def p_function_arglist_closed(self, p):
        '''function_arglist_closed : function_arglist_bare
                                   | EXPECT_MUSIC function_arglist_optional closed_music
                                   | EXPECT_SCM function_arglist_optional embedded_scm_closed
        '''
        p[0] = Node('function_arglist_closed', p[1:])


    def p_function_arglist_closed_optional(self, p):
        '''function_arglist_closed_optional : function_arglist_closed_keep
                                            | EXPECT_OPTIONAL EXPECT_MUSIC function_arglist_closed_optional
                                            | EXPECT_OPTIONAL EXPECT_PITCH function_arglist_closed_optional
                                            | EXPECT_OPTIONAL EXPECT_DURATION function_arglist_closed_optional
                                            | EXPECT_OPTIONAL EXPECT_MARKUP function_arglist_closed_optional
                                            | EXPECT_OPTIONAL EXPECT_SCM function_arglist_closed_optional
        '''
        p[0] = Node('function_arglist_closed_optional', p[1:])


    def p_function_arglist_closed_keep(self, p):
        '''function_arglist_closed_keep : EXPECT_OPTIONAL EXPECT_MARKUP function_arglist_keep full_markup
                                        | EXPECT_OPTIONAL EXPECT_MARKUP function_arglist_keep simple_string
                                        | EXPECT_OPTIONAL EXPECT_PITCH function_arglist_keep pitch_also_in_chords
                                        | EXPECT_OPTIONAL EXPECT_DURATION function_arglist_closed_keep duration_length
                                        | EXPECT_OPTIONAL EXPECT_SCM function_arglist_keep simple_string
                                        | EXPECT_OPTIONAL EXPECT_MUSIC function_arglist_keep closed_music
                                        | EXPECT_OPTIONAL EXPECT_SCM function_arglist_keep embedded_scm_closed
                                        | function_arglist_closed
        '''
        p[0] = Node('function_arglist_closed_keep', p[1:])


    def p_embedded_scm_closed(self, p):
        '''embedded_scm_closed : embedded_scm_bare
                               | scm_function_call_closed
        '''
        p[0] = Node('embedded_scm_closed', p[1:])


    def p_scm_function_call_closed(self, p):
        '''scm_function_call_closed : SCM_FUNCTION function_arglist_closed
        '''
        p[0] = Node('scm_function_call_closed', p[1:])


    def p_function_arglist_bare(self, p):
        '''function_arglist_bare : EXPECT_NO_MORE_ARGS
                                 | EXPECT_MARKUP function_arglist_optional full_markup
                                 | EXPECT_MARKUP function_arglist_optional simple_string
                                 | EXPECT_PITCH function_arglist_optional pitch_also_in_chords
                                 | EXPECT_DURATION function_arglist_closed_optional duration_length
                                 | EXPECT_SCM function_arglist_optional simple_string
        '''
        p[0] = Node('function_arglist_bare', p[1:])


    def p_music_function_call(self, p):
        '''music_function_call : MUSIC_FUNCTION function_arglist
        '''
        p[0] = Node('music_function_call', p[1:])


    def p_optional_id(self, p):
        '''optional_id : 
                       | '=' simple_string
        '''
        p[0] = Node('optional_id', p[1:])


    def p_complex_music(self, p):
        '''complex_music : music_function_call
                         | CONTEXT simple_string optional_id optional_context_mod music
                         | NEWCONTEXT simple_string optional_id optional_context_mod music
                         | TIMES fraction music
                         | repeated_music
                         | re_rhythmed_music
        '''
        p[0] = Node('complex_music', p[1:])


    def p_mode_changed_music(self, p):
        '''mode_changed_music : mode_changing_head grouped_music_list
                              | mode_changing_head_with_context optional_context_mod grouped_music_list
        '''
        p[0] = Node('mode_changed_music', p[1:])


    def p_mode_changing_head(self, p):
        '''mode_changing_head : NOTEMODE
                              | DRUMMODE
                              | FIGUREMODE
                              | CHORDMODE
                              | LYRICMODE
        '''
        p[0] = Node('mode_changing_head', p[1:])


    def p_mode_changing_head_with_context(self, p):
        '''mode_changing_head_with_context : DRUMS
                                           | FIGURES
                                           | CHORDS
                                           | LYRICS
        '''
        p[0] = Node('mode_changing_head_with_context', p[1:])


    def p_new_lyrics(self, p):
        '''new_lyrics : ADDLYRICS closed_music
                      | new_lyrics ADDLYRICS closed_music
        '''
        p[0] = Node('new_lyrics', p[1:])


    def p_re_rhythmed_music(self, p):
        '''re_rhythmed_music : closed_music new_lyrics
                             | LYRICSTO simple_string music
        '''
        p[0] = Node('re_rhythmed_music', p[1:])


    def p_context_change(self, p):
        '''context_change : CHANGE STRING '=' STRING
        '''
        p[0] = Node('context_change', p[1:])


    def p_property_path_revved(self, p):
        '''property_path_revved : embedded_scm_closed
                                | property_path_revved embedded_scm_closed
        '''
        if len(p) == 2:
            p[0] = Node('property_path_revved', [p[1]])
        else:
            items = list(p[1].value)
            items.append(p[2])
            p[0] = Node('property_path_revved', items)



    def p_property_path(self, p):
        '''property_path : property_path_revved
        '''
        p[0] = Node('property_path', p[1].value)


    def p_property_operation(self, p):
        '''property_operation : STRING '=' scalar
                              | UNSET simple_string
                              | OVERRIDE simple_string property_path '=' scalar
                              | REVERT simple_string embedded_scm
        '''
        p[0] = Node('property_operation', p[1:])


    def p_context_def_mod(self, p):
        '''context_def_mod : CONSISTS
                           | REMOVE
                           | ACCEPTS
                           | DEFAULTCHILD
                           | DENIES
                           | ALIAS
                           | TYPE
                           | DESCRIPTION
                           | NAME
        '''
        p[0] = Node('context_def_mod', p[1:])


    def p_context_mod(self, p):
        '''context_mod : property_operation
                       | context_def_mod STRING
                       | context_def_mod embedded_scm
        '''
        p[0] = Node('context_mod', p[1:])


    def p_context_prop_spec(self, p):
        '''context_prop_spec : simple_string
                             | simple_string '.' simple_string
        '''
        p[0] = Node('context_prop_spec', p[1:])


    def p_simple_music_property_def(self, p):
        '''simple_music_property_def : OVERRIDE context_prop_spec property_path '=' scalar
                                     | REVERT context_prop_spec embedded_scm
                                     | SET context_prop_spec '=' scalar
                                     | UNSET context_prop_spec
        '''
        p[0] = Node('simple_music_property_def', p[1:])


    def p_music_property_def(self, p):
        '''music_property_def : simple_music_property_def
                              | ONCE simple_music_property_def
        '''
        p[0] = Node('music_property_def', p[1:])


    def p_string(self, p):
        '''string : STRING
                  | STRING_IDENTIFIER
                  | string '+' string
        '''
        p[0] = Node('string', p[1:])


    def p_simple_string(self, p):
        '''simple_string : STRING
                         | LYRICS_STRING
                         | STRING_IDENTIFIER
        '''
        p[0] = Node('simple_string', p[1:])


    def p_scalar_bare(self, p):
        '''scalar_bare : string
                       | lyric_element
                       | bare_number
                       | embedded_scm_bare
                       | full_markup
        '''
        p[0] = Node('scalar_bare', p[1:])


    def p_scalar(self, p):
        '''scalar : scalar_bare
                  | scm_function_call
        '''
        p[0] = Node('scalar', p[1:])


    def p_scalar_closed(self, p):
        '''scalar_closed : scalar_bare
                         | scm_function_call_closed
        '''
        p[0] = Node('scalar_closed', p[1:])


    def p_event_chord(self, p):
        '''event_chord : simple_chord_elements post_events
                       | CHORD_REPETITION optional_notemode_duration post_events
                       | MULTI_MEASURE_REST optional_notemode_duration post_events
                       | command_element
                       | note_chord_element
        '''
        p[0] = Node('event_chord', p[1:])


    def p_note_chord_element(self, p):
        '''note_chord_element : chord_body optional_notemode_duration post_events
        '''
        p[0] = Node('note_chord_element', p[1:])


    def p_chord_body(self, p):
        '''chord_body : ANGLE_OPEN chord_body_elements ANGLE_CLOSE
        '''
        p[0] = Node('chord_body', p[1:])


    def p_chord_body_elements(self, p):
        '''chord_body_elements : 
                               | chord_body_elements chord_body_element
        '''
        p[0] = Node('chord_body_elements', p[1:])


    def p_chord_body_element(self, p):
        '''chord_body_element : pitch exclamations questions octave_check post_events
                              | DRUM_PITCH post_events
                              | music_function_chord_body
        '''
        p[0] = Node('chord_body_element', p[1:])


    def p_music_function_chord_body_arglist(self, p):
        '''music_function_chord_body_arglist : function_arglist_bare
                                             | EXPECT_MUSIC music_function_chord_body_arglist chord_body_element
                                             | EXPECT_SCM function_arglist_optional embedded_scm_chord_body
        '''
        p[0] = Node('music_function_chord_body_arglist', p[1:])


    def p_embedded_scm_chord_body(self, p):
        '''embedded_scm_chord_body : embedded_scm_bare
                                   | SCM_FUNCTION music_function_chord_body_arglist
        '''
        p[0] = Node('embedded_scm_chord_body', p[1:])


    def p_music_function_chord_body(self, p):
        '''music_function_chord_body : MUSIC_FUNCTION music_function_chord_body_arglist
        '''
        p[0] = Node('music_function_chord_body', p[1:])


    def p_music_function_event_arglist(self, p):
        '''music_function_event_arglist : function_arglist_bare
                                        | EXPECT_MUSIC music_function_event_arglist post_event
                                        | EXPECT_SCM function_arglist_optional embedded_scm_event
        '''
        p[0] = Node('music_function_event_arglist', p[1:])


    def p_embedded_scm_event(self, p):
        '''embedded_scm_event : embedded_scm_bare
                              | SCM_FUNCTION music_function_event_arglist
        '''
        p[0] = Node('embedded_scm_event', p[1:])


    def p_music_function_event(self, p):
        '''music_function_event : MUSIC_FUNCTION music_function_event_arglist
        '''
        p[0] = Node('music_function_event', p[1:])


    def p_event_function_event(self, p):
        '''event_function_event : EVENT_FUNCTION music_function_event_arglist
        '''
        p[0] = Node('event_function_event', p[1:])


    def p_command_element(self, p):
        '''command_element : command_event
                           | E_BRACKET_OPEN
                           | E_BRACKET_CLOSE
                           | E_BACKSLASH
                           | '|'
                           | TIME_T fraction
                           | MARK scalar
        '''
        p[0] = Node('command_element', p[1:])


    def p_command_event(self, p):
        '''command_event : E_TILDE
                         | MARK DEFAULT
                         | tempo_event
                         | KEY DEFAULT
                         | KEY NOTENAME_PITCH SCM_IDENTIFIER
        '''
        p[0] = Node('command_event', p[1:])


    def p_post_events(self, p):
        '''post_events : 
                       | post_events post_event
        '''
        if len(p) == 1:
            p[0] = Node('post_events', [ ])
        else:
            items = list(p[1].value)
            items.append(p[2])
            p[0] = Node('post_events', items)



    def p_post_event_nofinger(self, p):
        '''post_event_nofinger : direction_less_event
                               | script_dir music_function_event
                               | HYPHEN
                               | EXTENDER
                               | script_dir direction_reqd_event
                               | script_dir direction_less_event
                               | string_number_event
        '''
        p[0] = Node('post_event_nofinger', p[1:])


    def p_post_event(self, p):
        '''post_event : post_event_nofinger
                      | script_dir fingering
        '''
        p[0] = Node('post_event', p[1:])


    def p_string_number_event(self, p):
        '''string_number_event : E_UNSIGNED
        '''
        p[0] = Node('string_number_event', p[1:])


    def p_direction_less_char(self, p):
        '''direction_less_char : '['
                               | ']'
                               | '~'
                               | '('
                               | ')'
                               | E_EXCLAMATION
                               | E_OPEN
                               | E_CLOSE
                               | E_ANGLE_CLOSE
                               | E_ANGLE_OPEN
        '''
        p[0] = Node('direction_less_char', p[1:])


    def p_direction_less_event(self, p):
        '''direction_less_event : direction_less_char
                                | EVENT_IDENTIFIER
                                | tremolo_type
                                | event_function_event
        '''
        p[0] = Node('direction_less_event', p[1:])


    def p_direction_reqd_event(self, p):
        '''direction_reqd_event : gen_text_def
                                | script_abbreviation
        '''
        p[0] = Node('direction_reqd_event', p[1:])


    def p_octave_check(self, p):
        '''octave_check : 
                        | '='
                        | '=' sub_quotes
                        | '=' sup_quotes
        '''
        p[0] = Node('octave_check', p[1:])


    def p_sup_quotes(self, p):
        '''sup_quotes : "'"
                      | sup_quotes "'"
        '''
        if len(p) == 2:
            p[0] = Node('sup_quotes', 1)
        else:
            p[0] = Node('sup_quotes', p[1].value + 1)


    def p_sub_quotes(self, p):
        '''sub_quotes : ','
                      | sub_quotes ','
        '''
        if len(p) == 2:
            p[0] = Node('sub_quotes', 1)
        else:
            p[0] = Node('sub_quotes', p[1].value + 1)


    def p_steno_pitch(self, p):
        '''steno_pitch : NOTENAME_PITCH
                       | NOTENAME_PITCH sup_quotes
                       | NOTENAME_PITCH sub_quotes
        '''
        p[0] = Node('steno_pitch', p[1:])


    def p_steno_tonic_pitch(self, p):
        '''steno_tonic_pitch : TONICNAME_PITCH
                             | TONICNAME_PITCH sup_quotes
                             | TONICNAME_PITCH sub_quotes
        '''
        p[0] = Node('steno_tonic_pitch', p[1:])


    def p_pitch(self, p):
        '''pitch : steno_pitch
                 | PITCH_IDENTIFIER
        '''
        p[0] = Node('pitch', p[1:])


    def p_pitch_also_in_chords(self, p):
        '''pitch_also_in_chords : pitch
                                | steno_tonic_pitch
        '''
        p[0] = Node('pitch_also_in_chords', p[1:])


    def p_gen_text_def(self, p):
        '''gen_text_def : full_markup
                        | string
        '''
        p[0] = Node('gen_text_def', p[1:])


    def p_fingering(self, p):
        '''fingering : UNSIGNED
        '''
        p[0] = Node('fingering', p[1:])


    def p_script_abbreviation(self, p):
        '''script_abbreviation : '^'
                               | '+'
                               | '-'
                               | '|'
                               | ">"
                               | '.'
                               | '_'
        '''
        p[0] = Node('script_abbreviation', p[1:])


    def p_script_dir(self, p):
        '''script_dir : '_'
                      | '^'
                      | '-'
        '''
        p[0] = Node('script_dir', p[1:])


    def p_duration_length(self, p):
        '''duration_length : multiplied_duration
        '''
        p[0] = Node('duration_length', p[1:])


    def p_optional_notemode_duration(self, p):
        '''optional_notemode_duration : 
                                      | multiplied_duration
        '''
        p[0] = Node('optional_notemode_duration', p[1:])


    def p_steno_duration(self, p):
        '''steno_duration : bare_unsigned dots
                          | DURATION_IDENTIFIER dots
        '''
        p[0] = Node('steno_duration', p[1:])


    def p_multiplied_duration(self, p):
        '''multiplied_duration : steno_duration
                               | multiplied_duration '*' bare_unsigned
                               | multiplied_duration '*' FRACTION
        '''
        p[0] = Node('multiplied_duration', p[1:])


    def p_fraction(self, p):
        '''fraction : FRACTION
                    | UNSIGNED '/' UNSIGNED
        '''
        p[0] = Node('fraction', p[1:])


    def p_dots(self, p):
        '''dots : 
                | dots '.'
        '''
        if len(p) == 1:
            p[0] = Node('dots', 0)
        else:
            p[0] = Node('dots', p[1].value + 1)


    def p_tremolo_type(self, p):
        '''tremolo_type : ':'
                        | ':' bare_unsigned
        '''
        p[0] = Node('tremolo_type', p[1:])


    def p_bass_number(self, p):
        '''bass_number : UNSIGNED
                       | STRING
                       | full_markup
        '''
        p[0] = Node('bass_number', p[1:])


    def p_figured_bass_alteration(self, p):
        '''figured_bass_alteration : '-'
                                   | '+'
                                   | '!'
        '''
        p[0] = Node('figured_bass_alteration', p[1:])


    def p_bass_figure(self, p):
        '''bass_figure : "_"
                       | bass_number
                       | bass_figure ']'
                       | bass_figure figured_bass_alteration
                       | bass_figure figured_bass_modification
        '''
        p[0] = Node('bass_figure', p[1:])


    def p_figured_bass_modification(self, p):
        '''figured_bass_modification : E_PLUS
                                     | E_EXCLAMATION
                                     | '/'
                                     | E_BACKSLASH
        '''
        p[0] = Node('figured_bass_modification', p[1:])


    def p_br_bass_figure(self, p):
        '''br_bass_figure : bass_figure
                          | '[' bass_figure
        '''
        p[0] = Node('br_bass_figure', p[1:])


    def p_figure_list(self, p):
        '''figure_list : 
                       | figure_list br_bass_figure
        '''
        p[0] = Node('figure_list', p[1:])


    def p_figure_spec(self, p):
        '''figure_spec : FIGURE_OPEN figure_list FIGURE_CLOSE
        '''
        p[0] = Node('figure_spec', p[1:])


    def p_optional_rest(self, p):
        '''optional_rest : 
                         | REST
        '''
        p[0] = Node('optional_rest', p[1:])


    def p_simple_element(self, p):
        '''simple_element : pitch exclamations questions octave_check optional_notemode_duration optional_rest
                          | DRUM_PITCH optional_notemode_duration
                          | RESTNAME optional_notemode_duration
                          | lyric_element optional_notemode_duration
        '''
        p[0] = Node('simple_element', p[1:])


    def p_simple_chord_elements(self, p):
        '''simple_chord_elements : simple_element
                                 | new_chord
                                 | figure_spec optional_notemode_duration
        '''
        p[0] = Node('simple_chord_elements', p[1:])


    def p_lyric_element(self, p):
        '''lyric_element : lyric_markup
                         | LYRICS_STRING
        '''
        p[0] = Node('lyric_element', p[1:])


    def p_new_chord(self, p):
        '''new_chord : steno_tonic_pitch optional_notemode_duration
                     | steno_tonic_pitch optional_notemode_duration chord_separator chord_items
        '''
        p[0] = Node('new_chord', p[1:])


    def p_chord_items(self, p):
        '''chord_items : 
                       | chord_items chord_item
        '''
        p[0] = Node('chord_items', p[1:])


    def p_chord_separator(self, p):
        '''chord_separator : CHORD_COLON
                           | CHORD_CARET
                           | CHORD_SLASH steno_tonic_pitch
                           | CHORD_BASS steno_tonic_pitch
        '''
        p[0] = Node('chord_separator', p[1:])


    def p_chord_item(self, p):
        '''chord_item : chord_separator
                      | step_numbers
                      | CHORD_MODIFIER
        '''
        p[0] = Node('chord_item', p[1:])


    def p_step_numbers(self, p):
        '''step_numbers : step_number
                        | step_numbers '.' step_number
        '''
        p[0] = Node('step_numbers', p[1:])


    def p_step_number(self, p):
        '''step_number : bare_unsigned
                       | bare_unsigned '+'
                       | bare_unsigned "-"
        '''
        p[0] = Node('step_number', p[1:])


    def p_tempo_range(self, p):
        '''tempo_range : bare_unsigned
                       | bare_unsigned '~' bare_unsigned
        '''
        p[0] = Node('tempo_range', p[1:])


    def p_number_expression(self, p):
        '''number_expression : number_expression '+' number_term
                             | number_expression '-' number_term
                             | number_term
        '''
        if len(p) == 2:
            p[0] = Node('number_expression', p[1])
        elif p[2] == '+':
            p[0] = Node('number_expression', p[1].value + p[3])
        else:
            p[0] = Node('number_expression', p[1].value - p[3])


    def p_number_term(self, p):
        '''number_term : number_factor
                       | number_factor '*' number_factor
                       | number_factor '/' number_factor
        '''
        if len(p) == 2:
            p[0] = p[1]
        elif p[2] == '*':
            p[0] = p[1] * p[3]
        else:
            p[0] = p[1] / p[3]


    def p_number_factor(self, p):
        '''number_factor : '-' number_factor
                         | bare_number
        '''
        if p[1] == '-':
            p[0] = p[2] * -1.
        else:
            p[0] = p[1]


    def p_bare_number(self, p):
#        '''bare_number : UNSIGNED
#                       | REAL
#                       | NUMBER_IDENTIFIER
#                       | REAL NUMBER_IDENTIFIER
#                       | UNSIGNED NUMBER_IDENTIFIER
#        '''
        '''bare_number : UNSIGNED
                       | REAL
                       | NUMBER_IDENTIFIER
        '''
        p[0] = p[1]


    def p_bare_unsigned(self, p):
        '''bare_unsigned : UNSIGNED
        '''
        p[0] = p[1]


    def p_unsigned_number(self, p):
        '''unsigned_number : bare_unsigned
                           | NUMBER_IDENTIFIER
        '''
        if hasattr(p[1], 'value'):
            p[0] = self.client.assignments[p[1].value[1:]]
        else:
            p[0] = p[1]


    def p_exclamations(self, p):
        '''exclamations : 
                        | exclamations '!'
        '''
        if len(p) == 1:
            p[0] = Node('exclamations', 0)
        else:
            p[0] = Node('exclamations', p[1].value + 1)


    def p_questions(self, p):
        '''questions : 
                     | questions '?'
        '''
        if len(p) == 1:
            p[0] = Node('questions', 0)
        else:
            p[0] = Node('questions', p[1].value + 1)


    def p_lyric_markup(self, p):
        '''lyric_markup : LYRIC_MARKUP_IDENTIFIER
                        | LYRIC_MARKUP markup_top
        '''
        p[0] = Node('lyric_markup', p[1:])


    def p_full_markup_list(self, p):
        '''full_markup_list : MARKUPLINES_IDENTIFIER
                            | MARKUPLINES markup_list
        '''
        p[0] = Node('full_markup_list', p[1:])


    def p_full_markup(self, p):
        '''full_markup : MARKUP_IDENTIFIER
                       | MARKUP markup_top
        '''
        p[0] = Node('full_markup', p[1:])


    def p_markup_top(self, p):
        '''markup_top : markup_list
                      | markup_head_1_list simple_markup
                      | simple_markup
        '''
        p[0] = Node('markup_top', p[1:])


    def p_markup_list(self, p):
        '''markup_list : MARKUPLINES_IDENTIFIER
                       | markup_composed_list
                       | markup_braced_list
                       | markup_command_list
        '''
        p[0] = Node('markup_list', p[1:])


    def p_markup_composed_list(self, p):
        '''markup_composed_list : markup_head_1_list markup_braced_list
        '''
        p[0] = Node('markup_composed_list', p[1:])


    def p_markup_braced_list(self, p):
        '''markup_braced_list : '{' markup_braced_list_body '}'
        '''
        p[0] = Node('markup_braced_list', p[1:])


    def p_markup_braced_list_body(self, p):
        '''markup_braced_list_body : 
                                   | markup_braced_list_body markup
                                   | markup_braced_list_body markup_list
        '''
        p[0] = Node('markup_braced_list_body', p[1:])


    def p_markup_command_list(self, p):
        '''markup_command_list : MARKUP_LIST_FUNCTION markup_command_list_arguments
        '''
        p[0] = Node('markup_command_list', p[1:])


    def p_markup_command_basic_arguments(self, p):
        '''markup_command_basic_arguments : EXPECT_MARKUP_LIST markup_command_list_arguments markup_list
                                          | EXPECT_SCM markup_command_list_arguments embedded_scm_closed
                                          | EXPECT_NO_MORE_ARGS
        '''
        p[0] = Node('markup_command_basic_arguments', p[1:])


    def p_markup_command_list_arguments(self, p):
        '''markup_command_list_arguments : markup_command_basic_arguments
                                         | EXPECT_MARKUP markup_command_list_arguments markup
        '''
        p[0] = Node('markup_command_list_arguments', p[1:])


    def p_markup_head_1_item(self, p):
        '''markup_head_1_item : MARKUP_FUNCTION EXPECT_MARKUP markup_command_list_arguments
        '''
        p[0] = Node('markup_head_1_item', p[1:])


    def p_markup_head_1_list(self, p):
        '''markup_head_1_list : markup_head_1_item
                              | markup_head_1_list markup_head_1_item
        '''
        p[0] = Node('markup_head_1_list', p[1:])


    def p_simple_markup(self, p):
        '''simple_markup : STRING
                         | MARKUP_IDENTIFIER
                         | LYRIC_MARKUP_IDENTIFIER
                         | STRING_IDENTIFIER
                         | SCORE '{' score_body '}'
                         | MARKUP_FUNCTION markup_command_basic_arguments
        '''
        p[0] = Node('simple_markup', p[1:])


    def p_markup(self, p):
        '''markup : markup_head_1_list simple_markup
                  | simple_markup
        '''
        p[0] = Node('markup', p[1:])

    ### NON-LILYPOND-DERIVED SCHEME PARSING ###

    def p_scheme_string(self, p):
        '''string : SCHEME_START string'''
        p[0] = Node('string', p[1:])
        p.lexer.pop_state( )

    def p_scheme_number(self, p):
        '''bare_number : SCHEME_START bare_number'''
        p[0] = p[2]
        p.lexer.pop_state( )
