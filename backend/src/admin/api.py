from typing import Callable, Dict, List, Union

import flask
from googleapiclient import discovery

from backend.src.data import folder_ids, mime_types
from backend.src.data.drive_playground import playground_folder_ids
from backend.src.data.new_semester import new_folder_ids
from backend.src.drive_commands import copy, create, find, remove
from backend.src.google_apis import drive_api

# TODO: clean up this file :O

admin_api = flask.Blueprint('admin_api', __name__)


@admin_api.route('/create/file', methods=['POST'])
def api_create_file():
    payload = flask.request.get_json()
    drive_service = drive_api.build_service()
    arguments = generate_batch_arguments(payload=payload,
                                         parse_func=parse_create,
                                         drive_service=drive_service)
    create.batch(arguments=arguments,
                 include_output=False,
                 uniform_mime_type=parse_mime_type(payload),
                 drive_service=drive_service)
    return 'Create file worked!'


@admin_api.route('/create/folder', methods=['POST'])
def api_create_folder():
    payload = flask.request.get_json()
    drive_service = drive_api.build_service()
    arguments = generate_batch_arguments(payload=payload,
                                         parse_func=parse_create,
                                         drive_service=drive_service)
    create.batch_folder(arguments=arguments,
                        drive_service=drive_service,
                        include_output=False)
    return 'Create folder worked!'


@admin_api.route('/copy/file', methods=['POST'])
def api_copy_file():
    payload = flask.request.get_json()
    drive_service = drive_api.build_service()
    global_source_resource_id = parse_global_source(payload, drive_service=drive_service)
    arguments = generate_batch_arguments(payload=payload,
                                         parse_func=parse_copy,
                                         drive_service=drive_service,
                                         original_resource_id=global_source_resource_id)
    copy.batch(arguments=arguments,
               drive_service=drive_service,
               include_output=False)
    return 'Copy file worked!'


@admin_api.route('/move/file', methods=['POST'])
def api_move_file():
    payload = flask.request.get_json()
    raise NotImplementedError


@admin_api.route('/move/folder', methods=['POST'])
def api_move_folder():
    payload = flask.request.get_json()
    raise NotImplementedError


@admin_api.route('/rename/file', methods=['POST'])
def api_rename_file():
    payload = flask.request.get_json()
    raise NotImplementedError


@admin_api.route('/rename/folder', methods=['POST'])
def api_rename_folder():
    payload = flask.request.get_json()
    raise NotImplementedError


@admin_api.route('/remove/file', methods=['POST'])
def api_remove_file():
    payload = flask.request.get_json()
    drive_service = drive_api.build_service()  # TODO: add mime type
    arguments = generate_batch_arguments(payload=payload,
                                         parse_func=parse_remove,
                                         drive_service=drive_service)
    remove.batch(arguments=arguments,
                 drive_service=drive_service)
    return 'Remove file worked!'


@admin_api.route('/remove/folder', methods=['POST'])
def api_remove_folder():
    payload = flask.request.get_json()
    drive_service = drive_api.build_service()
    arguments = generate_batch_arguments(payload=payload,
                                         parse_func=parse_remove,
                                         drive_service=drive_service)
    remove.batch(arguments=arguments,
                 drive_service=drive_service)
    return 'Remove folder worked!'


# ----------------------------------------------------------------------------
# Parse
# ----------------------------------------------------------------------------

