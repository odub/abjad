# -*- encoding: utf-8 -*-
import collections
from abjad.tools.abctools.AbjadValueObject import AbjadValueObject


class NonreducedRatio(AbjadValueObject):
    '''Nonreduced ratio.

    ..  container:: example

        **Example 1.** Nonreduced ratio of two numbers:

        ::

            >>> mathtools.NonreducedRatio((2, 4))
            NonreducedRatio((2, 4))

    ..  container:: example

        **Example 2.** Nonreduced ratio of three numbers:

            >>> mathtools.NonreducedRatio((2, 4, 2))
            NonreducedRatio((2, 4, 2))

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_numbers',
        )

    ### INITIALIZER ###

    def __init__(self, numbers=(1, 1)):
        if isinstance(numbers, type(self)):
            numbers = numbers.numbers
        assert isinstance(numbers, collections.Sequence)
        numbers = tuple(numbers)
        self._numbers = numbers

    ### SPECIAL METHODS ###

    def __eq__(self, expr):
        r'''Is true when `expr` is a nonreduced ratio with numerator and
        denominator equal to those of this nonreduced ratio. Otherwise false.

        Returns boolean.
        '''
        expr = type(self)(expr)
        return self.numbers == expr.numbers

    def __format__(self, format_specification=''):
        r'''Formats duration.

        Set `format_specification` to `''` or `'storage'`.
        Interprets `''` equal to `'storage'`.

        ..  container:: example

            ::

                >>> ratio = mathtools.NonreducedRatio((2, 4, 2))
                >>> print(format(ratio))
                mathtools.NonreducedRatio((2, 4, 2))

        Returns string.
        '''
        from abjad.tools import systemtools
        if format_specification in ('', 'storage'):
            return systemtools.StorageFormatManager.get_storage_format(self)
        return str(self)

    def __hash__(self):
        r'''Hashes non-reduced ratio.

        Required to be explicitly re-defined on Python 3 if __eq__ changes.

        Returns integer.
        '''
        return super(NonreducedRatio, self).__hash__()

    ### PRIVATE PROPERTIES ###

    @property
    def _number_coercer(self):
        return int

    @property
    def _storage_format_specification(self):
        from abjad.tools import systemtools
        positional_argument_values = (
            self._numbers,
            )
        return systemtools.StorageFormatSpecification(
            self,
            is_indented=False,
            keyword_argument_names=(),
            positional_argument_values=positional_argument_values,
            )

    ### PUBLIC PROPERTIES ###

    @property
    def multipliers(self):
        r'''Gets multipliers of nonreduced ratio.

        ..  container:: example

            **Example 1.** Nonreduced ratio of two numbers:

            ::

                >>> ratio = mathtools.NonreducedRatio((2, 4))
                >>> ratio.multipliers
                (Multiplier(1, 3), Multiplier(2, 3))

        ..  container:: example

            **Example 2.** Nonreduced ratio of three numbers:

            ::

                >>> ratio = mathtools.NonreducedRatio((2, 4, 2))
                >>> ratio.multipliers
                (Multiplier(1, 4), Multiplier(1, 2), Multiplier(1, 4))

        Returns tuple of multipliers.
        '''
        from abjad.tools import durationtools
        weight = sum(self.numbers) 
        multipliers = [
            durationtools.Multiplier((_, weight)) 
            for _ in self.numbers
            ]
        multipliers = tuple(multipliers)
        return multipliers

    @property
    def numbers(self):
        r'''Gets numbers of nonreduced ratio.

        ..  container:: example

            **Example 1.** Nonreduced ratio of two numbers:

            ::

                >>> ratio = mathtools.NonreducedRatio((2, 4))
                >>> ratio.numbers
                (2, 4)

        ..  container:: example

            **Example 2.** Nonreduced ratio of three numbers:

            ::

                >>> ratio = mathtools.NonreducedRatio((2, 4, 2))
                >>> ratio.numbers
                (2, 4, 2)

        Set to tuple of two or more numbers.

        Returns tuple of two or more numbers.
        '''
        return self._numbers