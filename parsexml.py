def parse(data):
	lines = data.split('\n');
	tags = []
	for line in lines:
		for tag in __parse_line(line):
			tags.append(tag)
	
	return tags

def __parse_line(line):
	tagData = ''
	inTag = False
	tags = []
	
	for char in line:
		if char == '<':
			inTag = True
			continue
		if char == '>':
			inTag = False
			tags.append(__parse_tag(tagData))
			tagData = ''
			continue
		if inTag:
			tagData += char
	
	return tags

def __parse_tag(tagContents):
	isClosingTag = True if tagContents[0] == '/' else False
	tagName = ''
	attributes = {}
	phase = 0
	openApostrophe = False
	attributeName = ''
	attributeContents = ''
	
	for char in tagContents:
		if phase == 0:
			if char != '/':
				tagName += char
			phase = 1
			continue
		if phase == 1:
			if char == ' ':
				phase = 2
				continue
			tagName += char
			continue
		if phase == 2:
			if char == '=':
				phase = 2.1
				continue
			if char == ' ':
				attributes[attributeName] = True
				attributeName = ''
				continue
			attributeName += char
			continue
		if phase == 2.1:
			if openApostrophe == False and char == '"':
				openApostrophe = True
				continue
			if openApostrophe == True:
				if char == '"':
					openApostrophe = False
					continue
				attributeContents += char
				continue
			if char == ' ':
				phase = 2
				continue
			attributeContents += char
			continue
	if attributeName != '':
		attributes[attributeName] = True if attributeContents == '' else attributeContents
	
	return (tagName, attributes, isClosingTag)
