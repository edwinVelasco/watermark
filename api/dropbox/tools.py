import dropbox

from watermark.parameters import ACCESS_TOKEN_DROPBOX


class DropboxTools:
    """
    path: is made up of campus, student code, type doc and
        generated code
        example /cuc/18282004/CN/20190221143028COD18282004CN.pdf
    """
    def __init__(self):
        try:
            self.session = dropbox.Dropbox(ACCESS_TOKEN_DROPBOX)
            self.session.users_get_current_account()
        except Exception as error:
            print('Error de acceso a dropbox')
            print(error)

    def upload(self, path, data):
        """
        Create a new file with the contents provided in the request.
        Do not use this to upload a file larger than 150 MB
        :param path: Path in the user’s Dropbox to save the file.
        :param data: (bytes) – Contents to upload.
        :return: dict <msg, code>
        """
        try:
            res = self.session.files_upload(data, path)
            return {'code': 200, 'msg': res.path_display}
        except dropbox.exceptions.ApiError as error:
            print(error)
            return {'code': 540, 'msg': 'Error al tratar de crear el '
                                        'archivo en dropbox'}

    def download(self, path):
        """
        Download a file from a user’s Dropbox.
        :param path: The path of the file to download.
        :return: dict <msg, code>
        """
        try:
            sd = self.session.files_download(path)
            return {'msg': sd, 'code': 200}
        except dropbox.exceptions.HttpError as error:
            print(error)
            return {'msg': f'Archivo no encontrado {path}', 'code': 540}

    def remove_documents(self, list_path):
        """
        Delete the file or folder at a given path. If the path is a folder,
        all its contents will be deleted too. A successful response indicates
         that the file or folder was deleted.
        :param list_path:
        :return: dict <msg, code>
        """
        try:
            for path in list_path:
                self.session.files_delete_v2(path)
            return {'msg': 'Los archivos vencidos se han borrado con '
                           'éxito', 'code': 200}
        except Exception as error:
            print(error)
            return {'msg': 'Error al tratar de borrar el listado de '
                           'archivos vencidos', 'code': 540}
