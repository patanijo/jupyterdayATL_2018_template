FROM continuumio/miniconda

LABEL maintainer={{cookiecutter.author_email}}

#copy over the source code, environment file and the model file
RUN mkdir models

COPY environment.yaml /
COPY models/*.pkl /models
COPY src/app.py /
RUN conda update conda -y
RUN conda env create --file environment.yaml

# Run the Analytic Web Service
ENTRYPOINT ["/opt/conda/envs/{{ cookiecutter.project_name.lower().replace(' ', '_') }}_env/bin/python","-m", "app"]
EXPOSE 5000

