
import aiohttp

async def load_data_from_url() -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.chucknorris.io/jokes/random") as responce:
            if responce.status == 200:
                data = await responce.json()
                return data.get("value", "Error Parsing")
            else:
                return "Error Request"