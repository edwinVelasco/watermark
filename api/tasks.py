from __future__ import absolute_import, unicode_literals

from celery import shared_task

from api.dropbox.tools import DropboxTools

from .models import LogsDocuments


@shared_task
def save_document(path, data, change=False):
    """

    :param path:
    :param data:
    :param change:
    """
    res = DropboxTools().upload(path, data)
    if res.get('code', 404) == 200:
        print('Archivo guardado con exito')
    else:
        print('Error en el guardado del archivo')
    LogsDocuments(action_flag=1 if not change else 2,
                  change_message=res['msg'], code=res['code']).save()


@shared_task
def remove_documents(list_path):
    """

    :param list_path:
    """
    res = DropboxTools().remove_documents(list_path)
    if res.get('code', 404) == 200:
        print('Archivo guardado con exito')
    else:
        print('Error en el guardado del archivo')
    LogsDocuments(action_flag=3,
                  change_message=f'{list_path} \n {res["msg"]}',
                  code=res['code']).save()
