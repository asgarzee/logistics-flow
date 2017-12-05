from django.urls import re_path

from .api import CreateView, DeliverView, DispatchView, PickView, ReadyToDispatchView, ReceiveView, ShelveView

urlpatterns = [
    re_path(r'^create/$', CreateView.as_view(), name='create'),
    re_path(r'^receive/$', ReceiveView.as_view(), name='receive'),
    re_path(r'^pick/$', PickView.as_view(), name='pick'),
    re_path(r'^shelve/$', ShelveView.as_view(), name='shelve'),
    re_path(r'^ready-to-dispatch/$', ReadyToDispatchView.as_view(), name='ready_to_dispatch'),
    re_path(r'^deliver/$', DeliverView.as_view(), name='deliver'),
    re_path(r'^dispatch/$', DispatchView.as_view(), name='dispatch'),

]
