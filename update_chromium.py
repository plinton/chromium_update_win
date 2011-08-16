import urllib2, subprocess, tempfile

url = "http://build.chromium.org/f/chromium/snapshots/Win_Webkit_Latest/"
ver_file = urllib2.urlopen(url + "LATEST")
ver = ver_file.read()
print("getting version " + ver)
installer_file = urllib2.urlopen(url + ver + "/mini_installer.exe")
temp_folder = tempfile.mkdtemp()
temp_file = open(temp_folder + "mini_installer.exe", "w+b")
temp_file.write(installer_file.read())
temp_file.flush()
temp_file.close()
print("updating chromium...")
subprocess.Popen(temp_file.name, shell=True)
