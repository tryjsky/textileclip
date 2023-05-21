FROM mcr.microsoft.com/dotnet/sdk:2.1-bionic

RUN apt-get update && \
  apt install -y curl
