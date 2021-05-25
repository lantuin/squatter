FROM rackspacedot/python37
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && apt-get update && apt-get install -y xvfb libxi6 libgconf-2-4 default-jdk python3-dnspython python3-geoip python3-whois python3-requests python3-ssdeep google-chrome-stable
WORKDIR /squatter
RUN git clone https://github.com/elceef/dnstwist.git
RUN pip3 install imgkit && pip3 install wand && pip3 install selenium && pip3 install dnspython
RUN mkdir tmp && wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip && unzip chromedriver_linux64.zip
COPY squatter.py /squatter/squatter.py
CMD ["python", "squatter.py"]
