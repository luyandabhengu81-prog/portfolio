FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && useradd --create-home portfolio
COPY --chown=portfolio:portfolio . .
USER portfolio
ENV PORT=8000
EXPOSE 8000
CMD ["sh", "-c", "exec gunicorn --bind 0.0.0.0:${PORT:-8000} --workers 2 --access-logfile - --error-logfile - app:app"]
