from django.urls import path
from people.views import index, file_upload, data_entry, file_download, reset_data

urlpatterns = [
    path('', index, name='index'),
    path('upload', file_upload, name='file_upload'),
    path('entry', data_entry, name='data_entry'),
    path('download', file_download, name='file_download'),
    path('reset', reset_data, name='delete_records'),
]
