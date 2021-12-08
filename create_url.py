def create_url(keywork, start_date, end_date, max_results = 10):
   search_url = "https://api.twitter.com/2/tweets/search/all"
    
    query_params = {
    # 'query': '(from:twitterdev -is:retweet) OR #twitterdev',
    'query': '(kabul OR taliban) (isis OR isis-k OR #isis OR #isis_k or iskp or khorasan) (lang:en OR lang:ar OR lang:fa)',
    'tweet.fields': 'attachments,context_annotations,conversation_id,created_at,entities,geo,in_reply_to_user_id,lang,possibly_sensitive,public_metrics,referenced_tweets,reply_settings,source,withheld',
    'expansions': 'author_id,referenced_tweets.id,in_reply_to_user_id,attachments.media_keys,attachments.poll_ids,geo.place_id,entities.mentions.username,referenced_tweets.id.author_id',
    'user.fields': 'id,name,username,created_at,description,entities,location,pinned_tweet_id,profile_image_url,protected,public_metrics,url,verified,withheld',
    'media.fields': 'media_key,type,duration_ms,height,preview_image_url,public_metrics,width,alt_text',
    'place.fields': 'full_name,id,contained_within,country,country_code,geo,name,place_type',
    'max_results': '100',
    'start_time': '2021-08-19T00:00:01.000Z', # RFC3339 date-time
    'end_time': '2021-09-02T00:00:01.000Z', # RFC3339 date-time
    'next_token': "b26v89c19zqg8o3fpdp7i2xji7k26qbz42tx6676gk6m5"
}

    return (search_url, query_params)
