these commands are perfomed in aws cloudshell::

  python3 -m venv ec2-slack-notification
  cd ec2-slack-notification/
  source ./bin/activate
  pip install resources
  cd lib/python3.7/site-packages/
  zip -r slack zip .
  cd ../../../
  mv ./lib/python3.7/site-packages/slack.zip .
  vi slackcode.py #insert the python code here
  zip -g slack.zip slackcode.py #then import the whole zip file to lambda
