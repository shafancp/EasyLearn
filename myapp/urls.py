"""
URL configuration for easylearn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('myapp/',views.myapp),
    path('login/',views.login),
    path('login_post/',views.login_post),
    path('adminhome/',views.adminhome),
    path('addsubject/',views.addsubject),
    path('addsubject_post/',views.addsubject_post),
    path('approvedtutors/', views.approvedtutors),
    path('approvedtutors_post/', views.approvedtutors_post),
    path('approvetutor/<id>', views.approvetutor),
    path('rejectedtutors/', views.rejectedtutors),
    path('rejectedtutors_post/', views.rejectedtutors_post),
    path('rejecttutor/<id>', views.rejecttutor),
    path('viewcomplaint/', views.viewcomplaint),
    path('viewcomplaint_post/', views.viewcomplaint_post),
    path('viewfeedback/', views.viewfeedback),
    path('viewfeedback_post/', views.viewfeedback_post),
    path('viewnotes_admin/', views.viewnotes_admin),
    path('viewnotes_admin_post/', views.viewnotes_admin_post),
    path('viewstudent/', views.viewstudent),
    path('viewstudent_post/', views.viewstudent_post),
    path('viewsubject/', views.viewsubject),
    path('viewsubject_post/', views.viewsubject_post),
    path('delete_subject/<id>', views.delete_subject),
    path('viewtutorverify/', views.viewtutorverify),
    path('viewtutorverify_post/', views.viewtutorverify_post),
    path('adminreply/<id>', views.adminreply),
    path('adminreply_post/', views.adminreply_post),
    path('change_password/', views.change_password),
    path('change_password_post/', views.change_password_post),

    path('studenthome/',views.studenthome),
    path('registration/', views.registration),
    path('registration_post/', views.registration_post),
    path('senddoubts/<id>', views.senddoubts),
    path('senddoubts_post/', views.senddoubts_post),
    path('viewdoubts/', views.viewdoubts),
    path('viewdoubts_post/', views.viewdoubts_post),
    path('viewnotes/', views.viewnotes),
    path('viewnotes_post/', views.viewnotes_post),
    path('viewprofile/', views.viewprofile),
    path('updateprofile/', views.updateprofile),
    path('updateprofile_post/', views.updateprofile_post),
    path('viewtutor/<id>', views.viewtutor),
    path('student_sendfeedback/', views.student_sendfeedback),
    path('student_sendfeedback_post/', views.student_sendfeedback_post),
    path('student_sendcomplaint/', views.student_sendcomplaint),
    path('student_sendcomplaint_post/', views.student_sendcomplaint_post),
    path('student_viewreply/', views.student_viewreply),
    path('student_change_password/', views.student_change_password),
    path('student_change_password_post/', views.student_change_password_post),


    path('addnote/', views.addnote),
    path('addnote_post/', views.addnote_post),
    path('registration_tutor/', views.registration_tutor),
    path('registration_tutor_post/', views.registration_tutor_post),
    path('sendfeedback/', views.sendfeedback),
    path('sendfeedback_post/', views.sendfeedback_post),
    path('sendcomplaint/', views.sendcomplaint),
    path('sendcomplaint_post/', views.sendcomplaint_post),
    path('viewdoubts_tutor/', views.viewdoubts_tutor),
    path('replydoubt/<id>', views.replydoubt),
    path('replydoubt_post/',views.replydoubt_post),
    path('viewnote/', views.viewnote_tutor),
    path('viewnote_post/', views.viewnote_tutor_post),
    path('editnote/<id>', views.edit_note_tutor),
    path('editnote_post/', views.edit_note_tutor_post),
    path('detelenote/<id>', views.delete_note_tutor),
    path('viewprofile_tutor/', views.viewprofile_tutor),
    path('updateprofile_tutor/', views.updateprofile_tutor),
    path('updateprofile_tutor_post/', views.updateprofile_tutor_post),
    path('viewnote_tutor/<id>', views.viewnote_tutor),
    path('tutor_change_password/', views.tutor_change_password),
    path('tutor_change_password_post/', views.tutor_change_password_post),

    path('viewreply/', views.viewreply),
    path('viewreply_post/', views.viewreply_post),
    path('viewstudent_tutor/', views.viewstudent_tutor),
    path('viewstudent_tutor_post/', views.viewstudent_tutor_post),
    path('tutor_home/', views.tutor_home),
    path('view_tutor_note/', views.view_tutor_notes),

    path('inputdoc/', views.inputdoc),
    path('inputdoc_post/', views.inputdoc_post),
    path('QAgeneration/', views.QAgeneration),
    path('voicreco/', views.voicreco),
    path('voicreco/', views.voicreco),
    path('exportwav/', views.exportwav),

    path('user_input/', views.user_input),
    path('pdf_process/', views.pdf_process),
    path('user_input_post/', views.user_input_post),
    path('download_conversation/', views.download_conversation),

]