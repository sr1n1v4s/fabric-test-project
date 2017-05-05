from fabric.api import local

def touch():
	local("./manage.py")
def commit():
	local("git add . && git commit -m 'testing touch manage'")
def push():
	local("git push origin master")

def deploy():
	print "Touching files"
	print "---------------"
	touch()
	
	print " adding to github & commit"
	print "--------------------------"
	commit()
	
	print "Pushing to git hub"
	print "--------------------------"
	push()
