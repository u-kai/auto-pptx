from fastapi import FastAPI
from src.server.convertor import PresentationRequest, PresentationRequestConvertor


def api_server():
    app = FastAPI()

    @app.post("/create_pptx")
    async def create_pptx(req: PresentationRequest):
        print(req)
        convertor = PresentationRequestConvertor(req)
        pptx = convertor.convert()
        pptx.save()
        return {"message": "Successfully created pptx"}

    return app
