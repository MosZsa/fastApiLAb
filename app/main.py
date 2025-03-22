from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Nutrition Calculator API",
    description="API for automated calculation of calorie and nutrient content of dishes",
    version="1.0.0"
)

app.include_router(router)

# --- Run ---
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
