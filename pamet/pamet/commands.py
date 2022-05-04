from typing import Tuple

import misli
from misli.gui import command

import pamet
from pamet import actions

log = misli.get_logger(__name__)


def current_tab_and_page_views() -> Tuple:
    tab = pamet.views.current_tab()
    if not tab:
        raise Exception('There\'s no open tab.')

    page_view = tab.page_view()
    if not page_view:
        raise Exception('No page view.')

    return tab, page_view


@command(title='Create new note')
def create_new_note():
    tab, page_view = current_tab_and_page_views()
    actions.note.create_new_note(page_view.id, page_view.mouse_position())


@command(title='Create new page')
def create_new_page():
    tab, page_view = current_tab_and_page_views()
    actions.tab.create_new_page(tab.id, page_view.mouse_position())


@command(title='Save page properties')
def save_page_properties():
    tab, page_view = current_tab_and_page_views()
    properties_view_state = misli.gui.view_state(
        tab.state().right_sidebar_view_id)
    page = properties_view_state.page
    page.name = properties_view_state.name_line_edit_text
    actions.map_page.save_page_properties(page)
    actions.map_page.close_page_properties(properties_view_state.id)


@command(title='Open page properties')
def open_page_properties():
    tab, page_view = current_tab_and_page_views()
    actions.map_page.open_page_properties(tab.id)


@command(title='Edit selected note')
def edit_selected_notes():
    tab, page_view = current_tab_and_page_views()
    selected_nc_ids = page_view.state().selected_nc_ids
    if not selected_nc_ids:
        return

    note_component = misli.gui.view(next(iter(selected_nc_ids)))
    actions.note.start_editing_note(tab.id, note_component.note)