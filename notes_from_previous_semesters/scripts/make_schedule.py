import glob
import re
github_organization = "cmps-2200"
github_repo = "cmps-2200-notes"
def get_header(fname):
	try:
		return re.sub('#', '', open(fname).readlines()[0]).strip()
	except Exception as e:
		return 'name'

for module in sorted(glob.glob("module*")):
	module_title = '**%s**' % get_header('%s/README.md' % module)
	print('|[%50s](https://github.com/%s/%s/tree/main/%s)|' % (module_title, github_organization, github_repo, module))
	for lecture in sorted(glob.glob('%s/0*' % module)):
		lecture_title = '&nbsp;&nbsp;%s' % get_header('%s/README.md' % (lecture))
		slides = 'n/a'
		try:
			slides = glob.glob('%s/*slides.html' % lecture)[0]
			# https://cmps-2200.github.io/cmps-2200-notes/module-01-cost/01-intro/01-intro.slides.html#/
			slides = '[%s](https://%s.github.io/%s/%s)' % (lecture_title, github_organization, github_repo, slides)
		except:
			pass
		# pdf = ' '
		# try:
		# 	pdf = glob.glob('%s/*pdf' % lecture)[0]
		# 	pdf = '[pdf](https://github.com/tulane-cmps2200/slides/blob/master/%s)' % pdf
		# except:
		# 	pass

		print('|%s|' % (slides))
