launch with command
```bash
docker run -it --rm -v "$(pwd):/usr/src/app"  --name ngosscrper ongscraper
```

## Next stps
1. Connect to database
2. Make it spidey. Go inside the pages and inspct, find the links to sign and stuffs
3. Don't make it loop all things everytime. Hash the already parsed link so i can go to the next ones.
4. Divide in multiple parsers, object oriented. Every parser works for a different website

(docker python mysql documentation)[https://docs.docker.com/language/python/develop/]
(altro tutorial python mysql docker )[https://medium.com/swlh/how-to-connect-to-mysql-docker-from-python-application-on-macos-mojave-32c7834e5afa]
(questo potrebbe fare al caso nostro)[https://mothishdeenadayalan.medium.com/containerizing-a-python-app-mysql-python-docker-1ce64e444ed9]
