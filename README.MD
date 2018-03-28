# ICCU Newsletters
A web service which converts Markdown content into a styled HTML web page which can be sent as an email.

This project is a generator for [Imperial College Christian Union's](iccu.co.uk) weekly email newsletters to members.

## Usage
1. Based on `example.md`, write the content of the newsletter in Markdown
2. Open [the website for this service](https://imperial-cu.github.io/generator/) or `webpage/index.html`
3. Fill in the text fields and paste the Markdown content in the big box
4. Click the big green button which says, "Generate the newsletter!"
5. You have been taken to a web page of the generated email. Select all and copy-paste this into the new email message

## For nerds - how does this work?
- [x] The `aws_lambda_function` folder, as you can guess by the name, contains Python code for an AWS Lambda function that
  processes the form inputs and concerts it into a web page
- [x] The main web page, `webpage/index.html` uses HTTP POST to send the input data to the Lambda function
- [x] Travis CI deploys the Lambda function code to an S3 bucket following a successful test of the master branch code
- [x] AWS Lambda automatically syncs up with the code in this bucket
- [x] Travis also deploys the web page to https://imperial-cu.github.io/generator/

## Bus factor issues
- The AWS Lambda function is hosted on Maurice Yap's personal Amazon Web Services account because it's the only practical way to do it which doesn't cost loads of money
  - **If a bus strikes:**
    - inside `aws_lambda_function`, run `pip3 install -t . -r requirements.txt`, then zip up `aws_lambda_function`. This is the zip file you need to upload to AWS after creating a new Lambda function.
    - in `webpage/index.html`, there is a `form` tag. Change the `action` parameter to the target path of the Lambda function you have set up. This is the URL to which you post data to the function, and it responds.
