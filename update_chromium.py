import urllib2, subprocess, tempfile

url = "http://commondatastorage.googleapis.com/chromium-browser-snapshots/Win/"
ver_file = urllib2.urlopen(url + "LAST_CHANGE")
ver = ver_file.read()
print("getting version " + ver)
installer_url = "http://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?path=Win"
installer_file = urllib2.urlopen(url + ver + "/mini_installer.exe")
temp_folder = tempfile.mkdtemp()
temp_file = open(temp_folder + "mini_installer.exe", "w+b")
temp_file.write(installer_file.read())
temp_file.flush()
temp_file.close()
print("updating chromium...")
subprocess.Popen(temp_file.name, shell=True)
