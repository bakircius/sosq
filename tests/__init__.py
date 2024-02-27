#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Refactored version of the fetcher.py script to follow a functional programming style suitable for open-source projects.
"""
import sys
sys.path.append('.')
import requests
import pandas as pd
from typing import Dict, Tuple, List


def build_api_url(base_url: str, apiname: str) -> str:
    """Construct the full API URL from the base URL and API name."""
    return f"{base_url}{apiname}"


def fetch_page(url: str, params: Dict[str, str]) -> Dict:
    """Fetch a single page of results from the API."""
    response = requests.get(url, params=params)
    return response.json()


def process_response(response: Dict) -> Tuple[pd.DataFrame, bool, bool]:
    """Process the API response, returning a DataFrame, has_more, and quota_remaining indicators."""
    df = pd.DataFrame(data=response["items"])
    has_more = response["has_more"]
    quota_remaining = response["quota_remaining"] > 500
    return df, has_more, quota_remaining


def append_dataframes(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """Append one DataFrame to another, handling the first iteration case."""
    if df1 is None:
        return df2
    else:
        return df1.append(df2, ignore_index=True)


def update_params(params: Dict[str, str], page: int) -> Dict[str, str]:
    """Update the request parameters for the next page."""
    params['page'] = page
    return params


def save_to_csv(df: pd.DataFrame, filename: str):
    """Save the DataFrame to a CSV file."""
    df.to_csv(filename)


def getResults(query, key, access_token):
    query = query
    page = 1
    params = {
        'q': query,
        'key': key,
        'access_token': access_token,
        'pagesize': 100,
        'site': 'stackoverflow',
        'order': 'asc',
        'sort': 'creation',
        'filter': 'withbody',
        'page': page
    }
    base_url = 'https://api.stackexchange.com/2.3/'
    apiname = 'search/advanced'
    url = build_api_url(base_url, apiname)

    has_more = True
    quota = True
    df_combined = None

    while has_more and quota:
        response = fetch_page(url, params)
        df, has_more, quota = process_response(response)
        df_combined = append_dataframes(df_combined, df)
        page += 1
        params = update_params(params, page)

    save_to_csv(df_combined, query + ".csv")


# Uncomment to run the getResults function
# getResults(query, key, access_token)


# results will be in your project folder.