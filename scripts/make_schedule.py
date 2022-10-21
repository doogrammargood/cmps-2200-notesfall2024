import glob
import re
github_organization = "CMPS-2200"
github_repo = "cmps-2200-slides"
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
		ipynb = 'n/a'
		try:
			ipynb = glob.glob('%s/*ipynb' % lecture)[0]
			ipynb = '[static](https://nbviewer.jupyter.org/github/%s/%s/blob/main/%s?flush_cache=True)' % (github_organization, github_repo, ipynb)
		except:
			pass
		live = ' '
		try:
			live = glob.glob('%s/*ipynb' % lecture)[0]
			live = '[live](https://mybinder.org/v2/gh/%s/%s/main?filepath=%s)' % (github_organization, github_repo, live)
		except:
			pass
		# pdf = ' '
		# try:
		# 	pdf = glob.glob('%s/*pdf' % lecture)[0]
		# 	pdf = '[pdf](https://github.com/tulane-cmps2200/slides/blob/master/%s)' % pdf
		# except:
		# 	pass

		print('|%s %s/%s|' % 
			(lecture_title,  live, ipynb ))
