FROM ubuntu:bionic

RUN apt-get update && \
  apt install -y ca-certificates gnupg && \
  gpg --homedir /tmp --no-default-keyring --keyring /usr/share/keyrings/mono-official-archive-keyring.gpg \
  --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
  echo "deb [signed-by=/usr/share/keyrings/mono-official-archive-keyring.gpg] https://download.mono-project.com/repo/ubuntu stable-bionic main" | \
  tee /etc/apt/sources.list.d/mono-official-stable.list && \
  apt-get update && \
  apt install -y git mono-devel libmono-system-numerics4.0-cil
