#ARG BASE_CONTAINER=jupyter/minimal-notebook
#FROM $BASE_CONTAINER
FROM jupyter/minimal-notebook

# Install guide from
# https://github.com/zabirauf/icsharp/wiki/Install-on-Unix-(Debian-7.8)
# https://github.com/3Dcube/docker-jupyter-icsharp/blob/master/Dockerfile

# Install Mono to Ubuntu 18.04
USER root
RUN apt-get update && apt-get install -yq --no-install-recommends \
    gnupg \
    && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
    echo "deb https://download.mono-project.com/repo/ubuntu stable-bionic main" | sudo tee /etc/apt/sources.list.d/mono-official-stable.list && \
    apt-get update && apt-get install -yq --no-install-recommends \
    mono-complete \
    mono-dbg \
    mono-runtime-dbg \
    ca-certificates-mono \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#RUN mozroots --import --machine --sync
RUN cert-sync /etc/ssl/certs/ca-certificates.crt && \
    git clone --recursive https://github.com/zabirauf/icsharp.git /icsharp && \
    cd /icsharp/Engine && \
    mono ./.nuget/NuGet.exe restore ./ScriptCs.sln && \
    cd /icsharp && \
    mono ./.nuget/NuGet.exe restore ./iCSharp.sln && \
    xbuild ./iCSharp.sln /property:Configuration=Release /nologo /verbosity:normal && \
    mkdir -p build/Release/bin && \
    for line in $(find ./*/bin/Release/*); do cp $line ./build/Release/bin; done

# Install kernel
RUN chown -R $NB_USER:users $HOME/.local && \
    chown -R $NB_USER:users $HOME/.mono && \
    chown -R $NB_USER:users $HOME/.nuget && \
    echo '{' > /icsharp/kernel-spec/kernel.json && \
    echo '    "argv": ["mono", "/icsharp/build/Release/bin/iCSharp.Kernel.exe", "{connection_file}"],' >> /icsharp/kernel-spec/kernel.json && \
    echo '    "display_name": "C#",' >> /icsharp/kernel-spec/kernel.json && \
    echo '    "language": "csharp"' >> /icsharp/kernel-spec/kernel.json && \
    echo '}' >> /icsharp/kernel-spec/kernel.json

# Switch back to jovyan to avoid accidental container runs as root
USER $NB_USER
RUN cd /icsharp && \
    jupyter-kernelspec install --user kernel-spec    
