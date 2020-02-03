## Python version required:

```
Python 3.7
```

## Token Creation

Create API token:
https://id.atlassian.com/manage/api-tokens

Create base64 encoded token example:

```
echo -n user@example.com:api_token_string | base64
```

## Create conf.py

Add following values to conf.py

```
api_token = 'base64token'
api_url = 'https://subdomain.atlassian.net/rest/api/2/'
```

## Package Requirements:

```
requests
pandas
```

Install packages through requirements.txt:

```
pip3 install requirements.txt
```
