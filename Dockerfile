FROM monogramm/docker-erpnext:11-debian

# Install Google Chrome & Chrome WebDriver for UI tests
RUN set -ex; \
    sudo apt-get update -q; \
    sudo apt-get install -y --no-install-recommends \
        unzip \
    ; \
    CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`; \
    sudo mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION; \
    sudo curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip; \
    sudo unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION; \
    sudo rm /tmp/chromedriver_linux64.zip; \
    sudo chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver; \
    sudo ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver; \
    export PATH="$PATH;/usr/local/bin/chromedriver"

# Build environment variables
ENV TESSDATA_PREFIX=/home/$FRAPPE_USER/tessdata

# Install Tesseract dependencies
RUN set -ex; \
    sudo apt-get update -q; \
    sudo apt-get install -y --no-install-recommends \
        ghostscript \
        imagemagick \
        libmagickwand-dev \
        tesseract-ocr \
        libtesseract-dev \
        libleptonica-dev \
        pkg-config \
    ; \
    sudo rm -rf /var/lib/apt/lists/*; \
    mkdir -p $TESSDATA_PREFIX; \
    sudo chown -R $FRAPPE_USER:$FRAPPE_USER $TESSDATA_PREFIX ; \
    wget -q https://raw.github.com/tesseract-ocr/tessdata/master/eng.traineddata -O $TESSDATA_PREFIX/eng.traineddata; \
    wget -q https://raw.github.com/tesseract-ocr/tessdata/master/equ.traineddata -O $TESSDATA_PREFIX/equ.traineddata; \
    wget -q https://raw.github.com/tesseract-ocr/tessdata/master/osd.traineddata -O $TESSDATA_PREFIX/osd.traineddata; \
    wget -q https://raw.github.com/tesseract-ocr/tessdata/master/fra.traineddata -O $TESSDATA_PREFIX/fra.traineddata; \
    wget -q https://raw.github.com/tesseract-ocr/tessdata/master/deu.traineddata -O $TESSDATA_PREFIX/deu.traineddata; \
    wget -q https://raw.github.com/tesseract-ocr/tessdata/master/spa.traineddata -O $TESSDATA_PREFIX/spa.traineddata; \
    wget -q https://raw.github.com/tesseract-ocr/tessdata/master/por.traineddata -O $TESSDATA_PREFIX/por.traineddata; \
    sudo chmod -R 755 $TESSDATA_PREFIX ; \
    sudo sed -i \
        -e 's/rights="none" pattern="PDF"/rights="read" pattern="PDF"/g' \
        /etc/ImageMagick*/policy.xml \
    ; \
    sudo mkdir -p "/home/$FRAPPE_USER"/frappe-bench/logs; \
    sudo touch "/home/$FRAPPE_USER"/frappe-bench/logs/bench.log; \
    sudo chmod 777 \
        "/home/$FRAPPE_USER"/frappe-bench/logs \
        "/home/$FRAPPE_USER"/frappe-bench/logs/* \
    ;

# Build environment variables
ARG FRAPPE_APP_TO_TEST=${FRAPPE_APP_TO_TEST}

# Copy the whole repository to app folder for manual install
COPY --chown=frappe:frappe . "/home/$FRAPPE_USER"/frappe-bench/apps/${FRAPPE_APP_TO_TEST}

# Install current app
RUN set -ex; \
    ./env/bin/pip install -q -U -e ./apps/${FRAPPE_APP_TO_TEST}; \
    bench build --app ${FRAPPE_APP_TO_TEST}

VOLUME "/home/${FRAPPE_USER}/frappe-bench/apps/${FRAPPE_APP_TO_TEST}/public"
