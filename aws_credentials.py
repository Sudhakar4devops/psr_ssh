import boto3
from flask import render_template, redirect, url_for

# Store the AWS credentials in a dictionary
aws_credentials = {}

def add_aws_credentials(request):
    if request.method == 'POST':
        access_key = request.form['access_key']
        secret_key = request.form['secret_key']

        # Save the AWS credentials to the dictionary
        aws_credentials[access_key] = secret_key

        # Check AWS account access and print success or failure
        try:
            session = boto3.Session(
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key
            )
            session.client('sts').get_caller_identity()
            print('Success: AWS account access granted')
        except Exception as e:
            print(f'Failure: {e}')

        return redirect(url_for('aws_credentials_route'))
    else:
        return render_template('add.html')

def aws_credentials_route():
    return render_template('aws_credentials.html', credentials=aws_credentials)
