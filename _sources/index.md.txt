# Tractometry
Tractometry uses diffusion-weighted MRI (dMRI) to extract microstructural tissue properties of major white matter pathways. Here, we maintain a suite of integrated, open-source software that performs all analysis stages:

[**pyAFQ**](https://tractometry.org/pyAFQ): Automated Fiber Quantification in Python:  
&emsp;• post-processing of dMRI data  
&emsp;• delineation of major white matter pathways  
&emsp;• modeling of the tissue properties within them  
&emsp;• expects pre-processed data. Data can be pre-processed with [*QSIprep*](https://qsiprep.readthedocs.io/en/latest/)  

[**AFQ-Insight**](https://tractometry.org/AFQ-Insight): Machine learning and statistics for tractomtery:  
&emsp;• novel machine learning models such as convolutional neural networks (CNNs) and recurrent neural network (RNNs)  
&emsp;• more standard approaches, such as ordinary least squares (OLS) and principal component analysis (PCA)  
&emsp;• integrated with [*scikit-learn*](https://scikit-learn.org/stable/) and adapted for tract data, bridging these two worlds  

[**Tractable**](https://tractometry.org/tractable): R-based statistical analysis of tractometry:  
&emsp;• focuses on generalized additive models (GAMs)  

[**AFQ-Browser**](https://tractometry.org/AFQ-Browser): Interactive exploratory visualization and sharing of tractometry studies:  
&emsp;• allows researchers to interactively query the data to explore patterns  

[**Tractoscope**](https://nrdg.github.io/tractoscope): Visualization of large openly-available tractometry studies.

## [Examples](examples/index.md)

**pyAFQ**

- *Basics*  

  • [Introduction](examples/001.md)  
  • [Visualizing AFQ derivatives](examples/002.md)

- *Extensions* 

  • [BabyAFQ: tractometry for infant dMRI data](examples/003.md)  
  • [RecoBundles for tract delineation](examples/004.md)

- *Adding New Bundles* 

  • [Optic Radiations](examples/005.md)  
  • [Acoustic Radiations](examples/006.md)  
  • [SLF 1/2/3 Subdivisions](examples/007.md)

- *Acceleration*

  • [GPU Tractography](examples/008.md)  
  • [Multiprocessing for Model Fitting (Ray)](examples/009.md)

**AFQ-Insight**

- [Parametric Statistics for Group Comparison](examples/010.md)  
- [Regression: Predict Age from White Matter](examples/011.md)  
- [Classification: ALS Diagnosis](examples/012.md)

**Tractable**

- [Fitting Generalized Additive Models (GAMs)](examples/013.md)

## How to get help

We encourage you to seek help and share your questions with the community. Here's how to get support for Tractometry-related projects:

1. **Check [NeuroStars](https://neurostars.org/)**  
   NeuroStars is a community forum for neuroimaging questions. Search for existing answers or post your question using the `pyafq`, `afq-insight`, or other relevant tags.

2. **Browse or open issues on the respective GitHub repositories**  
   Many questions may already be answered in the project's issue tracker. If not, you can open a new issue:

   - [**pyAFQ**](https://github.com/tractometry/pyAFQ/issues)
   - [**AFQ-Insight**](https://github.com/tractometry/AFQ-Insight/issues)
   - [**Tractable**](https://github.com/tractometry/tractable/issues)
   - [**AFQ-Browser**](https://github.com/tractometry/AFQ-Browser/issues)
   - [**Tractoscope**](https://github.com/tractometry/tractoscope/issues)

3. **Include details when asking for help**  
   When posting, please include:
   - The software version you're using
   - Relevant code or command-line calls
   - Error messages (if any)
   - Expected vs. actual behavior


```{eval-rst}

.. toctree::
   :maxdepth: 1
   :hidden:

   examples/index.md
```