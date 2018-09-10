import parsexml

xml = '<Foo foo="foo" foo1="foo 1">Foo</Foo>\n<Bar bar=bar>Bar</Bar>\n<Baz baz>Baz</Baz>'

parsed = parsexml.parse(xml)
print(parsed)
