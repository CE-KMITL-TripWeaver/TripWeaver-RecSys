FROM python:3.11-slim

# Set the initial working directory for project setup
WORKDIR /hybrid_recommender_system

COPY ./requirements.txt ./requirements.txt

COPY ./.env ./.env

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . .

# Change to the specific directory containing server.py
WORKDIR /hybrid_recommender_system/api/Hybrid_Recommendation_System

EXPOSE 8000

# CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
# Retrain model and run the recommender system API
CMD ["sh", "-c", "python ../../script/retrain_model_content-based.py \
                && python ../../script/retrain_model_collaborative_filtering.py \
                && uvicorn server:app --host 0.0.0.0 --port 8000"]

