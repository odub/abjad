import abc
from experimental.tools.scoremanagertools.core.ScoreManagerObject import \
    ScoreManagerObject


# TODO: extend repr to show target, if any
class Wizard(ScoreManagerObject):

    ### CLASS VARIABLES ###

    __metaclass__ = abc.ABCMeta

    target_editor_class_name_suffix = 'Editor'

    ### INITIALIZER ###

    def __init__(self, session=None, target=None):
        ScoreManagerObject.__init__(self, session=session)
        self.target = target

    ### PRIVATE PROPERTIES ###

    @abc.abstractproperty
    def _breadcrumb(self):
        pass

    ### PRIVATE METHODS ###

    @abc.abstractmethod
    def _run(self, cache=False, clear=True, head=None, user_input=None):
        pass
