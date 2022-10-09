launch with command
```bash
docker run -it --rm -v "$(pwd):/usr/src/app"  --name ngosscrper ongscraper
```

## Next stps
1. Connect to database
2. Make it spidey. Go inside the pages and inspct, find the links to sign and stuffs
3. Don't make it loop all things everytime. Hash the already parsed link so i can go to the next ones.
4. Divide in multiple parsers, object oriented. Every parser works for a different website