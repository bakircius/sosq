
# after successfull install sosq, use below code and see first 5 rows.
# data will be in working directory

import sosq

query = "your_search_query_here"
key = "your_key"
token = "your_token"

df = sosq.get_result(query,key,token)
df.head(5)