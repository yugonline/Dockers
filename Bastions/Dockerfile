FROM ubuntu:16.04

LABEL maintainer "Team Bastion"

RUN apt-get update && apt-get install -y --no-install-recommends build-essential curl libfreetype6-dev libpng12-dev libzmq3-dev pkg-config python3 python3-dev rsync software-properties-common unzip && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN curl -O https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py && rm get-pip.py

RUN pip3 --no-cache-dir install Pillow h5py ipykernel jupyter matplotlib numpy pandas quandl statistics scipy sklearn && python3 -m ipykernel.kernelspec

RUN pip3 --no-cache-dir install http://ci.tensorflow.org/view/Nightly/job/nightly-python35-linux-cpu/lastSuccessfulBuild/artifact/pip_test/whl/tensorflow-1.head-cp35-cp35m-manylinux1_x86_64.whl

RUN ln -s /usr/bin/python3 /usr/bin/python

COPY jupyter_notebook_config.py /root/.jupyter/

COPY notebooks /notebooks

COPY run_jupyter.sh /

EXPOSE 6006

EXPOSE 8888

WORKDIR "/notebooks"

CMD sh /run_jupyter.sh --allow-root
