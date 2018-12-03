from bs4 import BeautifulSoup
import re,csv
import requests
version = []
version2 = []
result = []
range = None
lib1_stop_pos=-1
pattern_name = re.compile('(?<=in )(\S+\d?) (\d+\.\S*)?(before)?(through)? (\d+\.\S*)|(Moodle) (\d+\.\S*)? (before)?(through)? (\d+\.\S*)')
#pattern_name2 = re.complie('(\S+\d?)(\d+\.\S(before)?(through)? (\d+\.\S*)')
pattern_version_1 = re.compile('(\d+\.\S+) (before) (\d+\.\S+)')
with open('NVD - CVE-2017-16816.html','r') as fp, open('phplist.csv','w') as fw, open('PHPCVEList_Huang.csv','r') as fr:
	CVE = 'CVE-2017-16816'
	phplist = fr.read().split('\n')
	
	fields_name = ['CVE ID','lib_name','versions']
	writer = csv.writer(fw,delimiter=',',lineterminator = '\n')
	writer.writerow(fields_name)
	for cveid in phplist:
		print (cveid)
		html_page = requests.get('https://nvd.nist.gov/vuln/detail/'+cveid)
		html = BeautifulSoup(html_page.text,'html.parser')
		description = html.find(attrs={"data-testid": "vuln-description"}).string
		
		name = re.search(pattern_name,description)
		if name:
			
			lib_name = name.group(1) 
			#print(name.group(3))
			if name.group(2):
				left_version = name.group(2).replace('x','0')
				if name.group(3) == 'before':
					version.append('['+left_version+','+name.group(5)+')')
					range = name.group(3)#before or through
				elif name.group(4) == 'through':
					version.append('['+left_version+','+name.group(5)+']')
					range = name.group(4)#before or through
			else:
				if name.group(3) == 'before':
					version.append('[,'+name.group(5)+')')
					range = name.group(3)#before or through
				elif name.group(4) == 'through':
					version.append('[,'+name.group(5)+']')
					range = name.group(4)#before or through
				else:
					version.append('['+name.group(5)+']')
			name2 = re.search(pattern_name,description[name.end():])
			if name2:
				lib1_stop_pos = name2.start()
				lib_name2 = name2.group(1)
				if name2.group(2):
					left_version = name2.group(2).replace('x','0')
					if name2.group(3) == 'before':
						version2.append('['+left_version+','+name2.group(5)+')')
						range = name2.group(3)#before or through
					elif name2.group(4) == 'through':
						version2.append('['+left_version+','+name2.group(5)+']')
						range = name2.group(4)#before or through
					
				else:
					if name2.group(3) == 'before':
						version2.append('[,'+name2.group(5)+')')
						range = name2.group(3)#before or through
					elif name2.group(4) == 'through':
						version2.append('[,'+name2.group(5)+']')
						range = name2.group(4)#before or through
					else:
						version2.append('['+name2.group(5)+']')
				versions2 = re.findall(pattern_version_1,description[name2.end():])
				if versions2:
					for ver in versions2:
						version2.append('['+ver[0]+','+ver[2]+')').encode('utf-8')
				for i in version2:
					i = i.encode('utf-8')
					result.append(i)
				writer.writerow([cveid,lib_name2,result])
				result = []
				
				
			#print (version)
			if lib1_stop_pos:
				versions = re.findall(pattern_version_1,description[name.end():lib1_stop_pos])
			else:
				versions = re.findall(pattern_version_1,description[name.end():])
			if versions:
				for ver in versions:
					version.append('['+ver[0].replace('x','0')+','+ver[2]+')')
			for i in version:
				i = i.encode('utf-8')
				result.append(i)
			writer.writerow([cveid,lib_name,result])
			print (cveid,lib_name,result)
			result = []
		else:
			#name = re.search(pattern_name,description)
			
			
			writer.writerow([cveid])
#print (result)
