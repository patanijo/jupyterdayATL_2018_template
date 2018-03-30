FROM continuumio/miniconda

LABEL maintainer=john.patanian@ge.com

#copy over the source code and the model file

COPY logging.conf /log/logging.conf

# Run the Analytic Web Service
ENTRYPOINT ["python","-m", "radish.synchronous"]
EXPOSE 5000

