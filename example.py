import parsexml

xml = '<Foo foo="foo">Foo</Foo>\n<Bar bar="bar">Bar</Bar>'

parsed = parsexml.parse(xml)
print(parsed)