def generate_batch_arguments(*,
                             payload: Dict,
                             parse_func: Callable,
                             drive_service: discovery.Resource = None,
                             **kwargs) -> List[Union[create.BatchArgument]]:
    target_folders = parse_semester_target(payload)
    arguments = []
    for target in payload['targetFolders']:
        if target['apiId'] == 'committeeChairs':
            arguments += parse_func(target=target,
                                    parent_folder_ids=target_folders['committees'].values(),
                                    drive_service=drive_service,
                                    **kwargs)
        if target['apiId'] == 'committeeLeads':
            arguments += parse_func(target=target,
                                    parent_folder_ids=target_folders['committee_leads'].values(),
                                    drive_service=drive_service,
                                    **kwargs)
        if target['apiId'] == 'missionTeams':
            arguments += parse_func(target=target,
                                    parent_folder_ids=target_folders['mission_teams'].values(),
                                    drive_service=drive_service,
                                    **kwargs)
        if target['apiId'] == 'sectionLeads':
            arguments += parse_func(target=target,
                                    parent_folder_ids=target_folders['sections'].values(),
                                    drive_service=drive_service,
                                    **kwargs)
    return arguments


def parse_semester_target(payload: Dict) -> Dict:
    semester = payload['semester']
    if semester == 'current':
        return {
            'committees': folder_ids.committees,
            'committee_leads': folder_ids.committee_leads,
            'mission_teams': folder_ids.mission_teams,
            'sections': folder_ids.sections,
            'semester_root': folder_ids.semester_root,
        }
    elif semester == 'next':
        return {
            'committees': new_folder_ids.committees,
            'committee_leads': new_folder_ids.committee_leads,
            'mission_teams': new_folder_ids.mission_teams,
            'sections': new_folder_ids.sections,
            'semester_root': new_folder_ids.semester_root,
        }
    elif semester == 'playground':
        return {
            'committees': playground_folder_ids.committees,
            'committee_leads': playground_folder_ids.committee_leads,
            'mission_teams': playground_folder_ids.mission_teams,
            'sections': playground_folder_ids.sections,
            'semester_root': playground_folder_ids.semester_root,
        }


def parse_mime_type(payload: Dict) -> str:
    api_value = payload['mimeType']
    association = {
        'gdoc': mime_types.gdoc,
        'gsheet': mime_types.gsheets,
        'gslide': mime_types.gslides,
        'gform': mime_types.gform,
        'file': mime_types.file
    }
    return association[api_value]


def parse_global_source(payload: Dict, *,
                        drive_service: discovery.Resource = None) -> drive_api.ResourceID:
    path = payload['globalSourcePath']
    mime_type = parse_mime_type(payload)
    parent_folder_id = parse_semester_target(payload)['semester_root']
    return find.recursive_resource(path=path.split('/'),
                                   parent_folder_id=parent_folder_id,
                                   mime_type=mime_type,
                                   drive_service=drive_service)


def parse_create(*,
                 target: Dict,
                 parent_folder_ids: List[drive_api.ResourceID],
                 drive_service: discovery.Resource = None) -> List[create.BatchArgument]:
    return [create.BatchArgument(name=target['targetPath'].split('/')[-1],  # last element of path list
                                 parent_folder_id=find.parent_folder_for_path(path=target['targetPath'],
                                                                              root_folder_id=folder_id,
                                                                              drive_service=drive_service))
            for folder_id in parent_folder_ids]


def parse_copy(*,
               original_resource_id: drive_api.ResourceID,
               target: Dict,
               parent_folder_ids: List[drive_api.ResourceID],
               drive_service: discovery.Resource = None) -> List[copy.BatchArgument]:
    return [copy.BatchArgument(origin_resource_id=original_resource_id,
                               new_name=target['targetPath'].split('/')[-1],  # last element of path list
                               target_folder_id=find.parent_folder_for_path(path=target['targetPath'],
                                                                            root_folder_id=folder_id,
                                                                            drive_service=drive_service))
            for folder_id in parent_folder_ids]


def parse_remove(*,
                 target: Dict,
                 parent_folder_ids: List[drive_api.ResourceID],
                 drive_service: discovery.Resource = None) -> List[copy.BatchArgument]:  # TODO: add Mime type
    return [remove.BatchArgument(resource_id=find.recursive_resource(path=target['targetPath'].split('/'),
                                                                     parent_folder_id=folder_id,
                                                                     drive_service=drive_service))
            for folder_id in parent_folder_ids]
