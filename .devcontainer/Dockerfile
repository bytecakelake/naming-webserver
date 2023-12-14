FROM debian:bookworm

# Install Python 3.11.x
RUN apt-get update
RUN apt-get install -y python3.11 python3-pip git
RUN pip install -y fastapi==0.104.1 uvicorn[standard]==0.24.0.post1 jinja2==3.1.2 openai==1.3.5