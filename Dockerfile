FROM python:3.11-slim

RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
       ffmpeg \
       git \
       curl \
       redis-server \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/

RUN pip3 install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

RUN python3 -c "\
import site, os; \
sp = site.getsitepackages()[0]; \
path = os.path.join(sp, 'youtubesearchpython/core/requests.py'); \
content = open(path).read(); \
content = content.replace('proxies=self.proxy', ''); \
open(path, 'w').write(content)"

CMD ["bash", "start.sh"]
