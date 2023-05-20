FROM mono:5

RUN sed -i '-es/deb.debian.org/archive.debian.org/' /etc/apt/sources.list && \
  apt-get update; \
  apt-get install -y apt-transport-https build-essential git curl && \
  cd /tmp && \
  curl -L https://github.com/IronLanguages/ironpython2/archive/refs/tags/ipy-2.7.9.tar.gz | tar xzf - && \
  cd ironpython2-ipy-2.7.9 && \
  true
#  git init && \
#  make && \
#  make install && \
#  cd .. && \
#  rm -rf ironpython2-ipy-2.7.9
