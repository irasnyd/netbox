FROM centos:7
MAINTAINER Ira W. Snyder <isnyder@lco.global>

EXPOSE 80
ENTRYPOINT [ "/init" ]

ENV NETBOX_VERSION v2.2.6

RUN yum -y install epel-release \
        && yum -y install gcc git graphviz libffi-devel libxml2-devel \
                libxslt-devel nginx openssl-devel postgresql postgresql-devel \
                python python-devel python-gunicorn python-pip supervisor \
        && yum -y update \
        && yum -y clean all

RUN mkdir -p /opt/netbox \
        && curl -L -o netbox.tar.gz "https://github.com/digitalocean/netbox/archive/${NETBOX_VERSION}.tar.gz" \
        && tar -xf netbox.tar.gz --strip-components=1 -C /opt/netbox \
        && rm -f netbox.tar.gz \
        && pip install -r /opt/netbox/requirements.txt \
        && rm -rf ~/.cache/pip

COPY docker/ /
