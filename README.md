To run in docker:

Bot using the code from https://gist.github.com/vbe0201/ade9b80f2d3b64643d854938d40a0a2d

`docker run -d --name musicbot --mount type=bind,src=<musicbot_path>/src/,dst=/bot/src -p 80:80 musicbot`
