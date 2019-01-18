import requests

class changeHttp:
	
	filename = ''
	dict = {}
	
	def __init__(self,filename):
		self.filename = filename
		
	def generatedict(self):
		with open(self.filename,'r') as f:
			line = f.readline()
			while line:
				if ':' not in line:
					line = f.readline()
				line = line.strip()
				line = line.replace('\n','')
				list = line.split(':')
				key = str(list[0]).strip()
				value = str(list[1]).strip()
				self.dict[key] = value
				line = f.readline()
	
	def getDict(self):
		return self.dict
	
	def changeCookie(self,cookie):
		self.dict['cookie'] = cookie
		
	def changeCookieFile(self,filename):
		try:
			with open(file,'r') as f:
				cookie = f.read()
				cookie = cookie.strip()
				cookie = cookie.replace('\n','')
				self.dict['cook'] = cookie
		except:
			pass
	
	def changeRemain(self,key,value):
		try:
			self.dict[key] = value
		except:
			pass
			
	def getCookie(self):
		cookie = self.dict['cookie']
		cookie = str(cookie)
		return cookie
		
	def getRemain(self,key):
		value = self.dict[key]
		value = str(value)
		return value
			