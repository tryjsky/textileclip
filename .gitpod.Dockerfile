FROM ubuntu:bionic

RUN apt-get update && \
  apt install -y ca-certificates gnupg curl && \
  gpg --homedir /tmp --no-default-keyring --keyring /usr/share/keyrings/mono-official-archive-keyring.gpg \
  --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
  echo "deb [signed-by=/usr/share/keyrings/mono-official-archive-keyring.gpg] https://download.mono-project.com/repo/ubuntu stable-bionic main" | \
  tee /etc/apt/sources.list.d/mono-official-stable.list && \
  apt-get update && \
  apt install -y git mono-devel && \
  curl -o /tmp/ironpython_2.7.9.deb https://github.com/IronLanguages/ironpython2/releases/download/ipy-2.7.9/ironpython_2.7.9.deb && \
  dpkg -i /tmp/ironpython_2.7.9.deb
