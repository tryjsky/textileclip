FROM mcr.microsoft.com/dotnet/sdk:2.1-bionic

RUN apt-get update && \
  apt install -y ca-certificates && \
  wget -P /tmp/ https://github.com/IronLanguages/ironpython2/releases/download/ipy-2.7.9/ironpython_2.7.9.deb && \
  dpkg -i /tmp/ironpython_2.7.9.deb
