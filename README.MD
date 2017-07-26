# ICCU Newsletters
A web service which converts Markdown content into a styled HTML web page which can be sent as an email.

This project is a generator for [Imperial College Christian Union's](iccu.co.uk) weekly email newsletters to members.

## Usage
1. Based on `example.md`, write the content of the newsletter in Markdown
2. Open [the website for this service](http://mauriceyap.co.uk/iccu) or `webpage/index.html`
3. Fill in the text fields and paste the Markdown content in the big box
4. Click the big green button which says, "Generate the newsletter!"
5. You have been taken to a web page of the generated email. Select all and copy-paste this into the new email message

## For nerds - how does this work?
- [x] The `aws_lambda_function` folder, as you can guess by the name, contains Python code for an AWS Lambda function that
  processes the form inputs and concerts it into a web page
- [x] The main web page, `webpage/index.html` uses HTTP POST to send the input data to the Lambda function
- [ ] Travis CI deploys the Lambda function code to an S3 bucket following a successful test of the master branch code
- [x] AWS Lambda automatically syncs up with the code in this bucket
- [ ] Travis also deploys the web page into a different S3 bucket which stores the website
