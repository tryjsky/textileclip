FROM mcr.microsoft.com/dotnet/sdk:2.1-bionic

RUN apt-get update && \
  apt install -y ca-certificates unzip && \
  wget -P /opt/ https://github.com/IronLanguages/ironpython2/releases/download/ipy-2.7.9/IronPython.2.7.9.zip && \
  unzip -d /opt/ /opt/IronPython.2.7.9.zip
