FROM python:3.11-slim

WORKDIR /hybrid_recommender_system

COPY ./requirements.txt ./requirements.txt

COPY ./.env ./.env

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./api/Hybrid_Recommendation_System .

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]

# docker run --name recsys_test_api -p 8001:8000 --env-file ./.env img_name