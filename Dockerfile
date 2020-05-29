FROM centos
RUN yum install python36 -y
RUN pip3 install --upgrade pip
RUN  pip install -U setuptools  && pip install numpy && pip install tensorflow==1.5.0 && pip install keras==2.2.4 && pip install pillow
ENV echo 1 > /proc/sys/vm/overcommit_memory


