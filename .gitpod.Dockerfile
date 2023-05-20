FROM mono:5

RUN apt-get update && \
  apt-get install -y git curl && \
  curl -L https://github.com/IronLanguages/ironpython2/archive/refs/tags/ipy-2.7.9.tar.gz | tar xz && \
  cd IronPython-2.7.9 && \
  ./make.sh mono && \
  cd .. && \
  rm -rf IronPython-2.7.9
