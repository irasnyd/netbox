FROM centos:7
MAINTAINER Ira W. Snyder <isnyder@lcogt.net>

EXPOSE 80
ENTRYPOINT [ "/init" ]

ENV NETBOX_VERSION v1.3.0

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

COPY init /init
COPY configuration.py /opt/netbox/netbox/
COPY gunicorn_config.py /opt/netbox/
COPY nginx.conf /etc/nginx/
COPY processes.ini /etc/supervisord.d/
