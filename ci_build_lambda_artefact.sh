#!/bin/sh
cd aws_lambda_function
zip -r zip.zip *
mv zip.zip ..
cd ..
