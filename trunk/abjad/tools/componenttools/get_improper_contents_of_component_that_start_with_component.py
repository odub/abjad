def get_improper_contents_of_component_that_start_with_component(component):
    r'''.. versionadded:: 2.9

    Get improper contents of `component` that start with `component`::

        abjad> staff = Staff(r"c' << \new Voice { d' } \new Voice { e' } >> f'")

    ::

        abjad> f(staff)
        \new Staff {
            c'4
            <<
                \new Voice {
                    d'4
                }
                \new Voice {
                    e'4
                }
            >>
            f'4
        }

    ::

        abjad> componenttools.get_improper_contents_of_component_that_start_with_component(staff[1])
        [<<Voice{1}, Voice{1}>>, Voice{1}, Note("d'4"), Voice{1}, Note("e'4")]

    Return list of `component` together with improper contents that start with component.
    '''
    from abjad.tools.containertools.Container import Container

    # initialize result
    result = []

    # add component
    result.append(component)

    # add content components that start with component
    if isinstance(component, Container):
        if component.is_parallel:
            for x in component:
                result.extend(get_improper_contents_of_component_that_start_with_component(x))
        elif component:
            result.extend(get_improper_contents_of_component_that_start_with_component(component[0]))

    # return result
    return result
