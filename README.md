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

and allow all public access
