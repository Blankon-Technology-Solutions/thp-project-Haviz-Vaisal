# blankon take home project

How to run:

-   Rename .env/.local/.django.template to .django
-   Change environment settings value on .django
-   chmod +x do
-   ./do setup

Visit localhost:8090/api/swagger/

Run test case:

-   create Python 3.10.12 virtualenv
-   activate virtualenv
-   cd sherpany
-   pip install -r tests/requirements.txt
-   export DJANGO_SECRET_KEY=YOUR_SECRET_KEY
-   export PYTHONPATH=/:tests/
-   python -m pytest --ds=component.test_settings tests/component


Use https://developers.google.com/oauthplayground to get google id token etc.


## FAQs

1. DB port already in used
- If you have port conflict, change postgresl port in local.yaml and change .django settings accordingly
