from django.conf.urls import patterns, include, url
from courseapi import views
# I need to check this , this is not needed when I convert this into a package.
urlpatterns = patterns('',
                       url(r'^student', 'courseapi.views.student_view'),
                       url(r'^course', 'courseapi.views.course_view'),
                       url(r'^instructor', 'courseapi.views.instructor_view'),
                       )
