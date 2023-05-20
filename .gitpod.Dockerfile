FROM ubuntu:bionic

RUN apt-get update && \
  apt-get install -y git gnupg && \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
  echo "deb https://download.mono-project.com/repo/ubuntu stable-bionic main" | tee /etc/apt/sources.list.d/mono-official-stable.list && \
  apt-get update && \
  apt install -y mono-devel libmono-system-numerics4.0-cil
