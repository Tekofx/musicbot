<h1 align="center">Musicbot</h1>
<p align="center">
    <img  width=25% src="./assets/logo.png"  >
</p>

<p align="center">Another discord music bot written in python</p>

## Setup
- Set a folder for musicbot and copy to it docker-compose.yml
- Create a folder named env and put inside a file called .env with the content:
    ```
    DISCORD_TOKEN=""
    SPOTIFY_CLIENT_ID=""
    SPOTIFY_CLIENT_SECRET=""
    PREFIX=""
    ```
## Running it
### Using Docker
`docker-compose up -d`

### Using binaries

```sh
pip3 install -r requirements.txt
python3 src/bot.py
```


Bot using the code from https://gist.github.com/vbe0201/ade9b80f2d3b64643d854938d40a0a2d

