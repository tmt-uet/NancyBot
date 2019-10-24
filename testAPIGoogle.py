from googleapiclient.discovery import build


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res


my_api_key = "AIzaSyCHsXec6soS2VuTeXz3aqq0YZBxiyDHiVI"
my_cse_id = "001182625316242497539:kyv2vbncdun"

result = google_search("Berlin", my_api_key, my_cse_id)
# print(result["items"][0]["snippet"])
print(result["items"])
