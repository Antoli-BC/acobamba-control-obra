[app]

title = CONTROL DE OBRA
package.name = controlobra
package.domain = org.obra.control

source.dir = .
source.include_exts = py,png,jpg,jpeg,gif,svg,xlsx,txt

version = 1.1.0
#version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

requirements = python3,kivy,plyer,python-docx,openpyxl,Pillow,pyjnius
orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

android.permissions = CAMERA, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, INTERNET
android.window_softinput_mode = adjustResize
android.gradle_dependencies = androidx.core:core:1.9.0

#presplash.filename = %(source.dir)s/presplash.png
#icon.filename = %(source.dir)s/icon.png
presplash_color = #101010

android.wakelock = False
android.copy_libs = 1
android.debug = False
android.ndk_verbose = False

ios.codesign.allowed = False
