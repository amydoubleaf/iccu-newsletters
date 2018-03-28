import json
import urllib
import markdown


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else res,
        'headers': {
            'Content-Type': 'text/html',
        },
    }


def get_date(body_raw):
    return (body_raw.split('date=')[1]).split('&')[0]


def get_bible_passage(body_raw):
    return (body_raw.split('bible_passage=')[1]).split('&')[0]


def get_bible_passage_location(body_raw):
    return (body_raw.split('bible_passage_location=')[1]).split('&')[0]


def get_content_md(body_raw):
    return body_raw.split('raw_markdown=')[1]


def compile_html_from_request_body(body_raw):
    date_text = get_date(body_raw)
    bible_passage_text = get_bible_passage(body_raw)
    bible_passage_location_text = get_bible_passage_location(body_raw)
    content_md = get_content_md(body_raw)

    # Get the template html
    template_html_file = open('resources/template.html', 'r')
    output_html = template_html_file.read()
    template_html_file.close()

    # Fill in the content
    content_html = markdown.markdown(content_md)
    output_html = output_html.replace('[CONTENT]', content_html)

    # Fill in other data
    output_html = output_html.replace('[DATE]', date_text)
    output_html = output_html.replace('[BIBLE PASSAGE]', bible_passage_text)
    output_html = output_html.replace('[BIBLE PASSAGE LOCATION]', bible_passage_location_text)
    return output_html


def lambda_handler(event, context):
    operation = event['httpMethod']
    if operation == 'GET':
        return respond(err=None, res=json.dumps(event, indent=2))
    elif operation == 'POST':
        output_html = compile_html_from_request_body(urllib.parse.unquote_plus(event['body']))
        return respond(None, res=output_html)
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))
