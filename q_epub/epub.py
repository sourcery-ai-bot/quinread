import zipfile
from .exceptions import *

class EpubBook:
	def __init__(self, filename):
		self.filename = filename
		self.load()

	def load(self):
		try:
			self.zf = zipfile.ZipFile(self.filename, "r", compression=zipfile.ZIP_DEFLATED, allowZip64=True)
		except zipfile.BadZipfile:
			raise EpubError("Bad Zip file")
		except zipfile.LargeZipFile:
			raise EpubError("Large Zip file")
