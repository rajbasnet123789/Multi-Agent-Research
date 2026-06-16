from fastapi import FastAPI
from AI_AGENT.search_agent import crawler
from AI_AGENT.text_generation import model
app = FastAPI()

class crawl_result:
    url:str
    result:str



@app.post('/crawl')
async def crawl(url:str):
    job =crawler.start_crawl(url, limit=500)
    return {url:str,result:job}

@app.write('/write')
async def write(crawled:crawl_result):
    y=model.generate(crawled.result)
    return {crawled_result:crawled.result,generate:y}

@app.structured('/structure')
async def restructure()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="[IP_ADDRESS]", port=8000)
