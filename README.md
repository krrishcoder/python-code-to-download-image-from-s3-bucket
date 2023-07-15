# python-code-to-download-image-from-s3-bucket

note--> plz edit aws s3 policy to this...
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::cryptokonit.com/*"
        }
    ]
}


code to get

import json
import requests as req

URL = 'https://963khe5x17.execute-api.ap-south-1.amazonaws.com/get_movies'
PARAMS = {"genre_name" :"Action Movie"}

r = req.get(url=URL , params = PARAMS)
data = r.json()
print(data)
and allow all public access
