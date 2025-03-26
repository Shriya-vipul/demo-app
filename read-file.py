# This file is to read data
def __init__():
  self.filePath = 'test-data.json'
  self.data = {}

  def readJsonData(self):
    self.data = json.load(self.file)
