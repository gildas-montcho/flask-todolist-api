FROM python:3.13-slim-bullseye

EXPOSE 5000

WORKDIR /src

# Copy only the requirements.txt file to the workdir (/app)
# If the requirements.txt does not change, the pip install is cached and doesn't run every time
COPY requirements.txt .

RUN pip --no-cache-dir install --requirement requirements.txt

COPY ./src/ .

CMD ["flask", "--app", "src/app", "run", "--host", "0.0.0.0"]
