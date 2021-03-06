from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<partner_hash_id>\w{10})/$', views.index_partner, name='index_partner'),
    url(r'^sorry-oly-desktop/$', views.desktop_only, name='desktop_only'),
    url(r'^how-it-works/$', views.how_it_works, name='how_it_works'),
    url(r'^my-codes/$', views.codes, name='codes'),
    url(r'^my-codes-get/$', views.codes_get, name='codes_get'),
    url(r'^result/(?P<hash_id>\w{10})/$', views.result, name='result'),
    url(r'^success/(?P<hash_id>\w{10})/$', views.success, name='success'),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(r'^contact-form/', views.contact_form, name='contact_form'),
    url(r'^edit-order-quantity/', views.edit_order_quantity, name='edit_order_quantity'),

]