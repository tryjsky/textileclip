FROM mono:5

RUN apt-get update; \
  apt-get install -y curl && \
  curl -L https://github.com/IronLanguages/ironpython2/archive/refs/tags/ipy-2.7.9.tar.gz | tar xzf - && \
  cd ironpython2-ipy-2.7.9
#  make && \
#  make install && \
#  cd .. && \
#  rm -rf ironpython2-ipy-2.7.9
