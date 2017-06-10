import sys
import requests
import re
import json

# Make sure a file name has been given
if len(sys.argv) < 2:
  print('I need the file name! - Enter the file name after compile.py.')
  print('For example, if the email file name is example.md, type this:')
  print('python3 compile.py example.md')
  exit()

file_name = sys.argv[1]

# Make sure the given file name is for a markdown file
if not (file_name.endswith('.md') or file_name.endswith('.MD')):
    print('You need to give me a markdown file')
    print('The file name should end in \'.md\' or \'.MD\'')
    exit()

src_md_file = open(file_name, 'r')
src_md = src_md_file.read()
src_md_file.close()

# Get main content
content_md = src_md.split('[CONTENT]')[1].encode('ascii', 'xmlcharrefreplace')
headers = {'Content-Type': 'text/x-markdown'}
url = 'https://api.github.com/markdown'
md_request_json = json.dumps({"text": content_md.decode(), "mode": "gfm", "context": "a"})
content_html = (requests.post(url, headers=headers, data=md_request_json)).text

# Get other data: date, bible passage, bible passage location
get_attribute = lambda attr : re.findall('\[' + attr + '\](.*)\n', src_md)[0].strip()
date_text = get_attribute('DATE')
bible_passage_text = get_attribute('BIBLE PASSAGE')
bible_passage_location_text = get_attribute('BIBLE PASSAGE LOCATION')

# Get the template html
template_html_file = open('template/template.html', 'r')
output_html = template_html_file.read()
template_html_file.close()

# Fill in the content
output_html = output_html.replace('[CONTENT]', content_html)

# Fill in other data
output_html = output_html.replace('[DATE]', date_text)
output_html = output_html.replace('[BIBLE PASSAGE]', bible_passage_text)
output_html = output_html.replace('[BIBLE PASSAGE LOCATION]', bible_passage_location_text)

# Process centering
output_html = output_html.replace('<p>[CENTRE]</p>', '<center>')
output_html = output_html.replace('<p>[/CENTRE]</p>', '</center>')

# Process colours
output_html = re.sub('<p>\[COLOUR(.*)\]<\/p>', '<span style=\"color: ' + r'\1'.strip() + '\">', output_html)
output_html = output_html.replace('<p>[/COLOUR]</p>', '</span>')


# Make the new html file
file_location = 'compiled/' + file_name[:-3] + '.html'
output_html_file = open(file_location, 'w')
output_html_file.write(output_html)
output_html_file.close()

print('Done! The generated html file is at ' + file_location)
print('Have a safe journey home!')
