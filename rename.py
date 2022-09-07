# rename files from 1 - ...

import os

# path shizzle
path = './'
files = os.listdir(path)
getImages = []
getFileEnding = []

for filename in os.listdir(path):
		if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".JPG") or filename.endswith(".PNG"):
			getImages.append(filename)
			getFileEnding.append(0)
		elif filename.endswith(".jpeg") or filename.endswith(".webp") or filename.endswith(".JPEG") or filename.endswith(".WEBP"):
			getImages.append(filename)
			getFileEnding.append(1)
		else:
			continue

for index in range(len(getImages)):
		if getFileEnding[index] == 0:
				os.rename(os.path.join(path, getImages[index]), os.path.join(path, ''.join([str(index), getImages[index][-4:]])))
		elif getFileEnding[index] == 1:
				os.rename(os.path.join(path, getImages[index]), os.path.join(path, ''.join([str(index), getImages[index][-5:]])))