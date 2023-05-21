FROM mcr.microsoft.com/dotnet/sdk:2.1-stretch-slim

RUN apt-get update && \
  apt install -y curl
