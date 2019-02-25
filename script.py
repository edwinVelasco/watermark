import dropbox
# siga_document
# dbx = dropbox.Dropbox('PtXbtd6gBKEAAAAAAAAAgrqNsGSUg4Gc3YoOD3HZxtPZLpmphgN6shQwx_iiXp4T')
# api_siga_postgraduate

dbx = dropbox.Dropbox(
    'Rld-8fG1VnAAAAAAAAAALt2xZ2mjRAf_aMV9ZRaYGzrJRVk0LXPQlLc2DeYQqbww')
dbx.users_get_current_account()

# for entry in dbx.files_list_folder('').entries:
#     print(entry.name)
#     print(entry)
#     print('/n')
# file = open('pol.pdf', 'rb')
file = open('deuda.pdf', 'rb')
res = dbx.files_upload(file.read(),
                       '/cuc/18282004/CN/20190221143028COD18282004RX.pdf',
                       mode=dropbox.dropbox.files.WriteMode.overwrite,
                       mute=True)
print(res)

# res = dbx.files_delete_v2('/cuc/18282004/CN/20190221143028COD18282004CN.pdf')
# print(res)


# try:
#     sd = dbx.files_download('/1090408984/deuda2.pdf')
#     print(sd)
# except Exception as e:
#     print(e.error.get_path().is_not_found())
#     print(e.error.get_path().is_not_file())
#     print(e.error.get_path().is_restricted_content())
