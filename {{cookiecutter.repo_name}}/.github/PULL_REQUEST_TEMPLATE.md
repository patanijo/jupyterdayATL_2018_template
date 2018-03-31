# Data Science Project Pull Request Checklist

## {{cookiecutter.project_name}}


__Adapted From Jeff Leek Book "Elements of Analytic Style"__

### Answering the question

[] Did you specify the type of data analytic question (e.g. exploration, association causality) before touching the data?
[] Did you define the metric for success before beginning?
[] Did you understand the context for the question and the scientific or business application? 
[] Did you record the experimental design?
[] Did you consider whether the question could be answered with the available data?

### Checking the data
 
[] Did you plot univariate and multivariate summaries of the data?
[] Did you check for outliers?
[] Did you identify the missing data code?

### Tidying the data
 
[] Is each variable one column?
[] Is each observation one row?
[] Do different data types appear in each table?
[] Did you record the recipe for moving from raw to tidy data?
[] Did you record all parameters, units, and functions applied to the data?

### Exploratory analysis
 
[] Did you identify missing values?
[] Did you make univariate plots (histograms, density plots, boxplots)?
[] Did you consider correlations between variables (scatterplots)?
[] Did you check the units of all data points to make sure they are in the right range?
[] Did you try to identify any errors or miscoding of variables? 
[] Did you consider plotting on a log scale?
[] Would a scatterplot be more informative?

### Inference
 
[] Did you identify what large population you are trying to describe?
[] Did you clearly identify the quantities of interest in your model?
[] Did you consider potential confounders?
[] Did you identify and model potential sources of correlation such as measurements over time or space?
[] Did you calculate a measure of uncertainty for each estimate on the scientific scale?

### Prediction
[] Did you identify in advance your error measure?
[] Did you immediately split your data into training and validation?
[] Did you use cross validation, resampling, or bootstrapping only on the training data?
[] Did you create features using only the training data?
[] Did you estimate parameters only on the training data?
[] Did you fix all features, parameters, and models before applying to the validation data?
[] Did you apply only one final model to the validation data and report the error rate?

### Causality
 
[] Did you identify whether your study was randomized?
[] Did you identify potential reasons that causality may not be appropriate such as confounders, missing data, non-ignorable dropout, or unblinded experiments?
[] If not, did you avoid using language that would imply cause and effect?

###  Written analyses 
[] Did you describe the question of interest?
[] Did you describe the data set, experimental design, and question you are answering?
[] Did you specify the type of data analytic question you are answering?
[] Did you specify in clear notation the exact model you are fitting?
[] Did you explain on the scale of interest what each estimate and measure of uncertainty means?
[] Did you report a measure of uncertainty for each estimate on the scientific scale?

### Figures 
[] Does each figure communicate an important piece of information or address a question of interest?
[] Do all your figures include plain language axis labels?
[] Is the font size large enough to read?
[] Does every figure have a detailed caption that explains all axes, legends, and trends in the figure?

### Reproducibility 
[] Did you avoid doing calculations manually?
[] Did you create a script that reproduces all your analyses?
[] Did you save the raw and processed versions of your data?
[] Did you record all versions of the software you used to process the data `Hint use conda env export or pip freeze`?
[] Did you try to have someone else run your analysis code to confirm they got the same answers?
