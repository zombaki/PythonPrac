#!/bin/sh

git add .
git commit -m "This is a cron update files to Github repo."
git push
echo  $(date) >> ~/pract/gitlog.txt
