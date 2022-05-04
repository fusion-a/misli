import os
import signal

import misli
from misli.gui.model_to_view_binder.actions import update_views_from_entity_changes

import pamet
from pamet import default_key_bindings
from pamet.desktop_app.app import DesktopApp
from pamet.desktop_app.config import get_config
from pamet.storage import FSStorageRepository

log = misli.get_logger(__name__)
signal.signal(signal.SIGINT, signal.SIG_DFL)


def main():
    misli.line_spacing_in_pixels = 20
    config = get_config()
    repo_path = config['repository_path']
    log.info('Using repository: %s' % repo_path)

    # # Testing - restore repo changes
    # for f in os.scandir(repo_path):
    #     if f.name.endswith('backup'):
    #         os.rename(f.path, f.path[:-7])
    #
    #     if f.name.endswith('misl.json'):
    #         os.remove(f.path)

    if os.path.exists(repo_path):
        fs_repo = FSStorageRepository.open(repo_path)
    else:
        fs_repo = FSStorageRepository.new(repo_path)

    misli.set_repo(fs_repo)
    misli.configure_for_qt()
    pamet.configure_for_qt()

    misli.gui.key_binding_manager.apply_config(default_key_bindings)
    misli.on_entity_changes(update_views_from_entity_changes)

    desktop_app = DesktopApp()

    start_page = pamet.helpers.get_default_page()
    if not start_page:
        start_page = pamet.actions.other.create_default_page()

    misli.gui.queue_action(pamet.actions.window.new_browser_window,
                           args=[start_page.id])

    return desktop_app.exec_()