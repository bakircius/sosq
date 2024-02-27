# stack overflow search queries (sosq)

This project fetches StackOverflow API returns a dataframe

# install

pip install sosq

# for use

1- Get your key and token from stackexchange (https://stackapps.com/users/login?returnurl=/apps/oauth/register)

2- sample code below.

```
import sosq
sosq.get_result("your_search_query", "your_key", "your_access_token")
```

