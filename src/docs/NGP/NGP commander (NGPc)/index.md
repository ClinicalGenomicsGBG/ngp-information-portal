# NGP commander (NGPc) - index.md

## About
The NGPc is a cloud-based High Performance Computing (HPC) cluster. It uses a cloud agnostic solution developed by Altair Engineering, NavOps, to provision nodes inside a cloud infrastructure, based on a job queue and job requirements. This means that the cluster does not have any compute servers / nodes by default, but it will create the appropriate servers when needed (as jobs are submitted to the queue), and remove the computation servers when they are not needed. This means that a huge amount of pipelines can be processed in parallell as there workload manager can spin up nodes to fit the current need. It also means that each pipeline will have a cost directly related to the amount of resources used.

NGPc only allow Nextflow and Snakemake based pipelines where tools are packed in singularities. Special care must be taken when building a pipeline to ensure that each step does not request more resources than it requires.

Internally, the cluster uses Altair Grid Engine as a workload manager and GMS uses Microsoft Azure as a primary cloud provider. Both Snakemake and Nextflow provide out-of-the-box compatibility with Altair Grid Engine.

Access to the compute cluster is provided through a web-based front end, Open On Demand, using SITHS-authentication. Open On Demand can provide direct command line access, as well as graphical user interfaces to manage files, start and monitor pipeline progess et cetera.

## Access

todo

