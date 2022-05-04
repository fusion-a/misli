from __future__ import annotations

from misli import gui, get_logger
from misli.entity_library.change import Change

from .view_state import ViewState

log = get_logger(__name__)


class View:
    """This base View class should be inherited by all view implementations in
    a Misli app. It registers every instance in misli.gui on class construction
     and provides access to a copy of the last applied view model via
     displayed_model(). There's also convenience methods to retrieve the child
     views.
     You can check out the developer documentation for the GUI architecture
     of Misli based apps, but overall we have a tree of views, where each one
     has a view model. View models get updated only via misli.update_view_model
      and those updates get rendered asynchronously (i.e. if a user action
      changes several views - those changes will be cached and then pushed
      as a batch of updates to the Views).
      Each view that wants to receive updates should implement the
      handle_model_update(self, previous_state, new_model) method. And if the view
      manages it's children it will implement the handle_child_changes method,
       which is invoked by misli.gui on each relevant view update with three
    arguments: children_added, chidren_removed and children_updated.
    """
    def __init__(self,
                 initial_state: ViewState = None):
        """Registers the View instance in misli.gui, so that model and child
        updates are received accordingly.

        Args:
            parent (str): The parent id. Can be none if this view is a root
            initial_state (Entity): The view model should be an Entity subclass
        """
        self.subscribtions = []

        if not initial_state:
            initial_state = ViewState()
        # if parent:
        #     initial_state.parent_id = parent.id
        self._state = initial_state
        self.__previous_state = None

    def __repr__(self):
        return '<%s id=%s>' % (type(self).__name__, self.id)

    @property
    def id(self):
        return self._state.id

    def state(self) -> ViewState:
        return self._state

    def previous_state(self) -> ViewState:
        if not self.__previous_state:
            return None
        return self.__previous_state.copy()

    def on_state_change(self, change: Change):
        pass

    def child(self, child_id: str) -> View:
        return gui.view(child_id)
